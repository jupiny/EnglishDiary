from django.core.files.base import ContentFile
from django.http.response import HttpResponse
from django.conf import settings
from django.contrib.auth import get_user_model
import datetime

from PIL import Image
from io import BytesIO
from wordcloud import WordCloud


def format_wordcloud_name(username):
    wordcloud_name = settings.IMAGE_FILENAME_FORMAT.format(
        username=username,
        datetime=datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S"),
    )
    return wordcloud_name


def set_wordcloud_image(words):

    if words:
        # WordCloud Option
        wc = WordCloud(
            background_color=settings.WORDCLOUD_BACKGROUND_COLOR,
            width=settings.WORDCLOUD_WIDTH,
            height=settings.WORDCLOUD_HEIGHT,
            max_words=settings.WORDCLOUD_MAX_WORDS,
            max_font_size=settings.WORDCLOUD_MAX_FRONT_SIZE,
            scale=settings.WORDCLOUD_SCALE,
        )
        wordcloud_img = wc.generate(words).to_image()
        return wordcloud_img
    return None


def save_wordcloud(user):
    whole_used_words = " ".join(user.whole_used_words())
    wordcloud_img = set_wordcloud_image(whole_used_words)

    if wordcloud_img:
        f = BytesIO()
        try:
            wordcloud_img.save(f, format='png')
            user.word_cloud.save(
                format_wordcloud_name(user.username),
                ContentFile(f.getvalue()),
            )
        finally:
            f.close()
    else:
        # If user has no words
        user.word_cloud = None
        user.save()
