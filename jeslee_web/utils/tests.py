from django.template import TemplateDoesNotExist
from django.test import SimpleTestCase
from django.core import mail
from django.test.utils import override_settings
from jeslee_web.utils.email import send_email

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

    def test_send_email_with_context(self):
        send_email(email_template_name='unittest/mail/email-with-context',
                   recipient_list=['to@example.com'],
                   context_dict={'context_var_1':'value_1', 'context_var_2':'value_2'})
        self.assertEquals(len(mail.outbox), 2)
        self.assertEquals(mail.outbox[0].subject, 'Test email with context value_1')
        self.assertEquals(mail.outbox[0].body, 'Message with context\nvalue_2')
        self.assertEquals(mail.outbox[0].from_email, 'info@jeslee.com')
        self.assertTrue('to@example.com' in mail.outbox[0].to,msg='to@example.com should be in the recipients list')

    def test_send_email(self):
        send_email(email_template_name='email/fashion_show/registration', subject='Subject here',
                   from_email='from@example.com', recipient_list=['to@example.com'])
        self.assertEquals(len(mail.outbox), 2)
        self.assertEquals(mail.outbox[0].subject, 'Subject here')

    def test_send_email_no_subject(self):
        try:
            # no subject file
            send_email(email_template_name='unittest/mail/no-subject-file',
                       from_email='from@example.com', recipient_list=['to@example.com'])
            self.assertFalse(False, msg="A template TemplateDoesNotExist expected")
        except TemplateDoesNotExist:
            self.assertEquals(len(mail.outbox), 0)
        send_email(email_template_name='unittest/mail/no-subject',
                   from_email='from@example.com', recipient_list=['to@example.com'])



    def test_send_no_email(self):
        send_email(subject='Subject here', from_email='from@example.com', recipient_list=['to@example.com'])
        self.assertEquals(len(mail.outbox), 0)

    def tearDown(self):
        mail.outbox = []
        super(EmailTest, self).tearDown()

