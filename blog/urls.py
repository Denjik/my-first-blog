from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url('drafts/', views.post_draft_list, name='post_draft_list'),
	url('post/<pk>/publish/', views.post_publish, name='post_publish'),
	url('post/<pk>/remove/', views.post_remove, name='post_remove'),
	url('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
	url('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    url('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]