from django.shortcuts import render
from django.views.generic import ListView

from .models import Job


class HomeView(ListView):
	model = Job
	template_name = 'jobs/home.html'
