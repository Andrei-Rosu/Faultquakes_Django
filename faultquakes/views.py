from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .models import Research
from .models import Geodesy
from .models import Modeling
from .models import Rock
from .models import Newswall
from django.db import models
from PIL import Image


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
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
    content = models.TextField
    image = models.ImageField(default='default.jpg', upload_to='publication_pics')
    fields = ['title', 'authors', 'content', 'journal', 'year', 'publisher', 'url', 'doi', 'team', 'image']

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
    fields = ['title', 'authors', 'content', 'journal', 'year', 'publisher', 'url', 'doi', 'team', 'image']

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
    template_name = 'faultquakes/home.html'
    queryset = User.objects.all()
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all().order_by('-date_posted')
        context['news'] = Newswall.objects.all().order_by('-date_posted')

        return context


def geodesy(request):
    context = {
        'geodesy': Geodesy.objects.all()
    }
    return render(request, 'faultquakes/home.html', context)


class GeodesyListView(ListView):
    model = Geodesy
    template_name = 'faultquakes/geodesy.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'geodesy'
    ordering = ['-date_posted']
    paginate_by = 4


class UserGeodesyListView(ListView):
    model = Geodesy
    template_name = 'faultquakes/user_geodesy.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'geodesy'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Geodesy.objects.filter(uploaded_by=user).order_by('-date_posted')


class GeodesyDetailView(DetailView):
    model = Geodesy


class GeodesyCreateView(LoginRequiredMixin, CreateView):
    model = Geodesy
    image = models.ImageField(default='default.jpg', upload_to='geodesy_pics')
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class GeodesyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Geodesy
    image = models.ImageField(default='default.jpg', upload_to='geodesy_pics')
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        geodesys = self.get_object()
        if self.request.user == geodesys.uploaded_by:
            return True
        return False


class GeodesyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Geodesy
    success_url = '/'

    def test_func(self):
        geodesys = self.get_object()
        if self.request.user == geodesys.uploaded_by:
            return True
        return False



def modeling(request):
    context = {
        'modeling': Modeling.objects.all()
    }
    return render(request, 'faultquakes/home.html', context)


class ModelingListView(ListView):
    model = Modeling
    template_name = 'faultquakes/modeling.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'modeling'
    ordering = ['-date_posted']
    paginate_by = 4


class UserModelingListView(ListView):
    model = Modeling
    template_name = 'faultquakes/user_modeling.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'modeling'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Modeling.objects.filter(uploaded_by=user).order_by('-date_posted')


class ModelingDetailView(DetailView):
    model = Modeling


class ModelingCreateView(LoginRequiredMixin, CreateView):
    model = Modeling
    image = models.ImageField(default='default.jpg', upload_to='modeling_pics')
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class ModelingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Modeling
    image = models.ImageField(default='default.jpg', upload_to='modeling_pics')
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        modelings = self.get_object()
        if self.request.user == modelings.uploaded_by:
            return True
        return False


class ModelingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Modeling
    success_url = '/'

    def test_func(self):
        modelings = self.get_object()
        if self.request.user == modelings.uploaded_by:
            return True
        return False


def rock(request):
    context = {
        'rock': Rock.objects.all()
    }
    return render(request, 'faultquakes/home.html', context)


class RockListView(ListView):
    model = Rock
    template_name = 'faultquakes/rock.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'rock'
    ordering = ['-date_posted']
    paginate_by = 4


class UserRockListView(ListView):
    model = Rock
    template_name = 'faultquakes/user_rock.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'rock'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Geodesy.objects.filter(uploaded_by=user).order_by('-date_posted')


class RockDetailView(DetailView):
    model = Rock


class RockCreateView(LoginRequiredMixin, CreateView):
    model = Rock
    image = models.ImageField(default='default.jpg', upload_to='rock_pics')
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class RockUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Rock
    image = models.ImageField(default='default.jpg', upload_to='rock_pics')
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        rocks = self.get_object()
        if self.request.user == rocks.uploaded_by:
            return True
        return False


class RockDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Rock
    success_url = '/'

    def test_func(self):
        rocks = self.get_object()
        if self.request.user == rocks.uploaded_by:
            return True
        return False


def news(request):
    context = {
        'news': Newswall.objects.all()
    }
    return render(request, 'faultquakes/home.html', context)


class NewswallListView(ListView):
    model = Newswall
    template_name = 'faultquakes/news.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'news'
    ordering = ['-date_posted']
    paginate_by = 8


class UserNewswallListView(ListView):
    model = Newswall
    template_name = 'faultquakes/user_news.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'news'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Newswall.objects.filter(uploaded_by=user).order_by('-date_posted')


class NewswallDetailView(DetailView):
    model = Newswall
    template_name = 'faultquakes/news_detail.html'
    context_object_name = 'news'


class NewswallCreateView(LoginRequiredMixin, CreateView):
    template_name = 'faultquakes/news_form.html'
    model = Newswall
    fields = ['title', 'content', 'image', 'video']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class NewswallUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'faultquakes/news_form.html'
    model = Newswall
    fields = ['title', 'content', 'image', 'video']

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






