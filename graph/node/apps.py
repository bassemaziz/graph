
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "graph.node"
    verbose_name = _("Nodes")

    def ready(self):
        try:
            import graph.node.signals  # noqa F401
        except ImportError:
            pass
