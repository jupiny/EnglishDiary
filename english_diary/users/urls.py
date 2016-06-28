from django.conf.urls import url, include

from users.views import *


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
]
