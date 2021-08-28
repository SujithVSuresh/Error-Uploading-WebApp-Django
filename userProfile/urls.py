from userProfile.views import ProfileView, AddFollower, RemoveFollower
from django.urls import path

urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='user-profile'),
    path('profile/<int:pk>/followers/add/', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove/', RemoveFollower.as_view(), name='remove-follower'),
]