from django.urls import path
from portalapp.views import BaseView, CategoryDetailView, ArticleDetailView

app_name = 'portalapp'
urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('article/<slug:article_slug>', ArticleDetailView.as_view(), name='article_detail'),
    path('category/<slug:category_slug>', CategoryDetailView.as_view(), name='category_detail'),
]
