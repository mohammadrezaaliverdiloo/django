from django.shortcuts import render,HttpResponse
from .models import Category

def category(request):
    
    categories = Category.objects.all()
    
    context={
        'categories':categories
    }
    return render(request,'CategoryPage.html',context)


def category_list(request,slug):
    
    categories = Category.objects.filter(slug=slug)
    
    context={
        'categories':categories
    }
    return render(request,'CategoryList.html',context)