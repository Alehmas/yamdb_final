from api_yamdb import settings


class TestSettings:

    def test_settings(self):

        assert not settings.DEBUG, 'Check that DEBUG in Django settings is off'
        assert settings.DATABASES['default']['ENGINE'] == 'django.db.backends.postgresql', (
            'Check you are using postgresql database'
        )
