from django.conf.urls import url, include

from diaries.api import *


urlpatterns = [
    url(r'^diary/(?P<datetime>\d{4}-\d{2}-\d{2})/$', DiaryDetailAPIView.as_view(), name="detail"),
]
