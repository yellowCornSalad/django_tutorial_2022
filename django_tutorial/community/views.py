from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tutorial.views import OwnerOnlyMixin

from community.models import Article
from django.urls import reverse_lazy


class ArticleListView(ListView):
    model = Article
    template_name = 'community/list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'community/view_detail.html'

# ##### 인증없이 작성
# class WriteFormView(CreateView):
#   model = Article
#   fields = ['name', 'title', 'contents', 'url', 'email']
#   template_name = 'community/write.html'
#   success_url = reverse_lazy('community:article_list')

    # def form_valid(self, form):
    #   return super().form_valid(form)


# 인증 후 작성 코드
# 메모작성
class WriteFormView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['name', 'title', 'contents', 'url', 'email']
    template_name = 'community/write.html'
    success_url = reverse_lazy('community:article_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# 변경(login user 자료만 list_up)


class ArticleChangeView(LoginRequiredMixin, ListView):
    template_name = 'community/change_list.html'

    def get_queryset(self):
        return Article.objects.filter(owner=self.request.user)

# 메모 수정(Update)


class ArticleUpdateView(OwnerOnlyMixin, UpdateView):
    model = Article
    template_name = 'community/article_update.html'
    fields = ['name', 'title', 'contents', 'url', 'email']
    success_url = reverse_lazy('community:change_list')

# 메모 삭제(Delete)


class ArticleDeleteView(OwnerOnlyMixin, DeleteView):
    model = Article
    template_name = 'community/article_delete.html'
    success_url = reverse_lazy('community:change_list')
