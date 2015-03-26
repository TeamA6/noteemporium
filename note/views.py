from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from note.forms import UserForm, UserProfileForm
from note.models import Module, Subject
from django.contrib.auth.models import User
# from myproject.myapp.models import Note
#from myproject.myapp.forms import DocumentForm
from models import *
from django.core.context_processors import csrf
from forms import NoteForm
from note.search import get_query

def index(request):
    response = render(request, 'noteemp/index.html', )
    return response


def register(request):
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'noteemp/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def view_notes(request, subject_name_slug,module_abb):

    args = {}
    args.update(csrf(request))
    args['notes'] = Note.objects.all()
    args['subject'] = subject_name_slug
    args['module'] = module_abb
    args['subjectTitle'] = Subject.objects.get(slug=subject_name_slug)

    args['moduleBool'] = False
    for note in args['notes']:
        if note.module == args['subjectTitle']:
            args['moduleBool'] = True


    args['moduleTitle'] = Module.objects.filter(sub=Subject.objects.all())#sub=args['subjectTitle'])

    #for sub in args['subjectTitle']:
    #   if sub.


    return render(request,'noteemp/viewNotes.html', args)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/note/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'noteemp/login.html', {})
    else:
        return render(request, 'noteemp/login.html', {})

def add_module(request, subject_name_slug):

    try:
        sub = Subject.objects.get(slug=subject_name_slug)
    except Subject.DoesNotExist:
                sub = None

    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            if sub:
                module = form.save(commit=False)
                module.sub = sub
                page.save()
                # probably better to use a redirect here.
                return HttpResponseRedirect('/note/')
        else:
            print form.errors
    else:
        form = ModuleForm()

    context_dict = {'form':form, 'subject': sub}

    return render(request, 'noteemp/add_module.html', context_dict)

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/note/')


def subject(request, subject_name_slug):
    context_dict = {}
    try:
        subject = Subject.objects.get(slug=subject_name_slug)
        context_dict['subject_name'] = subject.subjectTitle

        modules = Module.objects.filter(sub=subject)  # filter returns >= 1 model instance

        context_dict['modules'] = modules
        context_dict['subject'] = subject

    except Subject.DoesNotExist:
        pass
    # Go render the response and return it to the client.
    return render(request, 'noteemp/subject.html', context_dict)

'''
def module(request, module_abb, subject_name_slug):
    context_dict = {}
    context_dict['module'] = module_abb
    context_dict['subject'] = subject_name_slug
    #try:

    #except Subject.DoesNotExist:
    #   pass
    # Go render the response and return it to the client.
    return render(request, 'noteemp/addNote.html', context_dict)
'''

@login_required
def profile(request):
    u = User.objects.get(username=request.user.username)
    context_dict = {}
    try:
        up = UserProfile.objects.get(user=u)
        blah = Notes.objects.get(uploader=request.user).order_by('-date')[:5]
        print "defined blah as:" + blah
        context_dict['recent_notes'] = blah
    except:
        up = None
        context_dict['recent_notes'] = 'none'
    context_dict['user'] = u
    context_dict['userprofile'] = up
    context_dict['notes'] = Note.objects.all()
    return render(request, 'noteemp/profile.html', context_dict)

@login_required
def create(request, subject_name_slug, module_abb):

    try:
        sub = Subject.objects.get(slug=subject_name_slug)
        u = User.objects.get(username=request.user.username)
    except Subject.DoesNotExist:
        sub = None

    if request.POST:

        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
           if sub:
               page = form.save(commit=False)
               page.subject = sub
               page.module = module_abb
               page.uploader = request.user
               #page.date = models.DateTimeField(auto_now_add=True, blank=True)
               #page.date = datetime.datetime.now()
               page.save()
               #Note.subject = subject_name_slug
               # u = User.objects.get(username=request.user.username)
               # Note.module = module_abb # not really abb
               # form.save()
               return HttpResponseRedirect('/note/')  # should redirect to a success screen

    else:
        form = NoteForm()
    context_dict = {}
    context_dict.update(csrf(request))
    context_dict['subject'] = subject_name_slug
    context_dict['module'] = module_abb

    context_dict['form'] = form  # pass the form to the html

    return render(request, 'noteemp/addNote.html', context_dict)

def latest(request):
    context_dict = {}
    try:
        notes = Note.objects.order_by('-date')[:5]
        context_dict['notes'] = notes
    except:
        return("There are no notes yet.")

    return render(request, 'noteemp/latest.html', context_dict)

def search(request):
    query_string1 = ''
    query_string = ''
    context_dict = {}
    results=[]

    notes = None
    notes = Note.objects.all()
    context_dict['notes']=notes

    noteTitles=[]
    for i in notes:
        j = str(i.title).lower()
        noteTitles += [j]
    #context_dict['noteTitles'] = noteTitles

    foundNotes1 = None
    foundNotes=[]
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string1 = request.GET['q']
        
        if query_string1 == '':
            d = True
        
        for i in query_string1:
            if i != ' ':
                query_string+=i
                
        foundNotes1 = get_query(query_string)
        for i in foundNotes1:
            j = str(i)
            foundNotes += [j]

    for a in foundNotes:
        if a not in results:
            results+=[a]

    c = False
    if results:
        c = True
    if c:
        context_dict['haveRes']='have'

    if d:
        context_dict['start']='start'
    else:
        context_dict['noStart']='noStart'
        #context_dict['foundNotes']=foundNotes
        #context_dict['query_string']=query_string

    context_dict['results']=results

    #found_entries = Entry.objects.filter(entry_query).order_by('date')
    return render_to_response('noteemp/search.html',
                          context_dict,
                          context_instance=RequestContext(request))

def reported(request):
    context_dict = {}
    return render(request, 'noteemp/reported.html', context_dict)
