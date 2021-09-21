import os
import django
from django.core.management import call_command

if __name__ == "__main__":
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.test_settings"
    django.setup()
    call_command("makemigrations", "user_email")
