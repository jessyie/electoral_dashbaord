from django.urls import path
from . import views


urlpatterns = [
    path('', views.map, name='map'),
    path('update_charts/', views.update_charts, name='update_charts'),
    path('selectCensus', views.selectCensus, name='selectCensus'),
    
   
]