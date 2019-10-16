from django.db import models

from accounts.models import Profile


class Job(models.Model):
	employer = models.ForeignKey(Profile, on_delete=models.CASCADE)
	freelancer = models.OneToOneField(
		Profile, related_name='freelancer', blank=True, null=True, on_delete=models.SET_NULL
		)
	title = models.CharField(max_length=50)
	description = models.TextField()
	budget = models.PositiveIntegerField()
	is_done = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title
