from django.shortcuts import render
from django.http import Http404
from billboard import ChartData
from datetime import datetime, timedelta

# 빌보드 차트 뷰 함수
def billboardchart(request, date):
    # 입력받은 date 형식이 올바른지 확인(13월을 입력하는 등 유효하지 않으면 404로 추방)
    try:
        checkday = datetime.strptime(date, '%Y-%m-%d')
    except:
        raise Http404("Invalid date")
    
    # 입력된 날짜 정보 저장
    inputdate = date

    # 입력된 날짜가 미래의 날짜면 현재 날짜로 조정
    if datetime.now() < checkday:
        checkday = datetime.now()
        inputdate = checkday.strftime('%Y-%m-%d')
    # 입력된 날짜가 1963년 이전의 날짜면 1963년으로 조정(우리 가게는 1963년 이후 노래만 취급합니다)
    elif checkday < datetime(1963, 1, 1):
        checkday = datetime(1963, 1, 1)
    # 빌보드 차트 공개일인 토요일로 날짜 이동
    while checkday.weekday() != 5:
        checkday -= timedelta(days=1)
    checkday = checkday.strftime('%Y-%m-%d')

    # 입력된 날짜 기준 가장 최근(해당되는 날짜의 지난 토요일)의 빌보드 차트 불러옴
    chart = ChartData('hot-100', date=checkday)

    # 불러온 차트에 속한 100곡을 리스트로 저장
    chartlist = []
    for i in range(100):
        chartlist.append(chart[i])
    content = {
        'inputdate' : inputdate,
        'date' : chart.date,
        'chart' : chartlist
    }
    return render(request, 'billboardchart/billboardchart.html', content)
