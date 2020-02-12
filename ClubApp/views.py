from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'ClubApp/index.html')
    
def getmeeting (request):
    meeting_list=Meeting.objects.all()
    return render(request, 'ClubApp/meeting.html', {'meeting_list' : meeting_list})

def getmeetingminutes (request):
    meetingminutes_list=MeetingMinutes.objects.all()
    return render(request, 'ClubApp/meetingminutes.html', {'meetingminutes_list' : meetingminutes_list})

def getresource (request):
    resource_list=Resource.objects.all()
    return render(request, 'ClubApp/resource.html', {'resource_list' : resource_list})

def getevent (request):
    event_list=Event.objects.all()
    return render(request, 'ClubApp/event.html', {'event_list' : event_list})