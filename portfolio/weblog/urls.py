from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import category,category_list


urlpatterns = [
    path('category/', category,name ="category"),
    path('category/<slug:slug>', category_list,name ="category_list"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
