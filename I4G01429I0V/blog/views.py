from msilib.schema import Class
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.shortcuts import render
import blog

from blog.models import Post

# Create your views here.


Class PostListView(ListView):
    model = Post
    
Class PostCreateView(CreateView):
    model = Post
    fields = " all "
    success url = reserve lazy("blog:all")
    
Class PostDetailView(DetailView):
    model = Post
    
Class PostUpdateView(UpdateView):
    model = Post
    fields ="__all__"
    sucess_url = reserve_lazy('blog:all')


