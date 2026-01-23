from rest_framework import serializers
from .models import Item
from .models import DecisionOverride

class ItemSerializer(serializers.ModelSerializer):
    doi = serializers.SerializerMethodField()
    recomendation = serializers.SerializerMethodField()
    
    class Meta :
        model = Item 
        fields = [
            'id',
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
    


class DecisionOverrideSerializer(serializers.ModelSerializer):
    class Meta : 
        model = DecisionOverride
        fields = "__all__" 
        
        
class DecisionOverrideReadSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(source="item.item_code", read_only = True)
    
    class Meta : 
        model = DecisionOverride
        fields = [
            "id",
            "item_code",
            "override_value",
            "reason",
            "created_at",
        ]