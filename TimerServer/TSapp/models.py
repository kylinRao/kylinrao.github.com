from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()
class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()
class TaskInfo(models.Model):
        userId = models.CharField(max_length=30)
        remindTime  = models.CharField(max_length=50)
        remindTitle = models.CharField(max_length=60)
        remindDetail = models.CharField(max_length=30)

	def __unicode__(self):
		return self.userId
	class Meta:
		ordering = ['userId']
