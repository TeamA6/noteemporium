import re

from django.db.models import Q
from models import *

def get_query(query_string):
    found_notes = Note.objects.filter(title__contains=query_string)
    found_notes = list(found_notes)
    return found_notes

#def get_author(query_string):
#    found_authors = UserProfile.objects.filter(user__username__contains=query_string)
#    found_authors = list(found_authors)
#    return found_authors

def get_subject(query_string):
    found_subjects = Note.objects.filter(subject__contains=query_string)
    found_subjects = list(found_subjects)
    return found_subjects

def get_module(query_string):
    found_modules = Note.objects.filter(module__contains=query_string)
    found_modules = list(found_modules)
    return found_modules
