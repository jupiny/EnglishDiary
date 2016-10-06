from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.conf import settings
import datetime

from users.tasks.send_signup_email import SendSignupEmailTask
from users.utils import generate_user_activation_key
from users.models import Profile


@receiver(post_save, sender=get_user_model())
def post_save_user(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(
            user=instance,
            activation_key=generate_user_activation_key(instance.id),
            key_expires=datetime.datetime.strftime(
                datetime.datetime.now()+datetime.timedelta(days=settings.KEY_EXPIRES_DAY),
                "%Y-%m-%d %H:%M:%S",
            ),
        )

        task = SendSignupEmailTask()
        task.delay(instance.id)
