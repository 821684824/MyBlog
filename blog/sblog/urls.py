from django.conf.urls import url

urlpatterns = [
	url(r'^bloglist/$','sblog.views.blog_list',name = 'bloglist'),
	url(r'^blog/(?P<id>\d+)/$','sblog.views.blog_show',name = 'detailblog'),
]