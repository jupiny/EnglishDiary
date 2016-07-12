from django.conf.urls import url, include

from diaries.api import *


urlpatterns = [
    url(r'^diary/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', DiaryDetailAPIView.as_view(), name="detail"),
    url(r'^diary/create/$', DiaryCreateAPIView.as_view(), name="create"),
    url(r'^diary/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/delete/$',
        DiaryDeleteAPIView.as_view(), name="delete"),
    url(r'^dict/(?P<find_word>\w+)/$', NaverDictionaryAPIView.as_view(), name="dict"),
    url(r'translate/$', TranslateAPIView.as_view(), name='translate'),
    url(r'^translate/$', TranslateAPIView.as_view(), name='translate'),
]
