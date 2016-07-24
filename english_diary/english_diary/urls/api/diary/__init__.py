from django.conf.urls import url

from diaries.api.diary import *


urlpatterns = [
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', DiaryDetailAPIView.as_view(), name="detail"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/words/$', DiaryMontlyWordsAPIView.as_view(), name="monthly_words"),
    url(r'^$', DiaryCreateAPIView.as_view(), name="create"),
]
