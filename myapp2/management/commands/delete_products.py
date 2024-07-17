from django.core.management.base import BaseCommand
from myapp2.models import Product


class Command(BaseCommand):
    help = "constant specified number of products"
    
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='user ID')
    
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        i = 1
        while i <= count:
            product = Product.objects.filter(pk=i).first()
            if product is not None:
                product.delete()
            self.stdout.write(f"{product}")
            i += 1