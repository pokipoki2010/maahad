from django.urls import path, include, re_path
from django.contrib.auth import login, logout
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	
	path('it/<int:subject_id>/',views.subject, name='itsubjects'),
	path('business/<int:subject_id>/',views.subject, name='bsubjects'), 
	path('english/<int:subject_id>/',views.subject, name='esubjects'),  
	path('general/<int:subject_id>/',views.subject, name='gsubjects'),
    path('it/',views.information_technology, name='information_technology'),
    path('business/',views.business, name='business'),
    path('english/',views.english_Literature, name='english_Literature'),
    path('general/',views.general_studies, name='general_studies'),
 	path('', views.subjects_page, name='subjects'),
 	#path(r'^login/$', login, {'template_name': 'Majors/login.html'}),
 	#path(r'^logout/$', logout, {'template_name': 'Majors/logout.html'}),
 	path('accounts/login/', auth_views.LoginView.as_view(template_name='Majors/login.html'),name='login'),
 	path('accounts/logout/', auth_views.LogoutView.as_view(template_name='Majors/logout.html'),name='logout'),
]


#<int:subject_id>/'