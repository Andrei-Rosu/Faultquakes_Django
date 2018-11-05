from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .models import Research
from django.db import models
from PIL import Image



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'faultquakes/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'faultquakes/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 8


class PublicationsListView(ListView):
    model = Post
    template_name = 'faultquakes/publications.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 8


class UserPostListView(ListView):
    model = Post
    template_name = 'faultquakes/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(uploaded_by=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    image = models.ImageField(default='default.jpg', upload_to='publication_pics')
    fields = ['title', 'authors', 'journal', 'year', 'publisher', 'url', 'doi', 'team', 'image']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    image = models.ImageField(default='default.jpg', upload_to='publication_pics')
    fields = ['title', 'authors', 'journal', 'year', 'publisher', 'url', 'doi', 'team', 'image']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.uploaded_by:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.uploaded_by:
            return True
        return False


def map(request):
    return render(request, 'faultquakes/map.html', {'title': 'map'})





def research(request):
    context = {
        'research': Research.objects.all()
    }
    return render(request, 'faultquakes/home.html', context)


class ResearchListView(ListView):
    model = Research
    template_name = 'faultquakes/research.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'research'
    ordering = ['-date_posted']
    paginate_by = 4


class UserResearchListView(ListView):
    model = Research
    template_name = 'faultquakes/user_research.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'research'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Research.objects.filter(uploaded_by=user).order_by('-date_posted')


class ResearchDetailView(DetailView):
    model = Research


class ResearchCreateView(LoginRequiredMixin, CreateView):
    model = Research
    image = models.ImageField(default='default.jpg', upload_to='research_pics')
    fields = ['title', 'authors', 'journal', 'year', 'publisher', 'url', 'doi', 'team', 'image']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class ResearchUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Research
    image = models.ImageField(default='default.jpg', upload_to='research_pics')
    fields = ['title', 'authors', 'journal', 'year', 'publisher', 'url', 'doi', 'team', 'image']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        researches = self.get_object()
        if self.request.user == researches.uploaded_by:
            return True
        return False


class ResearchDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Research
    success_url = '/'

    def test_func(self):
        research = self.get_object()
        if self.request.user == research.uploaded_by:
            return True
        return False


def members(request):
    context = {
        'members': User.objects.all()
    }
    return render(request, 'users/members.html', context)


class MembersListView(ListView):
        model = User
        template_name = 'users/members.html'  # <app>/<model>_<viewtype>.html
        context_object_name = 'members'
        paginate_by = 8


class IndexView(ListView):
    context_object_name = 'home_list'
    template_name = 'faultquakes/index.html'
    queryset = User.objects.all()
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all().order_by('-date_posted')
        context['research'] = Research.objects.all().order_by('-date_posted')

        return context

