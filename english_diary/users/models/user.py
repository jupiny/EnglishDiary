from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
    )

    # TODO: ImageField with pillow

    # TODO: created_at, updated_at
