"""cmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from comment import views

urlpatterns = [
    url(r'^$', views.CommentList.as_view(), name='comment_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.CommentDetail.as_view(), name='comment_detail'),
    url(r'^create/$', views.CommentCreate.as_view(), name='comment_create'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.CommentUpdate.as_view(), name='comment_edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.CommentDelete.as_view(), name='comment_delete'),
    ## to set a specific template use
    # url(r'^$', views.CommentList.as_view(template_name="comment_list.html"),
]