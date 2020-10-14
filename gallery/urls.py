from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin

urlpatterns = [
    path('',views.home, name='home'),
    path('search/',views.search_results, name='search_results'),
    path('location/<location>',views.locate_image, name='locate_image'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)