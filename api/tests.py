from django.test import TestCase, Client
from .models import Sms
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .serializers import SmsSerializer, SmsListSerializer

class CreateSmsTest(TestCase):
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

class ListSmsTest(APITestCase):
    client = Client()
    def setUp(self):
        Sms(sender='9123456789', receptor='9125436798', text= 'hi there').save()
        Sms(sender='9123478945', receptor='9125436248', text= 'how are you doing').save()
        
    def test_get_all_queryset(self):
        url = reverse('smscontroller')
        response = self.client.get(url)
        sms = Sms.objects.all()
        serializer = SmsListSerializer(sms, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)