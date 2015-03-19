from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from time import gmtime, strftime

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

##class UserProfile(models.Model):
##    # This line is required. Links UserProfile to a User model instance.
##    user = models.OneToOneField(User)
##
##    # The additional attributes we wish to include.
##    email = models.CharField(unique=True)
##    name = models.CharField()
##    surname = models.CharField()
##    password = models.CharField()
##    picture = models.ImageField(upload_to='profile_images', blank=True)
##
##    # Override the __unicode__() method to return out something meaningful!
##    def __unicode__(self):
##        return self.user.username


class Note(models.Model):
    uploader = models.ForeignKey(User)
    note_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    module = models.CharField(max_length=128)
	
    date = models.DateField(strftime("%d/%m/%Y %H:%M", gmtime()))
    format = models.CharField(max_length=128)      # list of possible values
    def __unicode__(self):
        return self.title


class Rating(models.Model):
    rating_id = models.IntegerField(unique=True)
    note = models.ForeignKey(Note)
    stars = models.IntegerField()

    def __unicode__(self):
        return self.note
        
class Module(models.Model):
    ModuleSubject = models.CharField(max_length=128)
    moduleTitle = models.CharField(max_length=128)
    abb = models.CharField(max_length=128)
    def __unicode__(self):
        return self.modelTitle
        
class Subject(models.Model):
    subjectTitle = models.CharField(max_length=128)
    def __unicode__(self):
        return self.subjectTitle
