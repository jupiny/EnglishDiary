from django.conf.urls import url, include

from profiles.views import *


urlpatterns = [
    url(r'^verify/(?P<verification_key>\w+)/$', VerifyEmailView.as_view(), name="verify_email"),
    url(r'^verify/(?P<verification_key>\w+)/expire/$', KeyExpiresView.as_view(), name="key_expires"),
    url(r'^renew/$', RenewKeyView.as_view(), name="renew_key"),
]
