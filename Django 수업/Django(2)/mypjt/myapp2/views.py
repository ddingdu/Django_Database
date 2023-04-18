from django.shortcuts import render

# Create your views here.
def hello(request, name):

    context = {'name':name}

    return render(request, 'myapp2/hello.html', context)
