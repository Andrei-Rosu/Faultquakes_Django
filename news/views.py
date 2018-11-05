from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Newswall
from django.db import models


def news(request):
    context = {
        'news': Newswall.objects.all()
    }
    return render(request, 'news/news.html', context)


class NewswallListView(ListView):
    model = Newswall
    template_name = 'news/news.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'news'
    ordering = ['-date_posted']
    paginate_by = 8


class UserNewswallListView(ListView):
    model = Newswall
    template_name = 'news/user_news.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'news'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Newswall.objects.filter(uploaded_by=user).order_by('-date_posted')


class NewswallDetailView(DetailView):
    model = Newswall
    template_name = 'news/news_detail.html'
    context_object_name = 'news'


class NewswallCreateView(LoginRequiredMixin, CreateView):
    template_name = 'news/news_form.html'
    model = Newswall
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class NewswallUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'news/news_form.html'
    model = Newswall
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.uploaded_by:
            return True
        return False


class NewswallDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Newswall
    success_url = '/'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.uploaded_by:
            return True
        return False


# Create your views here.
