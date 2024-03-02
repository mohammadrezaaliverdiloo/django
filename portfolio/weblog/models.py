from django.db import models
import datetime

class Category (models.Model):
    
    title =models.CharField(null=False,max_length=255)
    slug = models.CharField(null=False,max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=False)
    
    
    def __str__(self):
        return self.title
    
    def __reper__(self):
        return self.title
        
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        
        
        
        
