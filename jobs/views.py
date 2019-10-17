from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
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
		# allow the job to be taken by only one user
		if not job.freelancer:
			profile = get_object_or_404(Profile, user=self.request.user)
			job.freelancer = profile
			job.save()
			messages.info(self.request, "Job has been accepted")
		return redirect(job.get_absolute_url())


class DeclineView(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		job = get_object_or_404(Job, pk=self.kwargs['pk'])
		# allow only the user who has taken the job to decline it
		if self.request.user.profile == job.freelancer:
			job.freelancer = None
			job.is_done = False
			job.save()
			messages.error(self.request, "Job has been declined")
		return redirect(job.get_absolute_url())


class DoneView(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		job = get_object_or_404(Job, pk=self.kwargs['pk'])
		# allow only the user who has taken the job to mark it as done
		if self.request.user.profile == job.freelancer:
			job.is_done = True
			job.save()
			messages.success(self.request, "Job has been done")
		return redirect(job.get_absolute_url())
