from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings 

from diaries.models import Diary


@receiver(post_save, sender=Diary)
def post_save_diary(sender, instance, created, **kwargs):
    if created:
        instance.word_count = len(instance.content.split())
        instance.formatted_created_at = instance.created_at.strftime(settings.DATETIME_FORMAT)
        instance.save()
