from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name="blog"),
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name="post"),
]
