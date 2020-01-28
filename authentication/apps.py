from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'authentication'
    verbose_name = _('appprofile')

    def ready(self):
        import authentication.signals
