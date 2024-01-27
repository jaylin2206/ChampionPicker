from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core.management import call_command


class PartypesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'partypes'

    def ready(self):
        post_migrate.connect(self.loadData, sender=self)

    def loadData(self, sender, **kwargs):
        call_command('loaddata', 'partypes/partypes.json')
