from django.conf.urls import url, include

from diaries.api.naver import *


urlpatterns = [
    url(r'^translate/$', TranslateAPIView.as_view(), name='translate'),
    url(r'^dict/(?P<find_word>.*)/$', NaverDictionaryAPIView.as_view(), name="dict"),
]
