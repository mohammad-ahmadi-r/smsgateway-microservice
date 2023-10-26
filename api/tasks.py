from logic.sms_logic import SmsFactory
from celery import shared_task
from time import sleep


@shared_task
def send_sms(sender, receptor, text, provider):
    #to simulate async we use sleep here
    sleep(2)
    smsfactory = SmsFactory.create_sender(provider)
    smsfactory.send_sms(sender, receptor, text)