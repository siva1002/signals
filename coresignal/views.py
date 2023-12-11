from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def create_blog_post(request):
    # Your code to create a new blog post goes here
    # ... new changes

    # After creating the blog post, send the signal

    return HttpResponse("hI")
