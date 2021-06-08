from django.shortcuts import render

# Create your views here.
def index(request):
    content = {}
    return render(request, 'index.html', context=content)