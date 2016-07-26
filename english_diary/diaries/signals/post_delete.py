from django.db.models.signals import post_delete
from django.dispatch import receiver

from diaries.models import Diary
from diaries.utils.words_cloud import save_wordcloud


@receiver(post_delete, sender=Diary)
def post_delete_diary(sender, instance, **kwargs):
    save_wordcloud(instance.user)
