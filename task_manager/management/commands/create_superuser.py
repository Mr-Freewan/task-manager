import os

from django.core.management.base import BaseCommand

from task_manager.apps.users.models import User

SUPERUSER_USERNAME = os.getenv('DJANGO_SUPERUSER_USERNAME')
SUPERUSER_PASSWORD = os.getenv('DJANGO_SUPERUSER_PASSWORD')
SUPERUSER_EMAIL = os.getenv('DJANGO_SUPERUSER_EMAIL')


class Command(BaseCommand):
    help = 'Automatically creates a superuser'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username=SUPERUSER_USERNAME).exists():
            User.objects.create_superuser(username=SUPERUSER_USERNAME,
                                          password=SUPERUSER_PASSWORD,
                                          email=SUPERUSER_EMAIL)
            self.stdout.write(
                self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))
