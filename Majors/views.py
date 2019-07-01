from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .models import Subject, Major
from django.http import Http404
from django.shortcuts import get_object_or_404

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def subjects_page(request):
	subjects = Subject.objects.all()
	context = {'subjects' : subjects}
	return render(request, 'Majors/majors.html', context)



def information_technology(request):
	subjects = Subject.objects.filter(major__name="Information Technology")
	context = {'subjects' : subjects}
	return render(request, 'Majors/information_technology.html', context)
#ptags = self.request.GET.get('ptags', None)
 #pub_date

#Subject.objects.filter(major__name="IT")

def business(request):
	subjects = Subject.objects.filter(major__name="Business")
	context = {'subjects' : subjects}
	return render(request, 'Majors/business.html', context)




def english_Literature(request):
	subjects = Subject.objects.filter(major__name="English Literature")
	context = {'subjects' : subjects}
	return render(request, 'Majors/english_Literature.html', context)



def general_studies(request):
	subjects = Subject.objects.filter(major__name="General Studies")
	context = {'subjects' : subjects}
	return render(request, 'Majors/general_studies.html', context)




def subject(request, subject_id):
	subjects = get_object_or_404( Subject,pk=subject_id)
	context = {'subjects':subjects}
	return render(request, 'Majors/subject.html', context)