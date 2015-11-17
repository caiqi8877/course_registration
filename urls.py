from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
	url(r'^$', views.index, name='index'),
	url(r'^LogginFailed/$', views.LogginFailed, name='LogginFailed'),
	url(r'^indexLogginValid/$', views.indexLogginValid, name='indexLogginValid'),
	url(r'^(?P<person_id>[0-9]+)/detail/$', views.detail, name='detail'),
	url(r'^register/$', views.register, name='register'),
	url(r'^registerValid/$', views.registerValid, name='registerValid'),
	url(r'^registerFailed/(?P<error_message>[a-z$,\d]+)/$', views.registerFailed, name='registerFailed'),
	url(r'^(?P<person_id>[0-9]+)/courses/$', views.courses, name='courses'),
	url(r'^(?P<person_id>[0-9]+)/courses/(?P<error_message>[a-zA-Z$,\d]+)/$', views.coursesFailed, name='coursesFailed'),
	url(r'^(?P<person_id>[0-9]+)/chooseCourse/$', views.chooseCourse, name='chooseCourse'),
	url(r'^(?P<person_id>[0-9]+)/dropCourse/$', views.dropCourse),
	url(r'^deletePerson/$', views.deletePerson),
]
