from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('login/', views.UserApiLogin.as_view()),
    path('tokensignin/', views.TokenSignIn.as_view()),
]
