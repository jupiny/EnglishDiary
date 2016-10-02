from celery import Task

from core.utils.wordcloud import save_wordcloud


class SaveWordCloudTask(Task):

    def run(self, user_id):
        save_wordcloud(user_id)
