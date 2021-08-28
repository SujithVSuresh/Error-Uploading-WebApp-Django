from django.shortcuts import redirect, render
from django.views import View
from .models import UserProfile
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

# Create your views here.
class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):

        profile = UserProfile.objects.get(pk=pk)
        followers = profile.followers.all()
        followers_count = followers.count()

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False    

        context = {
            'profile':profile,
            'followers_count':followers_count,
            'is_following':is_following
        }
        return render(request, 'userProfile/profile.html', context)

class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user)

        return redirect('user-profile', pk=profile.pk)

class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.remove(request.user)    

        return redirect('user-profile', pk=profile.pk)

            
