from django.conf.urls import url
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'engagments', views.EngagmentsViewSet)
router.register(r'user/engagments', views.UserEngagmentsListViewSet, base_name="user_engagments")
router.register(r'assign/user', views.AssignUserViewSet, base_name="assing")

urlpatterns = [] + router.urls
