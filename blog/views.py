from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.views.generic import TemplateView


class Postlist(TemplateView):
     def get(self, request, *args, **kwargs):
         return render(request, 'blog/post_list.html', context=None)
class Aboutme(TemplateView):
    template_name = "blog/about.html"
class MyBlog(TemplateView):
    template_name = "blog/blog.html"
