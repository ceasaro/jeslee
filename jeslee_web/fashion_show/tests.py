"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime

from django.test import TestCase
from jeslee_web.fashion_show.models import FashionShow, FashionLocation


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class FashionShowTestCase(TestCase):

    def setUp(self):
        location_1 = FashionLocation.objects.create(name="location_1")
        location_2 = FashionLocation.objects.create(name="location_2")
        self.show1 = FashionShow.objects.create(start_time="2014-05-01 15:00:00", end_time="2014-05-01 17:00:00"
                                           , location=location_1)
        self.show2 = FashionShow.objects.create(start_time="2014-01-01 15:00:00", end_time="2014-01-01 17:00:00"
                                           , location=location_2)
        self.show3 = FashionShow.objects.create(start_time="2014-03-01 15:00:00", end_time="2014-03-01 17:00:00"
                                           , location=location_1)
        self.show4 = FashionShow.objects.create(start_time="2013-01-01 15:00:00", end_time="2013-01-01 17:00:00"
                                           , location=location_2)

    def test_get_upcoming_shows(self):
        upcoming_shows = FashionShow.objects.get_upcoming_shows(date_from=datetime(year=2014, month=1, day=1))
        self.assertEqual(3, upcoming_shows.count(), msg="3 upcoming shows expected")
        self.assertEquals(self.show2, upcoming_shows[0], msg="first show must be {} but found {}"
                          .format(self.show2, upcoming_shows[0]))
        self.assertEquals(self.show3, upcoming_shows[1], msg="first show must be {} but found {}"
                          .format(self.show3, upcoming_shows[0]))
        self.assertEquals(self.show1, upcoming_shows[2], msg="first show must be {} but found {}"
                          .format(self.show1, upcoming_shows[0]))

    def test_get_upcoming(self):
        upcoming_show = FashionShow.objects.get_upcoming_show(date_from=datetime(year=2014, month=1, day=1))
        self.assertEquals(self.show2, upcoming_show, msg="upcoming show must be {} but found {}"
                          .format(self.show2, upcoming_show))
