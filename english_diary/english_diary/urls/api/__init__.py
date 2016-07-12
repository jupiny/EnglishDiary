from django.conf.urls import url, include


urlpatterns = [
    url(r'^diary/', include("english_diary.urls.api.diary", namespace="diary")),
    url(r'^naver/', include("english_diary.urls.api.naver", namespace="naver")),
]
