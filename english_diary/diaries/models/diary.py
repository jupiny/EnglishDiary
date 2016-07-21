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

    @property
    def used_words(self):
        diary_content = self.content.lower()
        for puctuation_mark in settings.PUCTUATION_MARKS:
            diary_content = diary_content.replace(puctuation_mark, "")
        return list(set(diary_content.split()))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    datetime = models.CharField(
        max_length=11,
        default="",
    )
