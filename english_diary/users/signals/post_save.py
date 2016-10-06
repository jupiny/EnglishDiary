from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.conf import settings
import datetime

from users.tasks.send_email_verification import SendEmailVerificationTask
from users.utils import generate_user_activation_key
from users.models import Profile


@receiver(post_save, sender=get_user_model())
def post_save_user(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(
            user=instance,
            verification_key=generate_user_activation_key(instance.id),
            key_expires=datetime.datetime.strftime(
                datetime.datetime.now()+datetime.timedelta(days=settings.KEY_EXPIRES_DAY),
                "%Y-%m-%d %H:%M:%S",
            ),
        )

        task = SendEmailVerificationTask()
        task.delay(instance.id)
