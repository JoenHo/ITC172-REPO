from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .views import getmeeting, getmeetingminutes, getresource, getevent
from .forms import MeetingForm, MeetingMinutesForm, ResourceForm, EventForm
from django.urls import reverse
from django.contrib.auth.models import User

#==================
# Testing Models
#==================
class MeetingTest(TestCase):
    def setUp(self):
        test=Meeting(meetingtitle='Hello', meetinglocation='Earth', meetingagenda='Save the world!')
        return test 
    def test_string(self):
        test=self.setUp()
        self.assertEqual(str(test.meetingtitle), 'Hello')
        self.assertEqual(str(test.meetinglocation), 'Earth')
        self.assertEqual(str(test.meetingagenda), 'Save the world!')
    
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        test=meetingminutes=MeetingMinutes(meetingminutestext='Meeting!')
        return test
    def test_string(self):
        test=self.setUp()
        self.assertEqual(str(test.meetingminutestext), 'Meeting!')
    
    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingMinutes')

class ResourceTest(TestCase):
    def setUp(self):
        test=resource=Resource(resourcename='Github', resourcetype='url', resourceurl='http://www.github.com', resourcedescription='gethub url')
        return test
    def test_string(self):
        test=self.setUp()
        self.assertEqual(str(test.resourcename), 'Github')
        self.assertEqual(str(test.resourcetype), 'url')
        self.assertEqual(str(test.resourceurl), 'http://www.github.com')
        self.assertEqual(str(test.resourcedescription), 'gethub url')

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        test=Event(eventtitle='Party', eventlocation='VolunteerPark', eventdescription='have fun!')
        return test
    def test_string(self):
        test=self.setUp()
        self.assertEqual(str(test.eventtitle), 'Party')
        self.assertEqual(str(test.eventlocation), 'VolunteerPark')
        self.assertEqual(str(test.eventdescription), 'have fun!')

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

# ==================
# Testing Views
# ==================
class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
class GetMeetingTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('meeting'))
       self.assertEqual(response.status_code, 200)

class GetMeetingMinutesTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('meetingminutes'))
       self.assertEqual(response.status_code, 200)

class GetResourceTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('resource'))
       self.assertEqual(response.status_code, 200)

class GetEventTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('event'))
       self.assertEqual(response.status_code, 200)

class GetMeetingDetailTest(TestCase):
   def setUp(self):
       test=self.detail=Meeting.objects.create(meetingtitle='Hello', meetingdate='2020-02-12', meetingtime='18:00:00', meetinglocation='Earth', meetingagenda='Save the world!')
       return test
   def test_view_url_accessible_by_name(self):
       test=self.setUp()
       response = self.client.get(reverse('meetingdetail', args=(test.id,)))
       self.assertEqual(response.status_code, 200)

# ==================
# Testing Forms
# ==================
class Meeting_Form_Test(TestCase):
    def test_meetingform_is_valid(self):
        form=MeetingForm(data={'meetingtitle': "Hello", 'meetingdate': "2020-02-12", 'meetingtime': "18:00:00", 'meetinglocation': "Earth", 'meetingagenda': "Save the world!"})
        self.assertTrue(form.is_valid())

    def test_typeform_empty(self):
        form=MeetingForm(data={'meetingtitle': ""})
        self.assertFalse(form.is_valid())

class MeetingMinutes_Form_Test(TestCase):
    def test_meetingminutesform_is_valid(self):
        form=MeetingMinutesForm(data={'meetingid': 1, 'meetingminutestext': "Hi Hi"})
        self.assertTrue(form.is_valid())

    def test_typeform_empty(self):
        form=MeetingMinutesForm(data={'meetingminutestext': ""})
        self.assertFalse(form.is_valid())

class Resource_Form_Test(TestCase):
    def test_resourceform_is_valid(self):
        form=ResourceForm(data={'resourcename': "aaabbb", 'resourcetype': "url", 'resourceurl': "http://python", 'resourceuserid': "1", 'resourcedescription': "this is a link"})
        self.assertTrue(form.is_valid())

    def test_typeform_empty(self):
        form=ResourceForm(data={'resourcename': ""})
        self.assertFalse(form.is_valid())   

class Event_Form_Test(TestCase):
    def test_eventform_is_valid(self):
        form=EventForm(data={'eventtitle': "Hi", 'eventlocation': "scc", 'eventdate': "2020-02-14", 'eventtime': "18:00:00", 'eventdescription': "aaabbbccc"})
        self.assertTrue(form.is_valid())

    def test_typeform_empty(self):
        form=ResourceForm(data={'eventtitle': ""})
        self.assertFalse(form.is_valid())