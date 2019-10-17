from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('create/', views.JobCreateView.as_view(), name='job_create'),
    path('<int:pk>/accept/', views.AcceptView.as_view(), name='accept'),
    path('<int:pk>/decline/', views.DeclineView.as_view(), name='decline'),
    path('<int:pk>/done/', views.DoneView.as_view(), name='done'),
]
