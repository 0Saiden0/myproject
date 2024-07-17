from django.core.management.base import BaseCommand
from myapp2.models import Order


class Command(BaseCommand):
    help = "update Order by id"
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='user ID')
        parser.add_argument('customer_id', type=int, help='user name')
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        c_id = kwargs.get('customer_id')
        order = Order.objects.filter(pk=pk).first()
        order.customer_id = c_id
        order.save()
        self.stdout.write(f"{order}")