from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyPetstagramProject.accounts'

    def ready(self):
        import MyPetstagramProject.accounts.signals
        result = super().ready()
        return result
