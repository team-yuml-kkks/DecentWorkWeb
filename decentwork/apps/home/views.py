from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token

@login_required
def home(request):
    token = Token.objects.filter(user=request.user).values('key').first()
    request.session['token'] = token['key']
    return render(request, 'home.html')


@login_required
def notice_detail(request, noticeId):
    token = Token.objects.filter(user=request.user).values('key').first()
    request.session['token'] = token['key']
    return render(request, 'home.html')


@login_required
def worker_detail(request, workerId):
    token = Token.objects.filter(user=request.user).values('key').first()
    request.session['token'] = token['key']
    return render(request, 'home.html')