from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name="index"),
    path('getmeeting/', views.getmeeting, name='meeting'),
    path('getmeetingminutes/', views.getmeetingminutes, name='meetingminutes'),
    path('getresource/', views.getresource, name='resource'),
    path('getevent/', views.getevent, name='event'),
    path('getmeetingdetail/<int:id>', views.getmeetingdetail, name='meetingdetail')
]