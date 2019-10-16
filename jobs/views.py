from django.shortcuts import render
from django.views.generic import TemplateView

# from .models import Job


class HomeView(TemplateView):
	template_name = 'jobs/base.html'
