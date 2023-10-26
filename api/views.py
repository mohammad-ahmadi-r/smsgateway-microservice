from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import SmsSerializer, SmsListSerializer
from .vo import SmsVO
from .models import Sms
from rest_framework.permissions import AllowAny, IsAdminUser
# from kavenegar import *
from .tasks import send_sms

class SmsController(ViewSet):
    def send_sms(self, request: Request) -> Response:
        serializer = SmsSerializer(data=request.data)
        if serializer.is_valid():
            sender = serializer.validated_data.get(SmsVO.sender, SmsVO.default_sender)
            receptor = serializer.validated_data.get(SmsVO.receptor)
            text = serializer.validated_data.get(SmsVO.text)
            provider = serializer.validated_data.get(SmsVO.provider, SmsVO.default_provider)

            Sms.objects.create(sender=sender, receptor=receptor, text=text).save()
            send_sms.delay(sender, receptor, text, provider)

            return Response(data=None, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def sms_report(self, request: Request) -> Response:
        try:
            report = Sms.objects.all()
            serialized_response = SmsListSerializer(report, many=True)
            return Response(data=serialized_response.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data = error, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action == "send_sms":
            permission_classes = [AllowAny]
        elif self.action == "sms_report":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]