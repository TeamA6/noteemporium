from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from time import gmtime, strftime, time
from datetime import datetime

def get_upload_file_name(instance, filename): # instance?
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'),filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


class Subject(models.Model):
    subjectTitle = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subjectTitle)
        super(Subject, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.subjectTitle

class Module(models.Model):
    sub = models.ForeignKey(Subject)
    moduleTitle = models.CharField(max_length=128)
    abb = models.CharField(max_length=128)

    def __unicode__(self):
        return self.moduleTitle


class Note(models.Model):
    uploader = models.ForeignKey(User)
    title = models.CharField(max_length=128,unique=True)
    slugTitle = models.SlugField()
    subject = models.CharField(max_length=128)
    reported = models.IntegerField(default=0)
    module = models.CharField(max_length=128)
    date = models.DateTimeField(default=datetime.now, blank=True)
    file = models.FileField(upload_to=get_upload_file_name)

    def __unicode__(self):
        return self.title

class Rating(models.Model):
    rating_id = models.IntegerField(unique=True)
    note = models.ForeignKey(Note)
    stars = models.IntegerField()

    def __unicode__(self):
        return self.note