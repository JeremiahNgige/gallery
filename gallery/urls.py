from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('',views.search_results(), name='search_results'),
    path('',views.locate_image, name='locate_image')
    
]