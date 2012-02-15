from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
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

    def email(self):
        return self.user.email
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


class School(models.Model):
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

class SchoolProfile(models.Model):
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

