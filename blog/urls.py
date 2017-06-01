from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Postlist.as_view()),
    url(r'^about/$', views.Aboutme.as_view()),
    url(r'^blog/$', views.MyBlog.as_view()),
]

