from django.conf.urls import include
from django.urls import path

from .views import home, notice_detail, worker_detail

urlpatterns = [
    path('', home),
    path('notices', home),
    path('workers', home),
    path('notices/add', home),
    path('notices/my', home),
    path('user/password/change', home),
    path('user/profile', home),
    path('notice/details/<int:noticeId>', notice_detail),
    path('workers/details/<int:workerId>', worker_detail),
]
