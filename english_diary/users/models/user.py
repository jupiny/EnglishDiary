from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db import models
from datetime import datetime
from users.storage import OverwriteStorage


# http://hjh5488.tistory.com/12
def user_directory_path(instance, filename):
    path = "images/{username}/{filename}".format(
        username=instance.username,
        filename=filename,
    )
    return path


class CustomUserManager(UserManager):

    def agree_email_notification(self):
        return self.filter(email_notification=True)

    def check_username(self, username):
        return self.filter(username=username).exists()

    def check_email(self, email):
        return self.filter(email=email).exists()


class User(AbstractUser):

    objects = CustomUserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    email_notification = models.BooleanField(
        default=True,
    )

    word_cloud = models.ImageField(
        blank=True,
        null=True,
        upload_to=user_directory_path,
        # storage=OverwriteStorage(),
    )

    is_verified = models.BooleanField(
        default=False,
    )

    @property
    def today_diary(self):
        today = datetime.now().strftime("%Y/%m/%d")
        return self.diary_set.get_or_none(datetime=today)

    def monthly_words(self, **kwargs):
        year = kwargs.get("year")
        month = kwargs.get("month")
        datetime = year+"/"+month+"/"
        diaries = self.diary_set.filter(datetime__contains=datetime)

        monthly_words = []
        for diary in diaries:
            monthly_words += diary.used_words
        return monthly_words

    def distinct_monthly_words(self, **kwargs):
        return set(self.monthly_words(**kwargs))

    def distinct_monthly_words_count(self, **kwargs):
        distinct_monthly_words = self.distinct_monthly_words(**kwargs)
        distinct_monthly_words_count = len(distinct_monthly_words)
        return distinct_monthly_words_count

    @property
    def whole_used_words(self):
        whole_used_words = []
        for diary in self.diary_set.all():
            whole_used_words += diary.used_words
        return whole_used_words

    @property
    def distinct_whole_used_words(self):
        return set(self.whole_used_words)

    @property
    def distinct_whole_used_words_count(self):
        return len(self.distinct_whole_used_words)
