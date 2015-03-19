import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'noteemporium.settings')

import django
django.setup()

from note.models import Subject, Module

def populate():

    computer_science_sub = add_sub("Computer Science")

    add_module(sub=computer_science_sub, moduleTitle="Web App Development", abb="WAD")

    add_module(sub=computer_science_sub, moduleTitle="Java and Object-Oriented Programming",
                                               abb="JOOSE")

    add_module(sub=computer_science_sub, moduleTitle="Algorithms and Data Structures", abb="ADS")

    add_module(sub=computer_science_sub, moduleTitle="Algorithmic Foundations", abb="AF2")

    add_module(sub=computer_science_sub, moduleTitle="Computing Fundamentals 2", abb="CF2")

    for c in Subject.objects.all():
        for p in Module.objects.filter(sub=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_sub(subjectTitle):
    s = Subject.objects.get_or_create(subjectTitle=subjectTitle)[0]
    return s

def add_module(sub, moduleTitle, abb):
    m = Module.objects.get_or_create(sub=sub, moduleTitle=moduleTitle, abb=abb)
    return m

if __name__ == '__main__':
    print "Starting Note Emporium population script..."
    populate()
