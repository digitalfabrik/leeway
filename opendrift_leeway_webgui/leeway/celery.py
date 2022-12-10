"""
Configure Celery workers
"""
import os
from imaplib import IMAP4_SSL
import email
from celery import Celery
from django.conf import settings

from .utils import mail_to_simulation

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opendrift_leeway_webgui.core.settings')
app = Celery('leeway')  # pylint: disable=invalid-name
app.config_from_object('django.conf:settings', namespace='CELERY')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):  # pylint: disable=unused-argument
    """
    Set up periodic tasks, i.e. retrieving mails from the mailbox
    """
    sender.add_periodic_task(60, check_mailbox.s(), name='check_mailbox')

@app.task
def check_mailbox():
    """
    Fetch mails from mailbox via IMAP and create new jobs
    """
    mailbox = IMAP4_SSL(host=settings.EMAIL_HOST)
    mailbox.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    mailbox.select('Inbox')
    typ, data = mailbox.search(None, 'UNSEEN')  # pylint: disable=unused-variable
    for num in data[0].split():
        typ, data = mailbox.fetch(num, '(RFC822)')
        mail_to_simulation(email.message_from_bytes(data[0][1]))
    mailbox.close()
    mailbox.logout()

app.autodiscover_tasks()
