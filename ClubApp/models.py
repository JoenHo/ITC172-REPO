from django.db import models
from django.contrib.auth.models import User


class Meeting(models.Model):
    meetingtitle = models.CharField(max_length=255)
    meetingdate = models.DateField()
    meetingtime = models.TimeField()
    meetinglocation = models.CharField(max_length=255, null=True, blank=True)
    meetingagenda = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class MeetingMinutes(models.Model):
    meetingid = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    meetingattendance = models.ManyToManyField(User)
    meetingminutestext = models.TextField()

    def __str__(self):
        return super().__str__()

    class Meta:
        db_table='meetingMinutes'
        verbose_name_plural='meetingsMinutes'

class Resource(models.Model):
    resourcename = models.CharField(max_length=255)
    resourcetype = models.CharField(max_length=255, null=True, blank=True)
    resourceurl = models.CharField(max_length=255, null=True, blank=True)
    recourcedateentered = models.DateField()
    resourceuserid = models.ForeignKey(User, on_delete=models.CASCADE)
    resourcedescription = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return super().__str__()

    class Meta:
        db_table='resource'
        verbose_name_plural='resource'

class Event(models.Model):
    eventtitle = models.CharField(max_length=255)
    eventlocation = models.CharField(max_length=255, null=True, blank=True)
    eventdate = models.DateField()
    eventtime = models.TimeField()
    eventdescription = models.CharField(max_length=255, null=True, blank=True)
    eventuser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()

    class Meta:
        db_table='event'
        verbose_name_plural='event'
