from typing import Optional
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from  django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name='posts' # by default is uses objectlist variabel
    ordering = ['-date_posted']
    paginate_by = 2 # number of posts need to display on a page.

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
   

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    #success_url= reverse_lazy('blog-home') # if we need to redirect to the home page
    def form_valid(self, form):
        form.instance.author = self.request.user # form you are tring to submit ,take that instance and set the author to the current logged in user.
        return super().form_valid(form) # validiating the form .


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    #success_url= reverse_lazy('blog-home') # if we need to redirect to the home page
    def form_valid(self, form):
        form.instance.author = self.request.user # form you are tring to submit ,take that instance and set the author to the current logged in user.
        return super().form_valid(form) # validiating the form . 
    # prevent tring to update other users..
    def test_func(self):
        post = self.get_object()
        if self.request.user ==  post.author:
            return True
        return False  


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user ==  post.author:
            return True
        return False  



def about(request):
    return render(request,'blog/about.html',{'title':'ABout'})