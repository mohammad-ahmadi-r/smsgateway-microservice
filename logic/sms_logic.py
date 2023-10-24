class SmsFactory:
    @staticmethod
    def create_sender(provider):
        if provider == 'qasedak':
            return QasedakSmsSender()
        elif provider == 'mock':
            return MockSmsSender()
        elif provider == 'kavenegar':
            return KavenegarSmsSender()
        elif provider == 'twilio':
            return TwilioSmsSender()
        else:
            raise ValueError('Unsupported provider')

class QasedakSmsSender:
    def send_sms(self, sender, receptor, text):
        print("sent by qasedak")
        print(text)
        pass

class KavenegarSmsSender:
    def send_sms(self, sender, receptor, text):
        print("sent by kavenegar")
        print(text)
        pass

class TwilioSmsSender:
    def send_sms(self, sender, receptor, text):
        print("sent by twilio")
        print(text)
        pass

class MockSmsSender:
    def send_sms(self, sender, receptor, text):
        print("sent by mock provider")
        print(text)
        pass