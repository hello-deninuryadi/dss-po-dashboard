from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    doi = serializers.SerializerMethodField()
    recomendation = serializers.SerializerMethodField()
    
    class Meta :
        model = Item 
        fields = [
            'item_code',
            'item_name',
            'current_stock',
            'avg_monthly_sales',
            'doi',
            'recomendation',
        ]
        
    def get_doi (self, obj):
        return obj.calculate_doi()
    
    def get_recomendation(self, obj):
        return obj.dss_recomendation()