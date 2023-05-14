from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse
from .models import Article
from .forms import ArticleForm


# Create your views here.
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    # def form_valid(self, form):
    #     return super().form_valid(form)


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    # queryset = Article.objects.all()

    def get_object(self, queryset=None):
        pk = self.kwargs.get('id')
        return get_object_or_404(Article, id=pk)


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    def get_object(self):
        pk = self.kwargs.get('id')
        return get_object_or_404(Article, id=pk)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('id')
        return get_object_or_404(Article, id=pk)

    def get_success_url(self):
        return reverse('blog:article_list')