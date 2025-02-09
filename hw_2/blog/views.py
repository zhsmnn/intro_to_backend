from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return JsonResponse(list(articles.values()), safe=False)

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return JsonResponse({
        'title': article.title,
        'text': article.text,
        'author': article.author,
    })