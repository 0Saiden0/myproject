from django.core.management.base import BaseCommand
from myapp2.models import Product
import datetime


class Command(BaseCommand):
    help = "update product data by id"
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='user ID')
    
    def handle(self, *args, **kwargs):
        dat = datetime.date(2024, 4, 13)
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        product.date = dat
        product.save()
        self.stdout.write(f"{product}")