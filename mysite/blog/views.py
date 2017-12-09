from django.shortcuts import render

# Create your views here.
from blog.models import Post


def post_list(request):
    posty=Post.objects.all()
    return render(request, 'post_list.html', {"posty":posty})