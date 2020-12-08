from django.shortcuts import render
from django.http import HttpResponse


posts=[
    {
        'author':'friday',
        'title':'Test title',
        'content':'Test Content',
        'date_posted':'January 06, 2020'
    },
    {
        'author':'jarvis',
        'title':'Test title2',
        'content':'Test Content2',
        'date_posted':'January 08, 2020'
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html', {'title':'About'})