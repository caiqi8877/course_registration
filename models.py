from django.db import models


class Person(models.Model):
	
    name = models.CharField(max_length=200,unique=True)
    account = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
    	return self.name

    class Meta:
        ordering = ('name',)

class Course(models.Model):

	course_name = models.CharField(max_length=200,unique=True)
	persons = models.ManyToManyField(Person)
	max_number = models.IntegerField(default=0)
	number = models.IntegerField(default=0)

	def __str__(self):
		return self.course_name

	class Meta:
		ordering = ('course_name',)


# Course.persons.add(p)
# Person.course_set.add(c)		
