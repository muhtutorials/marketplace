from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Job
from accounts.models import Profile


class HomeView(ListView):
	model = Job
	template_name = 'jobs/home.html'


class JobDetailView(DetailView):
	model = Job
	template_name = 'jobs/job_detail.html'


class JobCreateView(CreateView):
	model = Job
	fields = ['title', 'description', 'budget']

	# set employer of the job
	def form_valid(self, form):
		form.instance.employer = self.request.user.profile
		return super().form_valid(form)


class AcceptView(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		job = get_object_or_404(Job, pk=self.kwargs['pk'])
		if not job.freelancer:
			profile = get_object_or_404(Profile, user=self.request.user)
			job.freelancer = profile
			job.save()
			messages.info(self.request, "Job has been accepted")
		return redirect(job.get_absolute_url())


class DeclineView(LoginRequiredMixin, UserPassesTestMixin, View):
	def get(self, *args, **kwargs):
		job = get_object_or_404(Job, pk=self.kwargs['pk'])
		job.freelancer = None
		job.is_done = False
		job.save()
		messages.error(self.request, "Job has been declined")
		return redirect(job.get_absolute_url())

	# check if user is the user who has taken the job
	def test_func(self):
		job = get_object_or_404(Job, pk=self.kwargs['pk'])
		return self.request.user.profile == job.freelancer


class DoneView(LoginRequiredMixin, UserPassesTestMixin, View):
	def get(self, *args, **kwargs):
		job = get_object_or_404(Job, pk=self.kwargs['pk'])
		job.is_done = True
		job.save()
		messages.success(self.request, "Job has been done")
		return redirect(job.get_absolute_url())

	# check if user is the user who has taken the job
	def test_func(self):
		job = get_object_or_404(Job, pk=self.kwargs['pk'])
		return self.request.user.profile == job.freelancer
