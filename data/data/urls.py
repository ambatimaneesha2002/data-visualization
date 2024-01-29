
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('chartapp.urls')),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
]
