from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def profile(request):
    info = {
        "name" : "jinju",
        "age" : 20
    }
    return render(request, 'myapp/profile.html', info)

def fruits(request):
    f_lst = ["apple", "banana", "melon"]
    context = {
        "fruits" : f_lst
    }
    return render(request, 'myapp/fruits.html', context)

def template(request):
    return render(request, 'myapp/template.html' )

