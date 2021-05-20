from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from portalapp.models import Category, Article
# Create your views here.


class BaseView(View):

    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        articles = Article.objects.all()
        context = {
            'categories': categories,
            'articles': articles,
        }
        return render(request, self.template_name, context)


class CategoryDetailView(DetailView):

    model = Category
    template_name = 'category_articles.html'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['category_articles'] = Article.objects.filter(category=self.get_object())
        return context


class ArticleDetailView(DetailView):

    model = Article
    template_name = 'article_detail.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'
