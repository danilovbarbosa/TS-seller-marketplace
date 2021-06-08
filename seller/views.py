from django.shortcuts import render

# Create your views here.
def index(request):
    content = {}
    return render(request, 'seller/index.html', context=content)


def create(request):
    content = {}
    return render(request, 'seller/new_seller.html', context=content)