from rest_framework.generics import ListAPIView
from .models import Item
from .serializers import ItemSerializer
from django.shortcuts import render

# Create your views here.
class ItemDSSListView(ListAPIView):
    queryset = Item.objects.filter(is_active = True)
    serializer_class = ItemSerializer