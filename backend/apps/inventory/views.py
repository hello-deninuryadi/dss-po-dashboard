from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .models import DecisionOverride
from .serializers import DecisionOverrideSerializer
from .serializers import ItemSerializer
from .serializers import DecisionOverrideReadSerializer
# from django.shortcuts import render

# Create your views here.
class ItemDSSListView(ListAPIView):
    queryset = Item.objects.filter(is_active = True)
    serializer_class = ItemSerializer
    
class DecisionOverrideCreateView(APIView):
    def post(self, request):
        serializer = DecisionOverrideSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
class DecisionOverrideListView(APIView):
    def get(self, request, item_code = None):
        qs = DecisionOverride.objects.all().order_by("-created_at")
        
        if item_code :
            qs = qs.filter(item__item_code = item_code)
            
        serializer = DecisionOverrideReadSerializer(qs, many = True)
        return Response(serializer.data)