from sms_ir import SmsIr
from sms_gateway.settings import SMS_IR_API_KEY


class SmsFactory:
    @staticmethod
    def create_sender(provider):
        if provider == 'qasedak':
            return QasedakSmsSender()
        elif provider == 'smsir':
            return SmsIRSmsSender()
        else:
            raise ValueError('Unsupported provider')

class QasedakSmsSender:
    def send_sms(self, sender, receptor, text):
        print("this is mocking qasedak!")
        print("sent from {} to {}, context:{}".format(sender, receptor, text))
        pass

class SmsIRSmsSender:
    def send_sms(self, sender, receptor, text):
        sms_ir = SmsIr(api_key=SMS_IR_API_KEY, linenumber=sender)
        sms_ir.send_sms(number=str(receptor), message=text, linenumber=sender)