# 맨 마지막 줄 함수에 (시작년, 끝년)을 넣고 모두실행
import billboard
from datetime import datetime, timedelta
import numpy as np
import json

def getYearsChart(s_year, e_year):
    yearchartarr = []
    curday = datetime(s_year, 1, 1)
    while (curday.year == e_year):
        dayformat = curday.strftime('%Y-%m-%d')
        charts = billboard.ChartData('hot-100', date=dayformat)
        curday += timedelta(weeks=1)
        dayarr = []
        for song in charts:
            arr = [dayformat, song.title, song.artist, song.rank, []]
            dayarr.append(arr)
        yearchartarr.append(dayarr)
        yearchart = np.array(yearchartarr, dtype=object)
    return yearchart


# json으로 저장
def getBillboardData(s_year, e_year):
    yearsChart = getYearsChart(s_year, e_year)
    json_data = json.dumps(yearsChart.tolist())
    with open(f'data/billboard/billboard_{s_year}to{e_year}.json', 'w') as f:
        f.write(json_data)
