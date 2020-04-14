from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView,
  UpdateView, 
  DeleteView
)

from django.http import HttpResponse
from .models import Post



#function based views
def home(request):
  context = {
    'posts': Post.objects.all()
  }
  return render(request, 'blog/home.html', context)

class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
  context_object_name = 'posts'
  ordering = ['-date_posted'] # ['date_posted'] ordered the posts from oldest to newest
                              # minus sign reversed the process
  paginate_by = 5

class UserPostListView(ListView):
  model = Post
  template_name = 'blog/user_posts.html'
  context_object_name = 'posts'
  paginate_by = 5

  def get_queryset(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
  model = Post
  

class PostCreateView(LoginRequiredMixin,CreateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def text_func(self): #validate user
    post = self.get_object() #get the post
    if self.request.user==post.author:
      return True
    return False 

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def test_func(self): #validate user
    post = self.get_object() #get the post
    if self.request.user==post.author:
      return True
    return False 


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post
  success_url = '/'
  def test_func(self): #validate user
    post = self.get_object() #get the post
    if self.request.user==post.author:
      return True
    return False 

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

def shop(request):
  return render(request, 'blog/shop.html', {'title':'shop'})

def random_dialog(request):
  return render(request, 'blog/random_story.html', {'title':'story1'})