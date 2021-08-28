from django.urls import path
from .views import SocialErrorListingView

urlpatterns = [
    path('', SocialErrorListingView.as_view(), name='social-error-listing')
]