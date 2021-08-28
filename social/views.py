from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from ErrorIndex.models import ErrorListing

# Create your views here.
class SocialErrorListingView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        error_post = ErrorListing.objects.filter(mode='Public').order_by('-created_on')

        context = {
            'error_post':error_post

        }
        return render(request, 'social/social_error_listing.html', context)
