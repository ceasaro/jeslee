from django.contrib.sites.models import SiteManager
from django.template import TemplateDoesNotExist
from django.test import SimpleTestCase
from django.core import mail
from django.test.utils import override_settings
from jeslee_web.utils.email import send_email
from mock import patch
__author__ = 'ceasaro'


class SimpleTest(SimpleTestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class EmailTest(SimpleTestCase):

    def setUp(self):
        mail.outbox = []
        super(EmailTest, self).setUp()

    @patch.object(SiteManager, 'get_current', return_value='mock.jeslee.com')
    def test_send_email_with_context(self, mock_site_manager):
        send_email(email_template_name='unittest/mail/email-with-context',
                   recipient_list=['to@example.com'],
                   context_dict={'context_var_1':'value_1', 'context_var_2':'value_2'})
        self.assertEquals(len(mail.outbox), 2)
        self.assertEquals(mail.outbox[0].subject, 'Test email with context value_1')
        self.assertEquals(mail.outbox[0].body, 'Message with context value_2\nDomain is: mock.jeslee.com')
        self.assertEquals(mail.outbox[0].from_email, 'info@jeslee.com')
        self.assertTrue('to@example.com' in mail.outbox[0].to,msg='to@example.com should be in the recipients list')

    @patch.object(SiteManager, 'get_current', return_value='mock.jeslee.com')
    def test_send_email(self, mock_site_manager):
        send_email(email_template_name='email/fashion_show/registration', subject='Subject here',
                   from_email='from@example.com', recipient_list=['to@example.com'])
        self.assertEquals(len(mail.outbox), 2)
        self.assertEquals(mail.outbox[0].subject, 'Subject here')

    @patch.object(SiteManager, 'get_current', return_value='mock.jeslee.com')
    def test_send_email_no_subject(self, mock_site_manager):
        try:
            # no subject file
            send_email(email_template_name='unittest/mail/no-subject-file',
                       from_email='from@example.com', recipient_list=['to@example.com'])
            self.assertFalse(False, msg="A template TemplateDoesNotExist expected")
        except TemplateDoesNotExist:
            self.assertEquals(len(mail.outbox), 0)
        send_email(email_template_name='unittest/mail/no-subject',
                   from_email='from@example.com', recipient_list=['to@example.com'])

    @patch.object(SiteManager, 'get_current', return_value='mock.jeslee.com')
    def test_send_no_email(self, mock_site_manager):
        send_email(subject='Subject here', from_email='from@example.com', recipient_list=['to@example.com'])
        self.assertEquals(len(mail.outbox), 0)

    def tearDown(self):
        mail.outbox = []
        super(EmailTest, self).tearDown()

