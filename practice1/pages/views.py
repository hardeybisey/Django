from django.shortcuts import render
# from django.shortcuts import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def about_view(request, *args, **kwargs):
    my_context = {
        'myname': 'Idris Adebisi',
        'number': 7466556,
        'hobbies': ['coding', 'mathematics', 'machine learning']
    }
    return render(request, 'about.html', my_context)


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})
