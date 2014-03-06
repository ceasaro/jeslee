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
        FashionShow.objects.create(start_time="2014-05-01 15:00:00", end_time="2014-05-01 17:00:00", location=location_1)
        FashionShow.objects.create(start_time="2014-01-01 15:00:00", end_time="2014-01-01 17:00:00", location=location_2)
        FashionShow.objects.create(start_time="2014-03-01 15:00:00", end_time="2014-03-01 17:00:00", location=location_1)
        FashionShow.objects.create(start_time="2013-01-01 15:00:00", end_time="2013-01-01 17:00:00", location=location_2)

    def test_get_upcoming_shows(self):
        upcoming_shows = FashionShow.objects.get_upcoming_shows(date_from=datetime(year=2014, month=1, day=1))
        self.assertEqual(3,upcoming_shows.count())
