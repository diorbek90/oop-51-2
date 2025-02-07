# Абстрация

from abc import ABC, abstractmethod


# Nikita
# Twilio.com


class OTPService(ABC):

    @abstractmethod
    def sms_send(self):
        pass


class NikitaOTP(OTPService):

    def sms_send(self, phone):
        phone = input("Введите тел в формате +996xxx xx xx xx")


class Twilio(OTPService):

    def sms_send(self, phone):
        phone = input("Введите тел в формате +7xxx xx xx xx")


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):

    def make_sound(self):
        return print('Gaf gaf')
