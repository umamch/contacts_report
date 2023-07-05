from django.test import TestCase
from .models import Contacts
from csv_contacts import views
from django.test import RequestFactory


class ContactsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Setup test data for tests execution"""
        Contacts.objects.create(firstname='Durga',
                                lastname='Shiva',
                                street='Kailash',
                                zip='12345',
                                city='Srisail',
                                image='xyz/abc')

    def test_record_fetch_with_firstname(self):
        """Testing a record selection bases on first name of test data created using model Contacts"""
        record = Contacts.objects.get(firstname='Durga')
        self.assertEqual(record.firstname, 'Durga')


class ContactsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Setup Test data for view methods testing"""
        Contacts.objects.create(firstname='Durga',
                                lastname='Shiva',
                                street='Kailash',
                                zip='12345',
                                city='Srisail',
                                image='xyz/abc')

    def test_view_method_image_check(self):
        """Testing image check method under csv_contacts views"""
        record = Contacts.objects.get(firstname='Durga')
        check = views.check_image(record.image)
        self.assertFalse(check)

    def test_view_method_contact_list(self):
        """Testing view method contacts_list"""
        request = RequestFactory().get('/fake-path')
        records = views.contacts_list(request, 0)
        self.assertEqual(records.status_code, 200)

