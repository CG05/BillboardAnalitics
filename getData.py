import getBillboardData
import getSpotifyData

def getData(s_year, e_year):
    getBillboardData.getBillboardData(s_year, e_year)
    getSpotifyData.getSpotifyData(s_year, e_year)
    
# 시작년, 끝년 넣고 실행
getData(2007, 2022)