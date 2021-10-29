from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post,Scheme
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

class SchemeDetailView(DetailView):
    model = Scheme


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains=searched)
        
        schemes = Scheme.objects.filter(title__contains = searched)

        return render(request,'main/search.html',{'searched':searched,'posts':posts,'schemes':schemes})
    else:
        return render(request,'main/search.html',{})


def schemes(request):
    context = {"schemes": Scheme.objects.all()}
    return render(request, "main/schemes.html", context)


def speech_to_text(request):
    data = request.POST.get('record')
    

    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        output = " " + r.recognize_google(audio)
    except sr.UnknownValueError:
        output = "Could not understand audio"
    except sr.RequestError as e:
        output = "Could not request results; {0}".format(e)
    data =output

    return render(request,'main/base.html',{'data':data})
    
 