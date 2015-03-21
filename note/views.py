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
#from myproject.myapp.models import Note
#from myproject.myapp.forms import DocumentForm
from models import Document
from forms import DocumentForm


def index(request):
    response = render(request, 'noteemp/index.html',)
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
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def list(request,module_abb,subject_name_slug):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('notes.views.list')) #is this right???
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'noteemp/notes.html',
        {'documents': documents, 'form': form,'module': module_abb, 'subject':subject_name_slug },
        context_instance=RequestContext(request)
    )

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
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'noteemp/login.html', {})

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

        modules = Module.objects.filter(sub=subject) # filter returns >= 1 model instance

        context_dict['modules'] = modules
        context_dict['subject'] = subject

    except Subject.DoesNotExist:
        pass
    # Go render the response and return it to the client.
    return render(request, 'noteemp/subject.html', context_dict)


def module(request,module_abb,subject_name_slug):
    context_dict = {}
    context_dict['module'] = module_abb
    #try:

    #except Subject.DoesNotExist:
     #   pass
    # Go render the response and return it to the client.
    return render(request, 'noteemp/notes.html', context_dict)




@login_required
def profile(request):
    u = User.objects.get(username=request.user.username)
    context_dict = {}
    try:
        up = UserProfile.objects.get(user=u)
    except:
        up = None
    context_dict['user'] = u
    context_dict['userprofile'] = up
    return render(request, 'noteemp/profile.html', context_dict)