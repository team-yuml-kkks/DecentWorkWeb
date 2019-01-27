from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token


def home(request):
    return _show_view(request)


def notice_detail(request, noticeId):
    return _show_view(request)


def worker_detail(request, workerId):
    return _show_view(request)


def _show_view(request):
    _get_token(request)
    return render(request, 'home.html')


def _get_token(request):
    if request.user.is_authenticated:
        token = Token.objects.filter(user=request.user).values('key').first()
        request.session['token'] = token['key']

