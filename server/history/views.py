from django.shortcuts import render

def history(request):
    return render(request, 'history/history.html')
