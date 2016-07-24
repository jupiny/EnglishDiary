from django.conf.urls import url

from users.api.user import *


urlpatterns = [
    url(r'^email/$', UserEmailAPIView.as_view(), name="email"),
    url(r'^password/$', UserPasswordAPIView.as_view(), name="password"),
    url(r'^email_notification/$', UserEmailNotificationAPIView.as_view(), name="email_notification"),
    url(r'^delete/$', UserDeleteAPIView.as_view(), name="delete"),
]
