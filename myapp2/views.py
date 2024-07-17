from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
import logging

from .models import User, Product, Order


logger = logging.getLogger(__name__)


def index(request):
    logger.info('index page accessed')
    context = {'name': 'john'}
    return render(request, "myapp2/index.html", context)

def users_order(request, customer_id):
    user = get_object_or_404(User, pk=customer_id)
    today = timezone.now()
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)
    last_year = today - timedelta(days=365)
    
    products_week = Product.objects.filter(order__customer=user, date__gte=last_week).distinct().order_by('-date')
    products_month = Product.objects.filter(order__customer=user, date__gte=last_month).distinct().order_by('-date')
    products_year = Product.objects.filter(order__customer=user, date__gte=last_year).distinct().order_by('-date')
    
    return render(request, 'myapp2/list_order.html', {'user':user, 'products_week':products_week, 'products_month':products_month, 'products_year':products_year})
