from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    email_notification = models.BooleanField(
        default=True,
    )

    def monthly_words(self, **kwargs):
        year = kwargs.get("year")
        month = kwargs.get("month")
        datetime = year+"/"+month+"/"
        diaries = self.diary_set.filter(datetime__contains=datetime)

        monthly_words = []
        for diary in diaries:
            monthly_words += diary.used_words
        return monthly_words

    def monthly_words_count(self, **kwargs):
        monthly_words = self.monthly_words(
            **kwargs,
        )
        monthly_words_count = len(set(monthly_words))
        return monthly_words_count
