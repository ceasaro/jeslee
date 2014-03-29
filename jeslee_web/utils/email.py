import logging
from django.conf import settings
from django.core.mail import send_mail
from django.template import Context, TemplateDoesNotExist
from django.template.loader import get_template

__author__ = 'ceasaro'

logger = logging.getLogger(__name__)


def send_email(email_template_name=None, subject=None, recipient_list=None, context_dict=None,
               from_email=settings.DEFAULT_FROM_EMAIL):
    """
    Sends out an email
    @email_template_name: string: the template name of the e-mail it looks for a email_template_name+'.txt' file for a
                          text version and e email_template_name+'.html' for a html version. If the '.txt' version
                          isn't found no text email is send and if no '.html' version is found no html email is send.
    @subject:             string: the subject of the email, if not specified it tries to look for a
                          email_template_name+'-subject.txt' file.
    @context_dict:        a dictionary passed to the context of the email template renderer
    @recipient_list:      list of string:each an email address. Each member of recipient_list will see the other
                          recipients in the "To:" field of the email message.
    @from_email:          string: this address is used a the sender address, defaults to settings.DEFAULT_FROM_EMAIL
    """
    print "from_email = {} ".format(from_email)
    if email_template_name:
        default_context_dict = {}
        if context_dict:
            context_dict.update(default_context_dict)
        else:
            context_dict = default_context_dict
        context = Context(context_dict)
        if not subject:
            subject_file = email_template_name + "-subject.txt"
            logger.info("looking for subject in {subject_file}".format(subject_file=subject_file))
            subject_template = get_template(subject_file)
            subject = subject_template.render(context)

        try:
            plaintext = get_template(email_template_name+".txt")

            text_message = plaintext.render(context)
        except TemplateDoesNotExist:
            text_message = None

        try:
            html_text = get_template(email_template_name+".html")
            html_message = html_text.render(context)
        except TemplateDoesNotExist:
            html_message = None

        if subject and (text_message or html_message):
            if text_message:
                send_mail(subject=subject, message=text_message, from_email=from_email, recipient_list=recipient_list)
            else:
                logger.info("no plaintext email send with subject '{subject}'.".format(subject=subject))
            if html_message:
                send_mail(subject=subject, message=html_message, from_email=from_email, recipient_list=recipient_list)
            else:
                logger.info("no html email send with subject '{subject}'.".format(subject=subject))
        else:
            logger.warn("can't send message without subject or message, "
                        "may be no email templates found for {template}".format(template=email_template_name))
