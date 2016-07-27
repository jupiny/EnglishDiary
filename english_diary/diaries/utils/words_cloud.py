from django.core.files.base import ContentFile
from django.http.response import HttpResponse
from django.conf import settings
from django.contrib.auth import get_user_model

from PIL import Image
from io import BytesIO
from wordcloud import WordCloud


def save_wordcloud(user_id):

    user = get_user_model().objects.get(pk=user_id)
    whole_used_words = " ".join(user.whole_used_words())
    wc = WordCloud(
        background_color="white", width=800, height=600,
        max_words=100, max_font_size=150, scale=0.8
    )
    if whole_used_words:
        wordcloud_img = wc.generate(whole_used_words).to_image()

        f = BytesIO()
        wordcloud_img_name = settings.IMAGE_FILENAME_FORMAT.format(
            username=user.username,
        )
        try:
            wordcloud_img.save(f, format='png')
            user.word_cloud.save(
                wordcloud_img_name,
                ContentFile(f.getvalue()),
            )
        finally:
            f.close()
    else:
        # If user has no words
        user.word_cloud = None
        user.save()
