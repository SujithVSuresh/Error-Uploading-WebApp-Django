from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ErrorIndex.urls')),
    path('user-profile/', include('userProfile.urls')),
    path('social/', include('social.urls')),
    path('accounts/', include('allauth.urls')),
]
