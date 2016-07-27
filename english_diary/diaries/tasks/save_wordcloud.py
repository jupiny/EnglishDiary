from celery import Task

from diaries.utils.words_cloud import save_wordcloud


class SaveWordCloudTask(Task):

    def run(self, user_id):
        save_wordcloud(user_id)
