from django.http.response import HttpResponse

from diaries.models import Diary


def count_whole_words(request):

    whole_words = []
    for diary in request.user.diary_set.all():
        whole_words += diary.content.split()

    return HttpResponse(set(whole_words))
