from . views import ErrorDeleteView, ErrorDetailView, ErrorEditView, ErrorListingView, ErrorListingFormView, AddDislike, AddLike
from django.urls import path

urlpatterns = [
    path('', ErrorListingView.as_view(), name='error-listing'),
    path('error/<str:pk>/', ErrorDetailView.as_view(), name='error-detail'),
    path('error/upload/', ErrorListingFormView.as_view(), name='error-upload'),
    path('error/<str:pk>/like', AddLike.as_view(), name='add-like'),
    path('error/<str:pk>/dislike', AddDislike.as_view(), name='add-dislike'),
    path('error/edit/<str:pk>/', ErrorEditView.as_view(), name='error-edit'),
    path('error/delete/<str:pk>/', ErrorDeleteView.as_view(), name='error-delete'),
]