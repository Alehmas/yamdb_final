import os

from django.conf import settings


class TestRequirements:

    def test_requirements(self):
        try:
            with open(f'{os.path.join(settings.BASE_DIR, "requirements.txt")}', 'r') as f:
                requirements = f.read()
        except FileNotFoundError:
            assert False, 'Check that you have added the requirements.txt file'

        assert 'gunicorn' in requirements, 'Check that you have added gunicorn to requirements.txt'
        assert 'django' in requirements, 'Check you added django to requirements.txt'
        assert 'pytest-django' in requirements, 'Check that you have added pytest-django to requirements.txt'
