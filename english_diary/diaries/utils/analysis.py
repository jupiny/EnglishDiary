from django.http.response import HttpResponse

from diaries.models import Diary


def count_whole_words(request):

    whole_words = []
    for diary in Diary.objects.all():
        whole_words += diary.content.split()

    return HttpResponse(len(set(whole_words)))
