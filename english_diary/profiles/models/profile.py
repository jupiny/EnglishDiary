from django.db import models
import datetime

from users.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
    )
    verification_key = models.CharField(
        max_length=40,
    )
    key_expires = models.DateTimeField()

    @property
    def is_expired_key(self):
        return datetime.datetime.now() > self.key_expires
