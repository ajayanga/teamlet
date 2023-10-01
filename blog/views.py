from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

# Create your views here.
def home(request):
    return render(request, 'index.html')

def blogs(request):
    categorylist = Category.objects.all()
    bloglist = Blog.objects.filter(status='PB')
    pinnedblogs = bloglist.filter(pin='PI')

    categorydict = {}
    for category in categorylist:
        categorydict[category] = []
    for blog in bloglist:
        categorydict[blog.category].append(blog)
    print(categorydict)
    return render(request, 'blogs.html', {'blogs':bloglist[:4], 'categories' : categorydict, 'pinnedblogs':pinnedblogs})

def blog(request, pk):
    the_blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog.html', {'blog':the_blog})