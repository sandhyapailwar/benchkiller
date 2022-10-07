import os

ROOT_URLCONF = "spambot.urls"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = "/static/"


STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/attachment/"

MEDIA_ROOT = os.path.join(BASE_DIR, "attachment")
