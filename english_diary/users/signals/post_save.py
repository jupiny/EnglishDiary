from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.conf import settings

from profiles.utils import generate_user_activation_key
from profiles.utils import set_expiration_date
from profiles.models import Profile
from users.tasks.send_email_verification import SendEmailVerificationTask


@receiver(post_save, sender=get_user_model())
def post_save_user(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(
            user=instance,
            verification_key=generate_user_activation_key(instance.id),
            key_expires=set_expiration_date(settings.KEY_EXPIRES_DAY),
        )

        task = SendEmailVerificationTask()
        task.delay(instance.id)
