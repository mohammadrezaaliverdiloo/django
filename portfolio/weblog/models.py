from django.db import models
import datetime

class Category (models.Model):
    
    title =models.CharField(null=False,max_length=255)
    slug = models.SlugField(unique=True,null=False,max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=False)
    comment = models.TextField()
    
    
    def __str__(self):
        return self.title
    
    def __reper__(self):
        return self.title
        
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        
class Author (models.Model):
    
    PERMISSION=(
        ('read','READ'),
        ('publish','PUBLISH')
        )
    
    name =models.CharField(null=False,max_length=255)
    slug = models.CharField(null=False,max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    about_author = models.TextField()
    permission = models.CharField(max_length =8,choices=PERMISSION )
    
    
    def __str__(self):
        return self.name
    
    def __reper__(self):
        return self.name
        
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        
        
              
class Article (models.Model):
    STATUS=(
        ('draft','DRAFT'),
        ('published','PUBLISHED'),
    )
    category = models.ForeignKey(Category,related_name='category', on_delete=models.CASCADE)
    category = models.ForeignKey(Author,related_name='author', on_delete=models.CASCADE)
    title =models.CharField(null=False,max_length=255)
    slug = models.CharField(null=False,max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=False)
    content = models.TextField()
    permission = models.CharField(max_length =9,choices=STATUS )
    
    
    def __str__(self):
        return self.title
    
    def __reper__(self):
        return self.title
        
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        
            
        
        
        
