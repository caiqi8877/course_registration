from django.db import models


class Person(models.Model):
	
    name = models.CharField(max_length=200,blank=False)
    account = models.CharField(max_length=200,unique=True,blank=False)
    password = models.CharField(max_length=200,blank=False)

    def __str__(self):
    	return self.account

    class Meta:
        ordering = ('account',)

class Course(models.Model):

	course_name = models.CharField(max_length=200,unique=True,blank=False)
	persons = models.ManyToManyField(Person)
	max_number = models.IntegerField(default=0,blank=False)
	number = models.IntegerField(default=0,blank=False)
	# start_time = models.DateTimeField(blank=False)
	# end_time = models.DateTimeField(blank=False)

	def __str__(self):
		return self.course_name

	class Meta:
		ordering = ('course_name',)


# Course.persons.add(p)
# Person.course_set.add(c)		
