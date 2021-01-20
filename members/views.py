from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members


# Create your views here.
def index(req):
    return HttpResponse("Hello World@@@")

def git(req):
    return HttpResponse("<h2>git version</h2>")

def test(req):
    return HttpResponse("<h1>hello</h1>")
def test2(req):
    return HttpResponse("<h1>test2</h1>")
def signup(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['useremail']
        #username == exit
        # h2로 나가기를 출력
        #if username == 'exit' :
        #    return HttpResponse('나가기')
        #elif username == 'codingon':
        #    return render(req, 'login.html')

        member = Members(
            username = username,
            useremail = email
        )
        
        member.save()
        res_data = {}
        res_data['res'] = '등록성공'

        return render(req, 'index.html', res_data)

        print(req.POST['username'])
    return render(req, 'index.html')

