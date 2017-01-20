from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from comment.models import Comment

# Create your views here.
class CommentList(ListView):
    model = Comment
    ## Template name can also be put here as
    # template_name = 'comment/comment_list.html'

class CommentDetail(DetailView):
    model = Comment

class CommentCreate(CreateView):
    model = Comment
    fields = ['author', 'title', 'text']

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['author', 'title', 'text']

class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('comment_list')