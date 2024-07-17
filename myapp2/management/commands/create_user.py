from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "create user"
    
    def handle(self, *args, **kwargs):
        user = User(
            name='John', email='john@mail.com', numder=72569834, address='City')
        user.save()
        self.stdout.write(f"{user}")