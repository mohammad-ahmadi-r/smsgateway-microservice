from rest_framework import serializers
from . models import Sms
from .vo import SmsVO

class SmsSerializer(serializers.ModelSerializer):
    sender = serializers.IntegerField(required=False)
    receptor = serializers.IntegerField()
    text = serializers.CharField()
    provider = serializers.CharField(required=False)

    class Meta:
        model = Sms
        fields = [SmsVO.sender, SmsVO.receptor, SmsVO.text, SmsVO.provider]

# class SmsReportSerializer(serializers.Serializer):
#     start_date = mode
#     class Meta:
#         model = Sms
#         fields = ['start_date', 'end_date']