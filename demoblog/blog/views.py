from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    """ 
    A view for blog's entry page 
    View url: /blog
    """
    template_name = 'blog/post_list.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 5

class PostDetailView(DetailView):
    """
    A view for a blog post
    View url: /blog/<post.id>
    """
    template_name = 'blog/post_detail.html'
    model = Post
    context_object_name = 'post'
    