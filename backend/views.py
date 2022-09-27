from unicodedata import category
from urllib import response
from django.shortcuts import render, redirect
import requests
import json

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def quiz_page(request):
    response = requests.get('https://opentdb.com/api.php?amount=10')
    results = response.json()["results"]
    score = 0
    if request.method == 'POST':
        for key in request.POST:
            ans = request.POST[key]
            if ans == 'correct':
                score += 1
        return redirect('results', pk=score)
    context = {'results' : results }
    return render(request, 'quiz.html', context)

def result_page(request, pk):
    context = {'pk' : pk }
    return render(request, 'results.html', context)