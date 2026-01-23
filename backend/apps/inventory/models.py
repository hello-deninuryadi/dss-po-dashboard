from django.db import models

# Create your models here.

class Item(models.Model):
    item_code = models.CharField(max_length=50, unique=True)
    item_name  = models.CharField(max_length=255)
    
    category = models.CharField(max_length=100, blank=True)
    brand = models.CharField(max_length=100 , blank=True)
    
    current_stock  = models.IntegerField()
    avg_monthly_sales = models.IntegerField()
    
    lead_time_days  = models.IntegerField(default=0)
    
    is_active  = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at  = models.DateTimeField(auto_now=True)
    
    def calculate_doi (self):
        """
        DOI = stock / (monthly_sales / 30)
        """
        
        if self.avg_monthly_sales <= 0:
            return None
        daily_sales = self.avg_monthly_sales / 30
        
        return round(self.current_stock / daily_sales, 2)
    
    
    """
    Logic DSS
    """
    def dss_recomendation(self):
        doi = self.calculate_doi()
        
        
        base_low = 30
        base_high = 60
        
        buffer = self.lead_time_days * 1.5
        low_threshold = base_low + buffer
        high_threhold = base_high + buffer
        

        
        
        if doi is None :
            return "No Data"
        
        if doi < low_threshold:
            return "LAYAK PO"
        elif low_threshold <= doi <= high_threhold:
            return "MONITOR"
        else:
            return "TUNDA PO"
    
    
    
    
    def __str__(self):
        return f"{self.item_code} - {self.item_name}"


class DecisionOverride(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    override_value = models.CharField(max_length=20)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.item.item_code} - {self.override_value}"