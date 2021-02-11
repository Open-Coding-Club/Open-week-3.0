from django.shortcuts import render
from .models import Comment

# Create your views here.
def comments(request):
    count = Comment.objects.all().count()
    comments = Comment.objects.all()
    return render(request, "comments.html", {
    'comments':comments,
    'count':count,
    })

def home(request):
    return render(request, "home.html", {})
