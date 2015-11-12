from django.conf.urls import url
from . import views
urlpatterns = [
    # ex: /polls/
	url(r'^$', views.index, name='index'),
	url(r'^logAgain/$', views.indexLogAgain, name='indexLogAgain'),
	url(r'^loggin/$', views.loggin, name='loggin'),
	url(r'^(?P<person_id>[0-9]+)/detail/$', views.detail, name='detail'),
	url(r'^register/$', views.register, name='register'),
	url(r'^createAccount/$', views.createAccound, name='createAccound'),
	url(r'^(?P<person_id>[0-9]+)/courses/$', views.courses, name='courses'),
	url(r'^(?P<person_id>[0-9]+)/chooseCourse/$', views.chooseCourse, name='chooseCourse'),
	url(r'^(?P<person_id>[0-9]+)/dropCourse/$', views.dropCourse),
	url(r'^deletePerson/$', views.deletePerson),
]
