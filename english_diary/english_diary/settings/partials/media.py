import os

from .base import PROJECT_ROOT_DIR


MEDIA_ROOT = os.path.join(
    PROJECT_ROOT_DIR,
    "dist",
    "media",
)
MEDIA_URL = "/media/"

IMAGE_FILENAME_FORMAT = "img-wordcloud-{username}-{datetime}.png"
