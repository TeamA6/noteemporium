import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'noteemporium.settings')

import django
django.setup()

from note.models import Subject, Module

def populate():

    accounting_and_finance_sub = add_sub("Accounting and Finance")

    archaeology_sub = add_sub("Archaeology")

    biology_sub = add_sub("Biology")

    business_sub = add_sub("Business")

    celtic_studies_sub = add_sub("Celtic Studies")

    chemistry_sub = add_sub("Chemistry")

    classics_sub = add_sub("Classics")

    comparative_literature_sub = add_sub("Comparative Literature")

    computer_science_sub = add_sub("Computer Science")

    dentistry_sub = add_sub("Dentistry")

    economics_sub = add_sub("Economics")

    education_sub = add_sub("Education")

    english_language_sub = add_sub("English Language")

    english_literature_sub = add_sub("English Literature")

    film_and_television_sub = add_sub("Film and TV")

    french_sub = add_sub("French")

    geography_sub = add_sub("Geography")

    german_sub = add_sub("German")

    health_and_wellbeing_sub = add_sub("Health and Wellbeing")

    hispanic_studies_sub = add_sub("Hispanic studies")

    history_sub = add_sub("History")

    history_of_art_sub = add_sub("History of Art")

    immunology_sub = add_sub("Immunology")

    information_studies_sub = add_sub("Information Studies")

    italian_sub = add_sub("Italian")

    law_sub = add_sub("Law")

    life_sciences_sub = add_sub("Life Sciences")

    management_sub = add_sub("Management")

    mathematics_sub = add_sub("Mathematics")

    mechanical_engineering_sub = add_sub("Mechanical Engineering")

    medicine_sub = add_sub("Medicine")

    music_sub = add_sub("Music")

    neuroscience_sub = add_sub("Neuroscience")

    nursing_sub = add_sub("Nursing")

    philosophy_sub = add_sub("Philosophy")

    physics_sub = add_sub("Physics")

    politics_sub = add_sub("Politics")

    psychology_sub = add_sub("Psychology")

    russian_sub = add_sub("Russian")

    scottish_literature_sub = add_sub("Scottish Literature")

    sociology_sub = add_sub("Sociology")

    statistics_sub = add_sub("Statistics")

    theology_sub = add_sub("Theology")

    translation_sub = add_sub("Translation Studies")

    urban_sub = add_sub("Urban Studies")

    veterinary_sub = add_sub("Veterinary Studies")

    add_module(sub=computer_science_sub, moduleTitle="Web App Development", abb="WAD")

    add_module(sub=computer_science_sub, moduleTitle="Java and Object-Oriented Programming", abb="JOOSE")

    add_module(sub=computer_science_sub, moduleTitle="Algorithms and Data Structures", abb="ADS")

    add_module(sub=computer_science_sub, moduleTitle="Algorithmic Foundations", abb="AF2")

    add_module(sub=computer_science_sub, moduleTitle="Computing Fundamentals 2", abb="CF2")

    add_module(sub=computer_science_sub, moduleTitle="Programming", abb="1P")

    add_module(sub=computer_science_sub, moduleTitle="Computational Thinking", abb="1CT")

    add_module(sub=computer_science_sub, moduleTitle="Further Programming", abb="1PX")

    add_module(sub=computer_science_sub, moduleTitle="Information Management and Human Computer Interaction", abb="1Q")

    add_module(sub=computer_science_sub, moduleTitle="Systems", abb="1S")

    add_module(sub=computer_science_sub, moduleTitle="Introduction to Linux", abb="3L")

    add_module(sub=computer_science_sub, moduleTitle="Advanced Programming 3", abb="AP3")

    add_module(sub=computer_science_sub, moduleTitle="Algorithms 3", abb="3X")

    add_module(sub=computer_science_sub, moduleTitle="Database Systems 3", abb="DS3")

    add_module(sub=computer_science_sub, moduleTitle="Interactive Systems 3", abb="IS3")

    add_module(sub=computer_science_sub, moduleTitle="Networked Systems 3", abb="NS3")

    add_module(sub=computer_science_sub, moduleTitle="Operating Systems 3", abb="OS3")

    add_module(sub=computer_science_sub, moduleTitle="Professional Software Development 3", abb="PSD3")

    add_module(sub=computer_science_sub, moduleTitle="Programming Languages 3", abb="PL3")

    add_module(sub=french_sub, moduleTitle="French Language 1", abb="FL1")

    add_module(sub=french_sub, moduleTitle="French Language 2", abb="FL2")

    add_module(sub=french_sub, moduleTitle="French Culture 1", abb="FC1")

    add_module(sub=french_sub, moduleTitle="French Culture 2", abb="FC2")

    add_module(sub=mechanical_engineering_sub, moduleTitle="DYNAMICS 1", abb="DYN1")

    add_module(sub=mechanical_engineering_sub, moduleTitle="MECHANICAL DESIGN 1", abb="MECHDES1")

    add_module(sub=mechanical_engineering_sub, moduleTitle="MECHANICS OF SOLIDS AND STRUCTURES 4N", abb="MECHSOLSTR4N")

    add_module(sub=mathematics_sub, moduleTitle="2A: Multivariable Calculus", abb="2A")

    add_module(sub=mathematics_sub, moduleTitle="2B: Linear Algebra", abb="2B")

    add_module(sub=mathematics_sub, moduleTitle="2C: Applied Maths", abb="2C")

    add_module(sub=mathematics_sub, moduleTitle="2D: Applications of Linear Algebra and Multivariable Calculus", abb="2D")

    add_module(sub=mathematics_sub, moduleTitle="2E: Real Analysis", abb="2E")

    add_module(sub=mathematics_sub, moduleTitle="2F: Further Pure", abb="2F")

    add_module(sub=mathematics_sub, moduleTitle="2T: Discrete Mathematics", abb="2T")

    add_module(sub=mathematics_sub, moduleTitle="1R: Calculus", abb="1R")

    add_module(sub=mathematics_sub, moduleTitle="1S: Co-ordinate geometry", abb="1S")

    add_module(sub=mathematics_sub, moduleTitle="1X: Advanced Calculus", abb="1X")

    add_module(sub=mathematics_sub, moduleTitle="1Y: Advanced Geometry", abb="1Y")

    add_module(sub=mathematics_sub, moduleTitle="Maths 3E", abb="MATHS3E")

    add_module(sub=accounting_and_finance_sub, moduleTitle="Finance 1", abb="FIN1")

    add_module(sub=accounting_and_finance_sub, moduleTitle="Accounting 2", abb="ACC2")

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