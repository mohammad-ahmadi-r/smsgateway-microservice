from logic.sms_logic import SmsFactory

# def send_sms(sender, receptor, text, provider='Kavenegar'):
#     if provider == 'qasedak':
#         Qasedak.send_sms(sender, receptor, text)
#     else:
#         Kavenegar.send_sms(sender, receptor, text)

from celery import shared_task
from time import sleep


@shared_task
def send_sms(sender, receptor, text, provider='kavenegar'):
    sleep(8)
    sender = SmsFactory.create_sender(provider)
    sender.send_sms(sender, receptor, text)