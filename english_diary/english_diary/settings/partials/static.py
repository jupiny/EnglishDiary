# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
import os

from .base import BASE_DIR
from .base import PROJECT_ROOT_DIR


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "english_diary", "static"),
]
STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "static")

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'english_diary': {
            'source_filenames': (
              'css/application.css',
              'css/datepicker.css',
              'css/heroic-features.css',
              'css/home.css',
              'css/mypage.css',
              'css/signin.css',
              'css/messages.css',
            ),
            'output_filename': 'css/english_diary.css',
        },
    },
    'JAVASCRIPT': {
        'english_diary': {
            'source_filenames': (
              'js/application.js',
              'js/messages.js',
              'js/google_analytics.js',
            ),
            'output_filename': 'js/english_diary.js',
        },
        'home': {
            'source_filenames': (
              'js/bootstrap-datepicker.js',
              'js/home.js',
            ),
            'output_filename': 'js/home.js',
        },
        'mypage': {
            'source_filenames': (
              'js/mypage.js',
            ),
            'output_filename': 'js/mypage.js',
        },
    }
}
