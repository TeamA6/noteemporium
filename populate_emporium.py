import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'noteemporium.settings')

import django
django.setup()

from note.models import Subject, Module

def populate():

    computer_science_sub = add_sub("Computer Science")

    french_sub = add_sub("French")

    mechanical_engineering_sub = add_sub("Mechanical Engineering")

    maths_sub = add_sub("Maths")

    finance_sub = add_sub("Finance")

    add_module(sub=computer_science_sub, moduleTitle="Web App Development", abb="WAD")

    add_module(sub=computer_science_sub, moduleTitle="Java and Object-Oriented Programming", abb="JOOSE")

    add_module(sub=computer_science_sub, moduleTitle="Algorithms and Data Structures", abb="ADS")

    add_module(sub=computer_science_sub, moduleTitle="Algorithmic Foundations", abb="AF2")

    add_module(sub=computer_science_sub, moduleTitle="Computing Fundamentals 2", abb="CF2")

    add_module(sub=french_sub, moduleTitle="French Language 1", abb="CF2")

    add_module(sub=french_sub, moduleTitle="French Language 2", abb="CF2")

    add_module(sub=french_sub, moduleTitle="French Culture 1", abb="CF2")

    add_module(sub=french_sub, moduleTitle="French Culture 2", abb="CF2")

    add_module(sub=mechanical_engineering_sub, moduleTitle="DYNAMICS 1", abb="DYN1")

    add_module(sub=mechanical_engineering_sub, moduleTitle="MECHANICAL DESIGN 1", abb="MECHDES1")

    add_module(sub=mechanical_engineering_sub, moduleTitle="MECHANICS OF SOLIDS AND STRUCTURES 4N", abb="MECHSOLSTR4N")

    add_module(sub=maths_sub, moduleTitle="Maths 2A", abb="MATHS2A")

    add_module(sub=maths_sub, moduleTitle="Maths 2B", abb="MATHS2B")

    add_module(sub=maths_sub, moduleTitle="Maths 1R", abb="MATHS1R")

    add_module(sub=maths_sub, moduleTitle="Maths 1S", abb="MATHS1S")

    add_module(sub=maths_sub, moduleTitle="Maths 3E", abb="MATHS3E")

    add_module(sub=finance_sub, moduleTitle="Finance 1", abb="FIN1")

    add_module(sub=finance_sub, moduleTitle="Accounting 2", abb="ACC2")

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