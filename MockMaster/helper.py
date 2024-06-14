from twilio.rest import Client
import random

global sid
sid  = "AC05bf7adc7a1dc53888ddc302ee16f5d8"
global token
token = "2395b55e275759fbc98da90dc86e48c1"


class OTPverification:    
    phone_number = None
    otp = None
    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp

    def send_otp_on_phone(self):
        client = Client(sid, token)
        try:
            message = client.messages.create(
                body = f'your otp is {self.otp}',
                from_ = '+14695072412',
                to = self.phone_number
            )
        except:
            raise Exception("somthing went wrong")
        
            