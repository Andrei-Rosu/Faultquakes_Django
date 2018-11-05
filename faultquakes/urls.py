from django.urls import path
from .views import (PostListView,
                    PublicationsListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    ResearchListView,
                    UserResearchListView,
                    ResearchDetailView,
                    ResearchCreateView,
                    ResearchUpdateView,
                    ResearchDeleteView,
                    MembersListView,
                    IndexView)
from . import views




urlpatterns = [
    path('', PostListView.as_view(), name='faultquakes-home'),
    path('user/members/', MembersListView.as_view(), name='members'),
    path('publications/', PublicationsListView.as_view(), name='publications'),
    path('research/', ResearchListView.as_view(), name='research'),
    path('research/user/<str:username>', UserResearchListView.as_view(), name='user-research'),
    path('research/<int:pk>/', ResearchDetailView.as_view(), name='research-detail'),
    path('research/new/', ResearchCreateView.as_view(), name='research-create'),
    path('research/<int:pk>/update/', ResearchUpdateView.as_view(), name='research-update'),
    path('research/<int:pk>/delete/', ResearchDeleteView.as_view(), name='research-delete'),
    path('post/user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('map/', views.map, name='faultquakes-map'),
    path('index/', IndexView.as_view(), name='faultquakes-index'),
]



# Class based views are looking for a view of the format:
# <app>/<model>_<viewtype>.html