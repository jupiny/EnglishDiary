from django.db.models.signals import post_delete
from django.dispatch import receiver

from diaries.models import Diary
from diaries.tasks.save_wordcloud import SaveWordCloudTask


@receiver(post_delete, sender=Diary)
def post_delete_diary(sender, instance, **kwargs):
    task = SaveWordCloudTask()
    task.delay(instance.user.id)
