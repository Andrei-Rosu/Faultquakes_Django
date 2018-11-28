from django.urls import path
from .views import (MembersListView,
                    MemberDetailView,
                    MemberCreateView,
                    MemberUpdateView,
                    MemberDeleteView,
                    UserMembersListView,
                    )



urlpatterns = [
    path('members/', MembersListView.as_view(), name='members'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('members/new/', MemberCreateView.as_view(), name='member-create'),
    path('members/<int:pk>/update/', MemberUpdateView.as_view(), name='member-update'),
    path('members/<int:pk>/delete/', MemberDeleteView.as_view(), name='member-delete'),
    path('members/user/<str:username>', UserMembersListView.as_view(), name='user-members'),

]