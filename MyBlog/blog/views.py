from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.

def blog_title(request):
    blogs = models.BlogArticle.objects.all()
    return render(request, 'blog/titles.html',{'blogs': blogs})

def blog_details(request,article_id):
    article = get_object_or_404(models.BlogArticle,id=article_id)
    # article = models.BlogArticle.objects.get(id=article_id)
    return render(request, 'blog/content.html', {'article': article})