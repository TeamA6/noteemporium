from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from time import gmtime, strftime


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


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
    sub = models.CharField(max_length=128)
    moduleTitle = models.CharField(max_length=128)
    abb = models.CharField(max_length=128)

    def __unicode__(self):
        return self.moduleTitle


class Subject(models.Model):
    subjectTitle = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subjectTitle)
        super(Subject, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.subjectTitle


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d') # maybe need unicode
