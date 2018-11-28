from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Member
from django.db import models


def members(request):
    context = {
        'members': Member.objects.all()
    }
    return render(request, 'members/members.html', context)


class MembersListView(ListView):
    model = Member
    template_name = 'members/members.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'members'
    ordering = ['name']
    paginate_by = 8

class UserMembersListView(ListView):
    model = Member
    template_name = 'members/user_members.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'members'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Member.objects.filter(uploaded_by=user).order_by('name')


class MemberDetailView(DetailView):
    model = Member


class MemberCreateView(LoginRequiredMixin, CreateView):
    template_name = 'members/member_form.html'
    model = Member
    fields = ['name', 'status', 'team', 'office', 'email', 'www', 'description', 'mobile']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class MemberUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'members/member_form.html'
    model = Member
    fields = ['name', 'status', 'team', 'office', 'email', 'www', 'description', 'mobile']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        member = self.get_object()
        if self.request.user == member.uploaded_by:
            return True
        return False


class MemberDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Member
    success_url = '/'

    def test_func(self):
        member = self.get_object()
        if self.request.user == member.uploaded_by:
            return True
        return False
