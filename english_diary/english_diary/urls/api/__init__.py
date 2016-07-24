from django.conf.urls import url, include

from diaries.api import *


urlpatterns = [
    url(r'^diary/', include("english_diary.urls.api.diary", namespace="diary")),
    url(r'^naver/', include("english_diary.urls.api.naver", namespace="naver")),
    url(r'^clipboard/$', SetClipboardView.as_view(), name="clipboard"),
    url(r'^user/', include("english_diary.urls.api.user", namespace="user")),
]
