

from e_voting.settings.base import *
from dotenv import load_dotenv
import os

load_dotenv()


DEBUG = True

ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS")]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

