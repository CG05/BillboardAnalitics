from django.shortcuts import render

def introduction(request):
    return render(request, 'introduction/introduction.html')