from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length = 255, blank = True, null = True)
    mobile = models.CharField(max_length = 20, blank = True, null = True)

    def __unicode__(self):
        return self.name()

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email
    
class StudentProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length = 255, blank = True, null = True)
    mobile = models.CharField(max_length = 20, blank = True, null = True)

    def __unicode__(self):
        return self.email()

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

class Teacher(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length = 255, blank = True, null = True)
    mobile = models.CharField(max_length = 20, blank = True, null = True)

    def __unicode__(self):
        return self.email()

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email
class TeacherProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length = 255, blank = True, null = True)
    mobile = models.CharField(max_length = 20, blank = True, null = True)

    def __unicode__(self):
        return self.email()

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

class Parent(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length = 255, blank = True, null = True)
    mobile = models.CharField(max_length = 20, blank = True, null = True)

    def __unicode__(self):
        return self.email()

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name
class ParentProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length = 255, blank = True, null = True)
    mobile = models.CharField(max_length = 20, blank = True, null = True)

    def __unicode__(self):
        return self.email()

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

class Organization(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User)

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

class School(models.Model):    
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length = 255, blank = True, null = True)
    mobile = models.CharField(max_length = 20, blank = True, null = True)
    org = models.ForeignKey(Organization)
    

class City(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __unicode__(self):
        return self.name

    