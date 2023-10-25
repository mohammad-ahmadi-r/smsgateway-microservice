class SmsFactory:
    @staticmethod
    def create_sender(provider):
        if provider == 'qasedak':
            return QasedakSmsSender()
        elif provider == 'kavenegar':
            return KavenegarSmsSender()
        else:
            raise ValueError('Unsupported provider')

class QasedakSmsSender:
    def send_sms(self, sender, receptor, text):
        print("this is mocking qasedak!")
        print("sent from {} to {}, context:{}".format(sender, receptor, text))
        pass

class KavenegarSmsSender:
    def send_sms(self, sender, receptor, text):
        print("this is in kavenegar")
        try:
            api = KavenegarAPI('526B7441664E374B42456C39706F514179414C694E536366656F6C6954614768466E467636696A6D5175303D')
            params = { 
                'sender' : '{sender}', 
                'receptor': '{receptor}', 
                'message' :'{str}',
            }
            response = api.sms_send(params)
            print(response)
            return Response(data=None, status=status.HTTP_201_CREATED)
        except APIException as e: 
            print(e)
            print(params)
        except HTTPException as e: 
            print(e)