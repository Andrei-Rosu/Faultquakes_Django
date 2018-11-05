from django.urls import path
from .views import (JobsListView,
                    JobDetailView,
                    JobCreateView,
                    JobUpdateView,
                    JobDeleteView,
                    UserJobsListView,
                    )



urlpatterns = [
    path('jobs/', JobsListView.as_view(), name='openings'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('jobs/new/', JobCreateView.as_view(), name='job-create'),
    path('jobs/<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('jobs/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
    path('jobs/user/<str:username>', UserJobsListView.as_view(), name='user-jobs'),

]
