from django.contrib import admin
from django.urls import path, include
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('api/', include('productapp.urls')),  # Include app-specific URLs
    
]



