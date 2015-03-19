import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'noteemporium.settings')

import django
django.setup()

from note.models import Subject, Module

def populate():

    Computer_Science_sub = add_sub("Computer Science")

    add_module(sub=computer_science_sub, title="Web App Development", abb="WAD")

    add_module(sub=computer_science_sub, title="Java and Object-Oriented Programming",
                                               abb="JOOSE")

    add_module(sub=computer_science_sub, title="Algorithms and Data Structures", abb="ADS")

    add_module(sub=computer_science_sub, title="Algorithmic Foundations", abb="AF2")

    add_module(sub=computer_science_sub, title="Computing Fundamentals 2", abb="CF2")

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_sub(title):
    s = Subject.objects.get_or_create(name=name)[0]
    return s

def add_module(sub, title, abb):
    m = Module.objects.get_or_create(subject=sub, title=title, abbreviation=abb)
    return m

if __name__ == '__main__':
    print "Starting Note Emporium population script..."
        populate()