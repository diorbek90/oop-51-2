
import random
from lesson import OTPService


class RUSms(OTPService):

    def sms_send(self, phone):
        phone = input("Введите тел в формате +7xxx xx xx xx")


ru_sms = RUSms()

