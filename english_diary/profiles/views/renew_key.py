from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib import messages

from profiles.utils import generate_user_activation_key
from profiles.utils import set_expiration_date
from profiles.models import Profile
from users.tasks import SendVerificationEmailTask


class RenewKeyView(View):

    def post(self, request, *args, **kwargs):
        verification_key = request.POST.get("verification_key")
        profile = get_object_or_404(Profile, verification_key=verification_key)
        user = profile.user

        # Renew user verification key
        profile.verification_key = generate_user_activation_key(user.id)
        profile.key_expires = set_expiration_date(settings.KEY_EXPIRES_DAY)
        profile.save()

        task = SendVerificationEmailTask()
        task.delay(user.id)

        messages.add_message(
            request,
            messages.SUCCESS,
            settings.RESEND_EMAIL_VERIFICATION_MESSAGE,
        )

        return redirect(reverse("home"))
