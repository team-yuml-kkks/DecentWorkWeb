from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token


def home(request):
    if request.user.is_authenticated:
        token = Token.objects.filter(user=request.user).values('key').first()
        request.session['token'] = token['key']
    return render(request, 'home.html')


def notice_detail(request, noticeId):
    token = Token.objects.filter(user=request.user).values('key').first()
    request.session['token'] = token['key']
    return render(request, 'home.html')


def worker_detail(request, workerId):
    token = Token.objects.filter(user=request.user).values('key').first()
    request.session['token'] = token['key']
    return render(request, 'home.html')