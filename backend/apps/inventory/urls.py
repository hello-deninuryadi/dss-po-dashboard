from django.urls import path
from .views import ItemDSSListView

urlpatterns = [
    path('items/', ItemDSSListView.as_view(), name='item-dss-list')
]