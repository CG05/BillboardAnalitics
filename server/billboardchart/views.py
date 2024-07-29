from django.shortcuts import render

def billboardchart(request):
    return render(request, 'billboardchart/billboardchart.html')
