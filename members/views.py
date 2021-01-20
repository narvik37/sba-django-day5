from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members


# Create your views here.

def gugu(req):
    num = req.GET.get('num', '')#get이 들어오면 num에 대입, 안들어오면 그대로
    
    return HttpResponse(f'<h1>{num_gugu(num)} </h1>')
    return HttpResponse('123')

def num_gugu(num):
    str = ""
    for i in range (1,10):
        str += f"{num} * {i} = {int(num) * i}<br>"
    return str

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

