# cid, secret 본인 걸로 수정 후 맨 마지막 줄 함수에 (시작년, 끝년)을 넣고 모두실행
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
import pandas as pd
import json
import time
import re
import difflib
from sklearn.preprocessing import LabelEncoder

# 본인 cid, secret 입력
cid = "8494dc579e694b9a91d1728fe3be9b96" 
secret = "d571c3a3139849a68734f206590794fa"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

af = ['danceability', 'energy', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
columns = ['date', 'danceability', 'energy', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
trackIDs = []
songdict = {}

# get json file of billboard

def getJSONFile(s_year, e_year):
    with open(f'data/billboard/billboard_{s_year}to{e_year}.json', 'r') as f:
        data = f.read()
        data = json.loads(data)
    return data

def getSongSet(data):
    songSet = set()
    for chart in data:
        for song in chart:
            songSet.add((song[1], song[2]))
    return songSet

def getIDsAt(num, ls):
    temp = []
    for i in range(num * 77, num * 77 + 77):
        if i < len(ls) - 1:
            # artist = ls[i][1].replace(" x ", " & ").replace(" X ", " & ").replace("Featuring", "&").replace("featuring", "&").replace("With", "&").replace("with", "&").replace("And", "&").replace("and", "&")
            # raw string으로 변환 처리
            artist = re.sub(r"( x | X |Featuring|featuring|With|with|And|and)", "&", ls[i][1], flags=re.IGNORECASE)
            search = sp.search(f"{ls[i][0]} - {artist}", limit=1, type=['track', 'artist'])
            track = search['tracks']['items'][0]
            trackID = track['id']
            trackName = track['name']
            name = ls[i][0]
            # trackName과 name의 문자열을 비교해서 같은 정도가 어느정도인지 확인
            similarity = difflib.SequenceMatcher(None, trackName.lower(), name.lower()).ratio()
            if (trackName.lower() in name.lower()) or (name.lower() in trackName.lower()) or (similarity >= 0.5):
                temp.append(trackID)
                songdict[trackID] = [f"{ls[i][0]} - {ls[i][1]}", []]
        time.sleep(0.5)
    trackIDs.append(temp)
    
def getIDs(len, ls):
    for i in range(len):
        getIDsAt(i, ls)
        
def getFeaturesAt(num):
    features = sp.audio_features(tracks=trackIDs[num])
    for id, feature in zip(trackIDs[num], features):
        songdict[id] = [songdict[id][0], [feature["danceability"], feature["energy"], feature["loudness"], feature["mode"], feature["speechiness"], feature["acousticness"], feature["instrumentalness"], feature["liveness"], feature["valence"], feature["tempo"]]]
        
def getFeatures(len):
    for i in range(len):
        getFeaturesAt(i)
        time.sleep(5)
        
def getSpotifyData(s_year, e_year):
    data = getJSONFile(s_year, e_year)
    songSet = getSongSet(data)
    ls = list(songSet)
    length = len(ls) // 77 + 1
    
    getIDs(length, ls)
    getFeatures(len(trackIDs))
    featuresDict = {}
    for key, value in songdict.items():
        featuresDict[value[0]] = value[1]
        
    for chart in data:
        for song in chart:
            query = song[1] + " - " + song[2]
            song[4] = featuresDict.get(query)
    
    label = []
    for chart in data:
        for song in chart:
            if song[4] == None:
                label.append(50)
            else:
                label.append(song[3])
    label = np.array(label)
    dataList = []
    index = []
    arr = []
    for chart in data:
        for song in chart:
            index.append(song[0])
            if song[4] != None:
                arr = song[4]
                
            else:
                arr = np.empty(10)
                arr[:] = np.nan
            # arr 앞에 song[0]을 추가
            arr = np.concatenate(([song[0]], arr))
            dataList.append(arr)
    df = pd.DataFrame(data=dataList, index=index, columns=columns)
    label = pd.Series(label, index=index)

    for col in columns:
        if (df[col].dtype == "object") or (df[col].dtype == "O"):
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
    df.fillna(df.median(), inplace=True)
    
    df.to_csv(f"data/dataframes/dataframe_{s_year}to{e_year}.csv")
    label.to_csv(f"data/dataframes/label_{s_year}to{e_year}.csv")
    
getSpotifyData()
