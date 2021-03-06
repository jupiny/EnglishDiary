import requests
from bs4 import BeautifulSoup

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class NaverDictionaryAPIView(APIView):

    def get(self, request, *args, **kwargs):

        naver_dict_url = "http://endic.naver.com/search.nhn?sLn=kr&searchOption=all&query="
        find_word = kwargs.get("find_word")

        response = requests.get(naver_dict_url+find_word)
        dom = BeautifulSoup(response.content, "html.parser")
        searched_word_element = dom.select_one(".fnt_e30") or None
        word_meaning_element = dom.select_one(".fnt_k05") or None
        searched_word = find_word
        word_meaning = ""
        if searched_word_element and searched_word_element.select_one('strong'):
            searched_word = searched_word_element.select_one('strong').text.strip()
            word_meaning = word_meaning_element.text
        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "searched_word": searched_word,
                "word_meaning": word_meaning,
            },
        )
