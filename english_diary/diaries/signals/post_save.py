from django.db.models.signals import post_save
from django.dispatch import receiver

from diaries.models import Diary

from diaries.tasks.save_wordcloud import SaveWordCloudTask


@receiver(post_save, sender=Diary)
def post_save_diary(sender, instance, created, update_fields, **kwargs):
    if created or 'content' in update_fields:
        task = SaveWordCloudTask()
        task.delay(instance.user.id)
