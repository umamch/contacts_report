from django.apps import AppConfig


class CsvContactsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'csv_contacts'

    def ready(self):
        """Function used for importing and starting CSV data job scheduler"""
        from jobs import updater
        updater.start()


