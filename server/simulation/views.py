from django.shortcuts import render
import random

def simulation(request):
    # 시뮬레이션 페이지 요청에 보낼 Audio Feauture별 수치를 우선 초기화
    content = {
        'dateyear_input' : 2023,
        'datemonth_input' : 1,
        'danceability_input' : 0,
        'energy_input' : 0,
        'loudness_input' : 0,
        'mode_input' : 0,
        'speechiness_input' : 0,
        'acousticness_input' : 0,
        'instrumentalness_input' : 0,
        'liveness_input' : 0,
        'valence_input' : 0,
        'tempo_input' : 0,
        'rank' : 0
    }
    # GET 요청일 경우(시뮬레이션 페이지에 처음 들어온 경우)
    if request.method == 'GET':
        # 0으로 초기화한 Audio Feature 수치를 그대로 반환
        return render(request, 'simulation/simulation.html', content)
    # POST 요청일 경우(시뮬레이션 페이지에서 Audio Feauture을 설정하여 POST 요청했을 경우)
    elif request.method == 'POST':
        # 유저가 설정한 Audio Feauture 수치를 모두 가져옴
        # dateyear = request.POST.get('dateyear')
        # datemonth = request.POST.get('datemonth')
        danceability = request.POST.get('danceability')
        energy = request.POST.get('energy')
        loudness = request.POST.get('loudness')
        mode = request.POST.get('mode')
        speechiness = request.POST.get('speechiness')
        acousticness = request.POST.get('acousticness')
        instrumentalness = request.POST.get('instrumentalness')
        liveness = request.POST.get('liveness')
        valence = request.POST.get('valence')
        tempo = request.POST.get('tempo')
        
        # from datetime import datetime
        # defDate = datetime.strptime('2023-01-01', '%Y-%m-%d')
        # dateStr = f"{dateyear}-{datemonth}" + '-01'
        # dateSet = datetime.strptime(dateStr, '%Y-%m-%d')
        # deltaWeek = (dateSet - defDate).days // 7
        # date = 3132 + deltaWeek
        # print("Date : ", date)

        import numpy as np
        # temp_data = np.array([[date, danceability, energy, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo]], dtype=np.int32)
        # features = ['date', 'danceability', 'energy', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
        temp_data = np.array([[danceability, energy, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo]], dtype=np.int32)
        features = ['danceability', 'energy', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
        import pandas as pd
        temp_data = pd.DataFrame(temp_data, columns=features)

        # rank 계산 
        import pickle
        # 모델과 (입력값 전처리 용) 스케일러, LDA 로드
        try:
            # with open('../models/Standardized_LDA10.pkl', 'rb') as f:
            #     standardized_LDA_model = pickle.load(f)

            # LDA 전처리 객체 사용
            with open('../models/lda2023.pkl', 'rb') as f:
                LDA2023_model = pickle.load(f)
                
            # with open('../models/lda.pkl', 'rb') as f:
            #     lda = pickle.load(f)

            # 2023년 LDA 데이터로 학습시킨 KNN 회귀 모델 사용
            with open('../models/2023lda.pkl', 'rb') as f:
                lda = pickle.load(f)
                
            # with open('../models/StdScaler.pkl', 'rb') as f:
            #     stdScaler = pickle.load(f)
        except Exception as e:
            print("Maybe Model or Preprocessing Object is not in directory.")
            print(e)
        # 유저가 설정한 입력값 전처리 후 모델에 넣어서 예측값 추출
        try:
            # 표준화 안 쓰는 모델을 사용하기로 결정
            # scaled_data = stdScaler.transform(temp_data)
            # data = lda.transform(scaled_data)
            # rank = int(standardized_LDA_model.predict(data)[0])
            data = lda.transform(temp_data)
            rank = int(LDA2023_model.predict(data)[0])
            print("Model is successfully loaded. Prediction complete.")
            print("Predicted Rank :", rank)
        # 입력값 전처리 객체 또는 모델 객체가 정상적으로 받아와지지 않았다면 그냥 랜덤값 출력(예외 처리용)
        except Exception as e:
            print("Exception Occured. Random Output Generated.")
            print(e)
            rank = random.randint(1, 100)

        # Audio Feature 수치를 사용자가 설정한 수치값으로 변경 후 Response
        content['rank'] = rank
        # content['dateyear_input'] = dateyear
        # content['datemonth_input'] = datemonth
        content['danceability_input'] = danceability
        content['energy_input'] = energy
        content['loudness_input'] = loudness
        content['mode_input'] = mode
        content['speechiness_input'] = speechiness
        content['acousticness_input'] = acousticness
        content['instrumentalness_input'] = instrumentalness
        content['liveness_input'] = liveness
        content['valence_input'] = valence
        content['tempo_input'] = tempo
        return render(request, 'simulation/simulation.html', content)
