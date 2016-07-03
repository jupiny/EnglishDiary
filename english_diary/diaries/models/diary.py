from django.db import models
from django.conf import settings

from users.models import User


class Diary(models.Model):

    user = models.ForeignKey(User)
    content = models.TextField()

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
    )

    diary_image = models.ImageField(
        blank=True,
        null=True,
    )

    word_count = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0,
    )

    diary_type = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        default=0,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    datetime = models.CharField(
        max_length=10,
    )
