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

class SmsListSerializer(serializers.ModelSerializer):
    sender = serializers.IntegerField()
    receptor = serializers.IntegerField()
    text = serializers.CharField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Sms
        fields = [SmsVO.sender, SmsVO.receptor, SmsVO.text, 'created_at']