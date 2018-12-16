from django.conf.urls import url
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.EngagmentsViewSet)
router.register(r'user/engagments', views.UserEngagmentsListViewSet, base_name="user_engagments")

urlpatterns = [] + router.urls
