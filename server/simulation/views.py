from django.shortcuts import render
import random

def simulation(request):
    # 시뮬레이션 페이지 요청에 보낼 Audio Feauture별 수치를 우선 0으로 초기화
    content = {
        'date_input' : 0,
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
        date = request.POST.get('date')
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

        import numpy as np
        data = np.array([date, danceability, energy, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo])

        # rank 계산 

        # =============== 공사중 =====================
        import pickle
        # with open('../models/Standardized.pkl', 'rb') as f:
        #     standardized_model = pickle.load(f)
        # 표준화 모델 로드
        # try:
        #     with open('../models/Standardized.pkl', 'rb') as f:
        #         standardized_model = pickle.load(f)
        # except:
        #     print("Standardized Model Not Found")
        # PCA 모델 로드
        # try:
        #     with open('C:\itbank\preject2\project\BillboardAnalitics\models\Standardized.pkl', 'rb') as f:
        #         standardized_PCA_model = pickle.load(f)
        # except:
        #     print("Standardized PCA Model Not Found")

        # try:
        #     rank = standardized_model.predict(data)
        #     print("Predicted Rank :", rank)
        # except Exception as e:
        #     print(e)
        #     rank = random.randint(1, 100)

        # 랜덤값 출력
        rank = random.randint(1, 100)

        # Audio Feature 수치를 사용자가 설정한 수치값으로 변경 후 Response
        content['rank'] = rank
        content['date_input'] = date
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
