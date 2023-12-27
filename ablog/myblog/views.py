from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comment
from django.urls import reverse_lazy
# Create your views here.
#def home(request):
 #   return render(request,'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailViews(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddpostView(CreateView):
    model=Post
    template_name = 'add.html'
    fields = '__all__'

class AddcommentView(CreateView):
    model= Comment
    template_name = 'comment.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title' , 'body' ]

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')