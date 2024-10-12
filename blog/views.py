from django.shortcuts import render,get_object_or_404
from .models import Post


# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})



def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post, 
        status = Post.Status.PUBLISHED,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post,  # se utiliza el slug para encontrar el post correctamente en la base de datos.  # Este es un ejemplo de cómo se puede utilizar el slug en las urls.py. En realidad, debes usar un campo que sea único y único para cada post.  # Este es un ejemplo de cómo se puede utilizar el slug en las urls.py
        )
    return render(request, 'blog/post/detail.html', {'post': post})



