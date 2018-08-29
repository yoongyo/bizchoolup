from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^$', views.category_list, name='category_list'),
    url(r'^(?P<category>[\w|\W]+)/(?P<title>[\w|\W]+)/Edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<category>[\w|\W]+)/(?P<title>[\w|\W]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<category>[\w|\W]+)/$', views.post_list, name='post_list'),
    url(r'^new/$', views.post_new, name='post_new'),
]

