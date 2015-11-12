from django.shortcuts import get_object_or_404,render
from .models import Person,Course
from django.http import HttpResponseRedirect

def index(request):
	
	person_list = Person.objects.order_by('name')
	context = {'person_list':person_list}
	return render(request, 'students/index.html', context)

def indexLogAgain(request):
	
	person_list = Person.objects.order_by('name')
	context = {'person_list':person_list,'login_failed':1}
	return render(request, 'students/index.html', context)
	

def loggin(request):
	account = request.POST['account']
	password = request.POST['password']


	for s in Person.objects.all():
		if s.account == account and s.password == password:
			return HttpResponseRedirect("/students/" +  str(s.id) + "/detail")
	return HttpResponseRedirect("/students/logAgain")

def detail(request, person_id):
	try:
		p = Person.objects.get(id=person_id)
	except (KeyError):
		return HttpResponseRedirect("/students")
	else:	
		courses = p.course_set.all();
		return render(request, 'students/detail.html', {"courses": courses, "p_id": person_id, "name":p.name})

def register(request):
    return render(request, 'students/register.html')

def createAccound(request):
	s_name = request.POST['name']
	s_account = request.POST['account']
	s_password = request.POST['password']
	s = Person(name=s_name,account=s_account,password=s_password)
	s.save()
	return HttpResponseRedirect("/students")

def courses(request, person_id):

	courses = Course.objects.all();
	return render(request, 'students/courses.html', {"person_id" : person_id, "courses" : courses})

def chooseCourse(request, person_id):
	try:
		p = Person.objects.get(id=person_id)
	except (KeyError):
		return HttpResponseRedirect("/students")
	else:
		courses = Course.objects.all();
		for course in courses:
			if course.course_name in request.POST:
				if p.course_set.add(course):
					course.number = course.number + 1
					course.save()
		return HttpResponseRedirect("/students/" +  str(p.id) + "/detail")

def dropCourse(request, person_id):
	try:
		p = Person.objects.get(id=person_id)

	except (KeyError):
		return HttpResponseRedirect("/students")
	else:
		for c in p.course_set.all():
			if str(c.id) == request.POST['course']:
				p.course_set.remove(c)
				c.number -= 1
				c.save()
		courses = p.course_set.all()
		return HttpResponseRedirect("/students/" +  str(p.id) + "/detail")

def deletePerson(request):
	try:
		p = Person.objects.get(id=request.POST['pID'])
	except (KeyError):
		return HttpResponseRedirect("/students")
	else:
		p.delete()
	return HttpResponseRedirect("/students")
    
