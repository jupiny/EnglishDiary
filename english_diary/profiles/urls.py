from django.conf.urls import url, include

from profiles.views import *


urlpatterns = [
    url(r'^verify/(?P<verification_key>\w+)/$', EmailVerificationView.as_view(), name="email_verification"),
    url(r'^verify/(?P<verification_key>\w+)/expire/$', KeyExpiresView.as_view(), name="key_expires"),
    url(r'^renew/$', RenewKeyView.as_view(), name="renew_key"),
]
