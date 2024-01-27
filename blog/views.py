from django.shortcuts import render
# from django.http import HttpResponse 

#from django.http import HttpResponse is used to import the HttpResponse class from Django's django.http module, allowing you to create and return HTTP responses in your Django views.

#from django.shortcuts import render is used to import the render function from Django's django.shortcuts module, making it easier to render HTML templates in Django views.

posts = [
    {
        'author' : 'karanth',
        'title' : 'bettada jeeva',
        'content' : 'novel',
        'date' : '18-07-1967',
    },
    {
        'author' : 'Tejaswi',
        'title' : 'Karvalo',
        'content' : 'novel',
        'date' : '18-07-1996', 
    }
]

updates = [
    {
        'version' : '2.89',
        'release' : '3.0 yet to come',
    },
    {
        'version' : '4.89',
        'release' : '5.0 yet to come', 
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context1 = {
        'updates' : updates,
    }
    return render(request, 'blog/about.html', context1)



#blog --> templates --> blog.html
