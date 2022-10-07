import os
import sys
import django

#
# Init
#
BASE_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))

#
# Define Django Env settings
#
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spambot.settings")
sys.path.insert(0, BASE_DIR)

#
# Initialize Django
#
django.setup()
