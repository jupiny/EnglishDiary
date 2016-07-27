from django.apps import AppConfig


class DiaryAppConfig(AppConfig):
    name = "diaries"

    def ready(self):
        from diaries.signals.post_save import post_save_diary
        from diaries.signals.post_delete import post_delete_diary
