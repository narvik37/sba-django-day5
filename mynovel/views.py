from django.shortcuts import render, redirect
from django.http.response import HttpResponse
#from .models import Members

def my_novel(req, char1, char2):
    context = {"word":'6 word story', "char1":char1, "char2":char2}
    return render(req, 'novel.html', context)

def empty(req):
    return HttpResponse('단어 두개를 입력해주세요.')

