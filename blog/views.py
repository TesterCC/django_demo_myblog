from django.shortcuts import render
from django.http import HttpResponse

from . import models
# Create your views here.
# def index(request):
#     return HttpResponse('Hello, Django World!')

# def index(request):
#     return render(request, 'blog/index.html', {'hello': 'Blog1 Page'})

# def index(request):
#     article = models.Article.objects.get(pk=1)
#     return render(request, 'blog/index.html', {'article': article})


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})
