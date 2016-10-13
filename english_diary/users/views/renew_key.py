from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib import messages

from users.utils import generate_user_activation_key
from users.utils import set_expiration_date
from users.tasks.send_email_verification import SendEmailVerificationTask
from users.models import Profile


class RenewKeyView(View):

    def post(self, request, *args, **kwargs):
        verification_key = request.POST.get("verification_key")
        profile = get_object_or_404(Profile, verification_key=verification_key)
        user = profile.user

        # Renew user verification key
        profile.verification_key = generate_user_activation_key(user.id)
        profile.key_expires = set_expiration_date(settings.KEY_EXPIRES_DAY)
        profile.save()

        task = SendEmailVerificationTask()
        task.delay(user.id)

        messages.add_message(
            request,
            messages.SUCCESS,
            settings.RESEND_EMAIL_VERIFICATION_MESSAGE,
        )

        return redirect(reverse("home"))
