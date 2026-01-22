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
        
        if doi is None :
            return "No Data"
        
        if doi < 30:
            return "Layak PO"
        elif 30 <= doi <= 60:
            return "Monitor"
        else:
            return "TUNDA PO"
    
    
    
    
    def __str__(self):
        return f"{self.item_code} - {self.item_name}"