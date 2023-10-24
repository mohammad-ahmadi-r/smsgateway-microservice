from django.test import TestCase
from .models import Sms
from django.urls import reverse

class SmsInstanceTest(TestCase):
    def test_sms_exsition(self):
        sender = '09913236310'
        receptor = '09390109951'
        text = 'hi there'
        provider = 'kavenegar'

        response = self.client.post(
            reverse('smscontroller'),
            data={
                'sender': sender,
                'receptor': receptor,
                'text':text,
                'provider': provider
            }
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Sms.objects.filter(sender=sender, receptor=receptor, text=text).exists())