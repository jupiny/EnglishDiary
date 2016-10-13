from django.conf.urls import url, include

from users.views import *


urlpatterns = [
    url(r'^signin/$', SigninView.as_view(), name="signin"),
    url(r'^signout/$', SignoutView.as_view(), name="signout"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^mypage/$', MypageView.as_view(), name="mypage"),
    url(r'^verify/(?P<verification_key>\w+)/$', EmailVerificationView.as_view(), name="email_verification"),
    url(r'^verify/(?P<verification_key>\w+)/expire/$', KeyExpiresView.as_view(), name="key_expires"),
    url(r'^renew/$', RenewKeyView.as_view(), name="renew_key"),
]
