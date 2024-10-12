from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .models import Post
from .form import EmailForm

# Create your views here.


def post_list(request):
    post_list = Post.published.all()
    Paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
            posts  = Paginator.page(page_number)
    except PageNotAnInteger:
            posts = Paginator.page(1) 

    except EmptyPage:
            posts = Paginator.page(Paginator.num_pages)
                
    return render(request, 'blog/post/list.html', {'posts': posts})



def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post, 
        status = Post.Status.PUBLISHED,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post,  
        )
    return render(request, 'blog/post/detail.html', {'post': post})




def post_share(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED,
    )
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form})



class PostListView(ListView):
    """
    Alternative post list view
    """

    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

