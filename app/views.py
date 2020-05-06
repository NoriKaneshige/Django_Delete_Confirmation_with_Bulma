from django.urls import reverse_lazy
from .models import Post
from django.views import generic


class PostIndex(generic.ListView):
    model = Post

class PostDelete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('app:post_list')