from django.db import models
from .user import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
    )
    activation_key = models.CharField(
        max_length=40,
    )
    key_expires = models.DateTimeField()
