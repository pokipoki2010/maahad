from django.db import models

# Create your models here.


class Major(models.Model):
	name = models.CharField(max_length=200 , unique=True)
	
	def __str__(self):
		return "{}".format(self.name)

class Subject(models.Model):
	major = models.ForeignKey(Major, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=200, unique=True)
	summaries = models.URLField(max_length=200, blank=True)
	mock_exams = models.URLField(max_length=200, blank=True)
	videos = models.URLField(max_length=200, blank=True)
	def __str__(self):
		return "{}".format(self.name)
