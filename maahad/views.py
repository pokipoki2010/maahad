from django.http import HttpResponse
from django.shortcuts import render
from Majors.models import Major, Subject

def homepage(request):
	majors = Major.objects.order_by('id')
	subjects = Subject.objects.all()
	context = {'majors': majors, 'subjects': subjects,}
	
	return render(request, 'homepage.html', context)




#def about(request):
    #return HttpResponse('about')
    #return render(request, 'about.html')    