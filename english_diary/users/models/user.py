from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
    )

    profile_image = models.ImageField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO : 어떤 필드로 해야 하나 + 자동저장은 post_save() 처럼 하세요
    words = models.TextField(
        blank=True,
        null=True,
    )
