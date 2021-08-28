from .models import ErrorListing
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.edit import FormView, UpdateView, DeleteView, CreateView
from .forms import ErrorListingForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db.models import Q
from userProfile.models import UserProfile
from django.http import HttpResponseRedirect
# Create your views here.

class ErrorListingView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        errors = ErrorListing.objects.filter(author=request.user).order_by('-created_on')

        query = self.request.GET.get('query')
        if not query:
            query = ''
        errors = errors.filter(
            Q(error_body__icontains=query)
        )

        context = {
            'errors':errors
        }

        return render(request, 'ErrorIndex/error_listing.html', context)   


class ErrorListingFormView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = ErrorListing 
    template_name = 'ErrorIndex/error_upload.html'    
    form_class = ErrorListingForm 
    success_message = 'New error has been posted successfully..'
    success_url = reverse_lazy('error-listing') 
    
    #this is how we should provide initial data for CreateView form
    def get_initial(self):
        return {'author': self.request.user}



class ErrorDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        errors = ErrorListing.objects.get(pk=pk)
        author_profile = UserProfile.objects.get(user_name=errors.author)

        context = {
            'errors':errors,
            'author_profile':author_profile,
        }

        return render(request, 'ErrorIndex/error_detail.html', context)    

class ErrorEditView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = ErrorListing
    template_name = 'ErrorIndex/error_edit.html'
    form_class = ErrorListingForm 
    success_message = "Your post has been updated successfully"

    def get_success_url(self):
        pk = self.kwargs['pk']   
        return reverse_lazy('error-detail', kwargs={'pk':pk})

class ErrorDeleteView(LoginRequiredMixin, DeleteView):
    model = ErrorListing
    template_name = 'ErrorIndex/error_delete.html'
    success_url = reverse_lazy('error-listing') 
    success_message = "Your post has been deleted successfully"
    
    #for displaying messages
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ErrorDeleteView, self).delete(request, *args, **kwargs)

class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        error = ErrorListing.objects.get(pk=pk) 

        is_dislike = False

        for dislike in error.dislike.all():
            if request.user == dislike:
                is_dislike = True
                break

        if is_dislike:
            error.dislike.remove(request.user)  

        is_like = False

        for like in error.like.all():
            if request.user == like:
                is_like = True
                break

        if not is_like:
            error.like.add(request.user)

        if is_like:
            error.like.remove(request.user)            
        
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class AddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        error = ErrorListing.objects.get(pk=pk)
        
        is_like = False

        for like in error.like.all():
            if request.user == like:
                is_like = True
                break

        if is_like:
            error.like.remove(request.user)   

        is_dislike = False

        for dislike in error.dislike.all():
            if request.user == dislike:
                is_dislike = True
                break

        if not is_dislike:
            error.dislike.add(request.user)

        if is_dislike:
            error.dislike.remove(request.user)       
        
        
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
          




