from django.apps import AppConfig


class DiaryAppConfig(AppConfig):
    name = "diaries"

    def ready(self):
        from diaries.signals.post_save import post_save_diary
