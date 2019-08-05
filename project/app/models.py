from django.db import models

# Create your models here.

class Register(models.Model):
	username = models.TextField()
	password = models.TextField()
	email = models.TextField()
	childname = models.TextField()
	password_child = models.TextField()

class Login(models.Model):
	username = models.TextField()
	password = models.TextField()

class Search(models.Model):
	username = models.TextField()
	cid = models.TextField()
	date = models.DateField()
	time = models.TimeField()

class GetPlayLists(models.Model):
	username = models.TextField()
	cid = models.TextField()

