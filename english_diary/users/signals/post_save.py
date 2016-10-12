from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.conf import settings

from users.tasks.send_email_verification import SendEmailVerificationTask
from users.utils import generate_user_activation_key
from users.utils import set_expiration_date
from users.models import Profile


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
