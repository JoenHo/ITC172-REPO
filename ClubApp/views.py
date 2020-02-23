from django.shortcuts import *
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, MeetingMinutesForm, ResourceForm, EventForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index (request):
    return render(request, 'ClubApp/index.html')

@login_required    
def getmeeting (request):
    meeting_list=Meeting.objects.all()
    return render(request, 'ClubApp/meeting.html', {'meeting_list' : meeting_list})

@login_required
def getmeetingminutes (request):
    meetingminutes_list=MeetingMinutes.objects.all()
    return render(request, 'ClubApp/meetingminutes.html', {'meetingminutes_list' : meetingminutes_list})

@login_required
def getresource (request):
    resource_list=Resource.objects.all()
    return render(request, 'ClubApp/resource.html', {'resource_list' : resource_list})

@login_required
def getevent (request):
    event_list=Event.objects.all()
    return render(request, 'ClubApp/event.html', {'event_list' : event_list})

@login_required
def getmeetingdetail (request, id):
    meetingdetail=get_object_or_404(Meeting, pk=id)
    return render(request, 'ClubApp/meetingdetail.html', {'meetingdetail' : meetingdetail})

@login_required
def newMeeting(request):
     form=MeetingForm
     if request.method=='POST':
          form=MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
     else:
          form=MeetingForm()
     return render(request, 'ClubApp/newMeeting.html', {'form': form})

@login_required
def newMeetingMinutes(request):
     form=MeetingMinutesForm
     if request.method=='POST':
          form=MeetingMinutesForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingMinutesForm()
     else:
          form=MeetingMinutesForm()
     return render(request, 'ClubApp/newMeetingMinutes.html', {'form': form})

@login_required
def newResource(request):
     form=ResourceForm
     if request.method=='POST':
          form=ResourceForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ResourceForm()
     else:
          form=ResourceForm()
     return render(request, 'ClubApp/newResource.html', {'form': form})

@login_required
def newEvent(request):
     form=EventForm
     if request.method=='POST':
          form=EventForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=EventForm()
     else:
          form=EventForm()
     return render(request, 'ClubApp/newEvent.html', {'form': form})

def loginmessage(request):
    return render(request, 'ClubApp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'ClubApp/logoutmessage.html')

