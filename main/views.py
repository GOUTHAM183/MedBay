from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
import speech_recognition as sr
from django.views.generic import (
    ListView,
    
    DetailView,
)
from django.urls import reverse_lazy,reverse
from django.contrib import messages

def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "main/home.html", context)

class PostListView(ListView):
    model = Post
    template_name = "main/home.html"
    context_object_name = "posts"
    ordering = ["date_posted"]
    paginate_by = 4

class PostDetailView(DetailView):
    model = Post