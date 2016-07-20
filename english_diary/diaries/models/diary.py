from django.db import models
from django.conf import settings

from users.models import User


class GetOrNoneManager(models.Manager):
    """
    Adds get_or_none method to objects
    """
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None


class Diary(models.Model):

    objects = GetOrNoneManager()
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

    @property
    def used_words(self):
        diary_content = self.content
        for puctuation_mark in settings.PUCTUATION_MARKS:
            diary_content = diary_content.replace(puctuation_mark, "")
        return list(set(diary_content.split()))

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
