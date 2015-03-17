from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import time

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    email = models.CharField(unique=True)
	name = models.CharField()
	surname = models.CharField()
	password = models.CharField()
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Note(models.Model):
    user = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=128)
    note_id = (str(user) + str(title))
    subject = models.CharField(max_length=128)
	module = models.CharField(max_length=128)
	date = models.DateField(strftime("%d/%m/%Y %H:%M")
	format = models.CharField()							# list of possible values
    def __unicode__(self):
        return self.title


class Rating(models.Model):
    note = models.ForeignKey(Note)
    stars = models.IntegerField()

    def __unicode__(self):
        return self.note