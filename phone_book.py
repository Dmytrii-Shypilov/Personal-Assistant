from collections import UserDict
from datetime import datetime
import pickle
from pathlib import Path
import re


class Field:

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):

    def __str__(self):
        return self._value.title()


class Phone(Field):

    @staticmethod
    def validate_phone(phone):
        new_phone = str(phone).strip().replace("+", "").replace(" ", "")\
            .replace("(", "").replace(")", "").replace("-", "")
        if not new_phone.isdigit():
            raise ValueError("The phone number should contain only numbers!")
        else:
            if len(new_phone) == 10:
                return f"{new_phone}"
            else:
                raise ValueError("Check the length of the phone number!")

    def __init__(self, value):
        self._value = Phone.validate_phone(value)

    @Field.value.setter
    def value(self, value):
        self._value = Phone.validate_phone(value)


class Email(Field):

    @staticmethod
    def validate_email(email):
        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,}$"
        if re.match(pattern, email) is not None:
            return f"{email}"
        else:
            raise ValueError("Email is not correct!")

    def __init__(self, value):
        self._value = Email.validate_email(value)

    @Field.value.setter
    def value(self, value):
        self._value = Email.validate_email(value)


class Address(Field):

    def __str__(self):
        return self._value


class Birthday(Field):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            if value != None:
                self._value = datetime.strptime(value, '%d/%m/%Y').date()
        except ValueError:
            print(f'Please, input the date in format dd/mm/yyyy ')


class Record:

    def __init__(self, name, phone=None, email=None, birthday=None, address=None):
        self.name = name
        self.birthday = birthday
        self.address = address

        self.emails = []
        if email:
            self.emails.append(email)

        self.phones = []
        if phone:
            self.phones.append(phone)

  
   