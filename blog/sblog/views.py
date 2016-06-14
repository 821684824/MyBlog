from django.shortcuts import render
from sblog.models import Blog
from django.http import Http404
# Create your views here.
def blog_list(request):
	blogs = Blog.objects.all()
	return render(request,"blog_list.html",{"blogs":blogs})

def blog_show(request, id = ''):
	try:
		blog = Blog.objects.get(id = id)
	except Blog.DoesNotExist:
		raise Http404
	return render(request,'blog_show.html',{'blog':blog})