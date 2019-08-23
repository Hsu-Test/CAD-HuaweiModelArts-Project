#from _future_ import unicode_literals
from django.db import models

from django.db import models

# Create your models here.

class Register(models.Model):
	username = models.TextField()
	password = models.TextField()
	email = models.TextField()
	childname = models.TextField()
	password_child = models.TextField()

class Login(models.Model):
	email = models.TextField()
	password = models.TextField()

class Search(models.Model):
	username = models.TextField()
	cid = models.TextField()
	date = models.DateField()
	time = models.TimeField()

class GetPlayLists(models.Model):
	username = models.TextField()
	cid = models.TextField()


# Create your models here.
class category(models.Model):
	categoryId = models.CharField(max_length=200, blank=True, null=False,primary_key=True)
	typeOfVoice  = models.CharField(max_length=200, blank=True, null=True)
	startDate  = models.DateTimeField(max_length=200, blank=True, null=True)
	endDate=models.DateTimeField(max_length=200, blank=True, null=True)
	userId = models.CharField(max_length=200, blank=False, null=False)
	class Meta:
		managed = False
		db_table = 'RecordCategory'        