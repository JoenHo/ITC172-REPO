from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name="index"),
    path('getmeeting/', views.getmeeting, name='meeting'),
    path('getmeetingminutes/', views.getmeetingminutes, name='meetingminutes'),
    path('getresource/', views.getresource, name='resource'),
    path('getevent/', views.getevent, name='event'),
    path('getmeetingdetail/<int:id>', views.getmeetingdetail, name='meetingdetail'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('newMeetingMinutes/', views.newMeetingMinutes, name='newmeetingminutes'),
    path('newResource/', views.newResource, name='newresource'),
    path('newEvent/', views.newEvent, name='newevent'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]