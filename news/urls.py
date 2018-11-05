from django.urls import path
from .views import (NewswallListView,
                    NewswallDetailView,
                    NewswallCreateView,
                    NewswallUpdateView,
                    NewswallDeleteView,
                    UserNewswallListView,
                    )


urlpatterns = [
    path('news/', NewswallListView.as_view(), name='news'),
    path('news/<int:pk>/', NewswallDetailView.as_view(), name='news-detail'),
    path('news/new/', NewswallCreateView.as_view(), name='news-create'),
    path('news/<int:pk>/update/', NewswallUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete/', NewswallDeleteView.as_view(), name='news-delete'),
    path('news/user/<str:username>', UserNewswallListView.as_view(), name='user-news'),

]
