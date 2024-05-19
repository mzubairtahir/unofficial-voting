


from e_voting.settings.base import *
from dotenv import load_dotenv
import os

load_dotenv()

ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS")]


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),  # Set the host to your MySQL server (usually 'localhost' for local development)
    }
}

STATIC_ROOT  = BASE_DIR / "static_files"


