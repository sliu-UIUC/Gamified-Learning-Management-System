from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self): #ready for signals
        import users.signals
