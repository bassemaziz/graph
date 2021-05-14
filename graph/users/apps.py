from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "graph.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import graph.users.signals  # noqa F401
        except ImportError:
            pass
