from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import SmsSerializer
from .vo import SmsVO
from .models import Sms
from rest_framework.permissions import AllowAny, IsAdminUser
from kavenegar import *
from .tasks import send_sms

class SmsController(ViewSet):
    def send_sms(self, request: Request) -> Response:
        serializer = SmsSerializer(data=request.data)
        if serializer.is_valid():
            sender = serializer.validated_data.get(SmsVO.sender)
            receptor = serializer.validated_data.get(SmsVO.receptor)
            text = serializer.validated_data.get(SmsVO.text)
            provider = serializer.validated_data.get(SmsVO.provider) or "kavenegar"
            sms = Sms.objects.create(sender=sender, receptor=receptor, text=text)
            sms.save()
            send_sms.delay(sender, receptor, text, provider)
            print(provider)
            # print("async transaction and sms sent")
            # try:
            #     api = KavenegarAPI('526B7441664E374B42456C39706F514179414C694E536366656F6C6954614768466E467636696A6D5175303D')
            #     params = { 
            #         'sender' : '1000689696', 
            #         'receptor': '09913236310', 
            #         'message' :'{str}',
            #     }
            #     response = api.sms_send(params)
            #     print(response)
            #     return Response(data=None, status=status.HTTP_201_CREATED)
            # except APIException as e: 
            #     print(e)
            # except HTTPException as e: 
            #     print(e)
            return Response(data=None, status=status.HTTP_201_CREATED)

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def sms_report(self, request: Request) -> Response:
        # serializer = SmsSerializer(data=request.data)
        # if serializer.is_valid():
        # start_date = serializer.validated_data.get(SmsVO.sender)
        # end_date = serializer.validated_data.get(SmsVO.receptor)
        # return Sms.objects.filter(date__range=(start_date, end_date))
        try:
            report = Sms.objects.all()
            serialized_response = SmsSerializer(report, many=True)
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