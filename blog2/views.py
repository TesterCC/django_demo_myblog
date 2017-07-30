from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def index(request):
#     return HttpResponse('Hello, Django World!')
def index(request):
    return render(request, 'blog2/index.html', {'hello': 'Blog2 Page'})
