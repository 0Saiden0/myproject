from django.urls import path
from .views import index, users_order


urlpatterns = [
    path('', index, name='index'),
    path('user/<int:customer_id>/', users_order, name='users_order')
]