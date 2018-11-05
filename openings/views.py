from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Job
from django.db import models


def openings(request):
    context = {
        'jobs': Job.objects.all()
    }
    return render(request, 'openings/jobs.html', context)


class JobsListView(ListView):
    model = Job
    template_name = 'openings/jobs.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'jobs'
    ordering = ['deadline']
    paginate_by = 8


class WithinJobsListView(ListView):
    model = Job
    template_name = 'openings/jobs.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'within'
    ordering = ['deadline']
    paginate_by = 8

    def get_queryset(self):
        return Job.objects.filter(lab_choice="Within").order_by('deadline')


class OutsideJobsListView(ListView):
    model = Job
    template_name = 'openings/jobs.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'outside'
    ordering = ['deadline']
    paginate_by = 8

    def get_queryset(self):
        return Job.objects.filter(lab_choice="Outside").order_by('deadline')


class UserJobsListView(ListView):
    model = Job
    template_name = 'openings/user_jobs.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'jobs'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Job.objects.filter(uploaded_by=user).order_by('deadline')


class JobDetailView(DetailView):
    model = Job


class JobCreateView(LoginRequiredMixin, CreateView):
    template_name = 'openings/job_form.html'
    model = Job
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'openings/job_form.html'
    model = Job
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.uploaded_by:
            return True
        return False


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    success_url = '/'

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.uploaded_by:
            return True
        return False
