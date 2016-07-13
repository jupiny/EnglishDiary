from diary.models import Diary


def show_new_words(diary_old, diary_new):
    return set(diary_new.split()) - set(diary_old.split())


def main():
    diaries = Diary.objects.order_by("-id")
    new_words = show_new_words(diaries[0].content - diary[1].content)

    return new_words


# TODO : Model 에서 일기 가저오기
    # 3. model에서 request로 가져오고
