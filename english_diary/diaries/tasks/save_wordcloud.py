from django.contrib.auth import get_user_model

from celery import Task

from core.utils.wordcloud import save_wordcloud
from core.utils.s3 import delete_file_from_s3


class SaveWordCloudTask(Task):

    def run(self, user_id):
        user = get_user_model().objects.get(pk=user_id)
        prev_wordcloud_fiename = str(user.word_cloud)
        save_wordcloud(user)

        # Delete previous WordCloud file of user form AWS S3
        delete_file_from_s3(prev_wordcloud_fiename)
