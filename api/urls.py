from django.urls import path
from .views import SmsController

urlpatterns = [
    path('', SmsController.as_view({'post': 'send_sms', 'get': 'sms_report'}), name='smscontroller'),                                                        
]