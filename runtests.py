import os
import sys

import django
from django.test.runner import DiscoverRunner

if __name__ == "__main__":
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.test_settings"
    django.setup()
    sys.exit(bool(DiscoverRunner(verbosity=1).run_tests(["tests"])))
