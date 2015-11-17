from django.shortcuts import get_object_or_404,render
from .models import Person,Course
from django.http import HttpResponseRedirect
import re
import datetime

weeks = ["Mon", "Tue", "Wed", "Thur", "Fri"]

def index(request):
	
	person_list = Person.objects.order_by('name')
	context = {'person_list':person_list}
	return render(request, 'students/index.html', context)

def LogginFailed(request):
	
	person_list = Person.objects.order_by('name')
	context = {'person_list':person_list,'login_failed':1}
	return render(request, 'students/index.html', context)
	

def indexLogginValid(request):
	account = request.POST['account']
	password = request.POST['password']


	for s in Person.objects.all():
		if s.account == account and s.password == password:
			return HttpResponseRedirect("/students/" +  str(s.id) + "/detail")
	return HttpResponseRedirect("/students/LogginFailed")

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

def registerValid(request):
	name = request.POST['name']
	account = request.POST['account']
	password = request.POST['password']
	

	for s in Person.objects.all():
		if s.account == account:
			return HttpResponseRedirect("/students/registerFailed/the$account$has$already$takens")

	if not re.match(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[!*#@+=$%(^)&])[A-Za-z\d!*#@+=$%(^)&]{6,}$',password):
		if len(password) < 6:
			error_message = ["your$password$should$at$least$have$6$characters"]
			msg = ""
		else:
			msg = "your$password$should$include$"
			error_message = []
			if not re.match(r'^.*[\d].*$',password): error_message.append("digits")
			if not re.match(r'^.*[a-z].*$',password): error_message.append("lowercase$characters")
			if not re.match(r'^.*[A-Z].*$',password): error_message.append("uppercase$characters")
			if not re.match(r'^.*[!*#@+=$%(^)&].*$',password): error_message.append("special$characters")
		return HttpResponseRedirect("/students/registerFailed/" + "{0}{1}".format(msg,',$'.join(error_message)))

	p = Person(name=name,account=account,password=password)
	p.save()
	return HttpResponseRedirect("/students")

def registerFailed(request, error_message):
	return render(request, 'students/register.html',{"error_message" : error_message.replace("$"," ")})

def courses(request, person_id):
	courses = Course.objects.all();
	return render(request, 'students/courses.html', {"person_id" : person_id, "courses" : courses})

def coursesFailed(request, person_id,error_message):
	courses = Course.objects.all();

	return render(request, 'students/courses.html', {"person_id" : person_id, "courses" : courses, 
													 "error_message": error_message.replace("$"," ")})

def chooseCourse(request, person_id):
	try:
		p = Person.objects.get(id=person_id)
	except (KeyError):
		return HttpResponseRedirect("/students")
	else:
		for k in request.POST.keys():
			if k.isnumeric():
				course = Course.objects.get(id=k)
				if course.max_number <= course.number:
					return HttpResponseRedirect("/students/" +  str(p.id) + "/courses/you$can$not$choose$course$" 
						+ course.course_name + "$as$it$reaches$its$maximum$num")
				if course not in p.course_set.all():
					p.course_set.add(course)
					course.number = course.number + 1
					course.save()
		now = datetime.datetime(2015, 11, 12, 13, 00)

		print weeks[now.weekday()] + " " + str(now.hour) + " " + str(now.minute)

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
    
