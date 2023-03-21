from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter
import pickle
from pathlib import Path
from collections import UserDict
from datetime import datetime
import pickle
from phone_book import ContactBook, Name, Contact
from exception import input_error


p = Path("phone_book/phone_book.bin")
phone_book = ContactBook()
if p.exists():
    with open("phone_book/phone_book.bin", "rb") as file:
        phone_book.data = pickle.load(file)


def save_to_pickle():
    """ Save address book in pickle file"""

    with open("phone_book/phone_book.bin", "wb") as fh:
        pickle.dump(phone_book.data, fh)


def say_hello(s=None):
    return "\nHow can I help you?\n"


def say_goodbye(s=None):
    return "\nGood bye!\n"

@input_error
def add_contact(value):
    """ Add new contact to address book """

    name, *phones = value.lower().title().strip().split()
    name = Name(name.lower().title())

    if name.value not in phone_book:
        record = Contact(name, phones)
        phone_book.add_contact(record)
        if phones:
            for phone in phones:
                record.add_phone(phone)
        save_to_pickle()
        return f"\nContact {name.value.title()} was created.\n"
    else:
        return f"\nContact {name.value.title()} already exists.\n"


@input_error
def show_all(s):
    """ Функція виводить всі записи в телефонній книзі при команді 'show all' """

    if len(phone_book) == 0:
        return "\nPhone book is empty.\n"
    result = ''
    for record in phone_book.values():
        result += f"{record.contacts()}\n"
    return result


@input_error
def remove_contact(name: str):
    ''' Функція для видалення контакта з книги '''

    record = phone_book[name.strip().lower().title()]
    phone_book.del_contact(record.name.value)
    save_to_pickle()
    return f"\nContact {name.title()} was removed.\n"


@input_error
def add_phone(value):
    ''' Функція для додавання телефону контакта'''

    name, phone = value.lower().strip().title().split()

    if name.title() in phone_book:
        phone_book[name.title()].add_phone(phone)
        save_to_pickle()
        return f"\nThe phone number for {name.title()} was recorded.\n"
    else:
        return f"\nContact {name.title()} does not exist.\n"


@input_error
def remove_phone(value):
    ''' Функція для видалення телефону контакта '''
    name, phone = value.lower().title().strip().split()

    if name.title() in phone_book:
        phone_book[name.title()].delete_phone(phone)
        save_to_pickle()
        return f"\nPhone for {name.title()} was delete.\n"
    else:
        return f"\nContact {name.title()} does not exist.\n"


@input_error
def change_ph(value: str):
    ''' Функція для заміни телефону контакта '''

    name, old_phone, new_phone = value.split()

    if name.strip().lower().title() in phone_book:
        phone_book[name.strip().lower().title()].change_phone(
            old_phone, new_phone)
        save_to_pickle()
    else:
        return f"\nContact {name.title()} does not exists\n"


@input_error
def contact(name):
    """ Функція відображає номер телефону абонента, ім'я якого було в команді 'phone ...'"""

    if name.title() in phone_book:
        record = phone_book[name.title()]
        return record.contacts()
    else:
        return f"\nContact {name.title()} does not exist.\n"


@input_error
def add_em(value):
    ''' Функція для додавання e-mail контакта '''

    name, email = value.split()
    name = name.title()
    if name.title() in phone_book:
        phone_book[name.title()].add_email(email)
        save_to_pickle()
        return f"\nThe e-mail for {name.title()} was recorded.\n"
    else:
        return f"\nContact {name.title()} does not exist.\n"


@input_error
def remove_em(value):
    ''' Функція для видалення e-mail контакта '''

    name, email = value.split()
    name = name.title()
    email = email.lower()
    if name.title() in phone_book:
        phone_book[name.title()].delete_email(email)
        save_to_pickle()
        return f"\nThe e-mail for {name.title()} was delete.\n"
    else:
        return f"\nContact {name.title()} does not exist.\n"


@input_error
def change_em(value: str):
    ''' Функція для заміни e-mail контакта '''

    name, old_em, new_em = value.split()

    if name.strip().lower().title() in phone_book:
        phone_book[name.strip().lower().title()].change_email(old_em, new_em)
        save_to_pickle()
        return f"\nThe e-mail for {name.title()} was changed.\n"
    else:
        return f"\nContact {name.title()} does not exists.\n"


@input_error
def add_adrs(value):
    ''' Функція для додавання адреси контакта '''

    name, address = value.split(" ", 1)
    name = name.title()
    if name.title() in phone_book:
        phone_book[name.title()].add_address(address)
        save_to_pickle()
        return f"\nThe address for {name.title()} was recorded.\n"
    else:
        return f"\nContact {name.title()} does not exist.\n"


@input_error
def change_adrs(value):
    ''' Функція для зміни адреси контакта '''

    name, address = value.split(" ", 1)
    name = name.title()
    if name.strip().lower().title() in phone_book:
        phone_book[name.title()].add_address(address)
        save_to_pickle()
        return f"\nThe address for {name.title()} was changed.\n"
    else:
        return f"\nContact {name.title()} does not exists.\n"


@input_error
def remove_adrs(value):
    ''' Функція для видалення адреси контакта '''

    name = value.lower().title().strip()
    if name.title() in phone_book:
        phone_book[name.title()].delete_address()
        save_to_pickle()
        return f"\nAddress for {name.title()} was delete.\n"
    else:
        return f"\nContact {name.title()} does not exist.\n"


@input_error
def remove_bd(value):
    ''' Функція для видалення дня народження контакта контакта '''

    name = value.lower().title().strip()

    if name.title() in phone_book:
        phone_book[name.title()].delete_birthday()
        save_to_pickle()
        return f"\nBirthday for {name.title()} was delete.\n"
    else:
        return f"\nContact {name.title()} does not exist.\n"


@input_error
def add_contact_birthday(value):
    ''' Функція для додавання дня народження контакта к книгу '''

    name, birthday = value.lower().strip().split()

    if name.title() in phone_book:
        phone_book[name.title()].add_birthday(birthday)
        save_to_pickle()
        return f"\nThe Birthday for {name.title()} was recorded.\n"
    else:
        return f"\nContact {name.title()} does not exists.\n"


@input_error
def days_to_bd(name):
    ''' Функція виводить кількість днів до дня народження контакта '''

    if name.title() in phone_book:
        if not phone_book[name.title()].birthday is None:
            days = phone_book[name.title()].days_to_birthday()
            return days
        else:
            return f"\n{name.title()}'s birthday is unknown.\n"
    else:
        return f"\nContact {name.title()} does not exists.\n"


@input_error
def get_birthdays(value=None):
    ''' Функція виводить перелік іменинників за період '''

    if value.strip() == '':
        period = 7
    else:
        period = int(value.strip())
    return phone_book.get_birthdays_per_range(period)


@input_error
def change_bd(value):
    ''' Функція для зміни дня народження контакта '''

    name, new_birthday = value.lower().strip().split()
    if name.title() in phone_book:
        phone_book[name.title()].delete_birthday()
        phone_book[name.title()].add_birthday(new_birthday)
        save_to_pickle()
        return f"\nBirthday for {name.title()} was changed.\n"
    else:
        return f"\nContact {name.title()} does not exist.\n"


@input_error
def search(text_to_search: str):
    """ Search contact where there is 'text_to_search'  """

    return phone_book.search_contact(text_to_search)


def helps(value):
    rules = """LIST OF COMMANDS: \n
    1) to add new contact and one or more phones, write command: add contact <name> <phone> <phone> ... <phone>
    2) to remove contact, write command: remove contact <name>
    3) to add phone, write command: add phone <name> <one phone>
    4) to change phone, write command: change phone <name> <old phone> <new phone>
    5) to remove phone, write command: remove phone <name> <old phone>
    6) to add e-mail, write command: add email <name> <e-mail>
    7) to change e-mail, write command: change email <name> <new e-mail>
    8) to remove e-mail, write command: remove email <name>
    9) to add address, write command: add address <name> <address>
    10) to change address, write command: change address <name> <new address>
    11) to remove address, write command: remove address <name>
    12) to add birthday of contact, write command: add birthday <name> <dd/mm/yyyy>
    13) to remove birthday, write command: remove birthday <name>
    14) to change birthday, write command: change birthday <name> <d/m/yyyy>
    15) to see how many days to contact's birthday, write command: days to birthday <name>
    16) to see list of birthdays in period, write command: birthdays <number of days>
    17) to search contact, where is 'text', write command: search contact <text>
    18) to see full record of contact, write: phone <name>
    19) to see all contacts, write command: show addressbook
    20) to say goodbye, write one of these commands: good bye / close / exit / . 
    21) to say hello, write command: hello
    22) to see help, write command: help
    """
    return rules


handlers = {
    "hello": say_hello,
    "good bye": say_goodbye,
    "close": say_goodbye,
    "exit": say_goodbye,
    "help": helps,
    "add contact": add_contact,
    "remove contact": remove_contact,
    "show addressbook": show_all,
    "add phone": add_phone,
    "remove phone": remove_phone,
    "change phone": change_ph,
    "add email": add_em,
    "remove email": remove_em,
    "change email": change_em,
    "phone": contact,
    "add birthday": add_contact_birthday,
    "remove birthday": remove_bd,
    "change birthday": change_bd,
    "days to birthday": days_to_bd,
    "birthdays": get_birthdays,
    "change address": change_adrs,
    "remove address": remove_adrs,
    "add address": add_adrs
}

completer = NestedCompleter.from_nested_dict({
    "add": {
        "contact": {"<name> <phone> <phone> ... <phone>"},
        "phone": {"<name> <one phone>"},
        "email": {"<name> <e-mail>"},
        "address": {"<name> <address>"},
        "birthday": {"<name> <d/m/yyyy>"},
    },
    "remove": {
        "contact": {"<name>"},
        "phone": {"<name> <old phone>"},
        "email": {"<name>"},
        "address": {"<name>"},
        "birthday": {"<name>"},
    },
    "change": {
        "phone": {"<name> <old phone> <new phone>"},
        "email": {"<name> <new e-mail>"},
        "birthday": {"<name> <d/m/yyyy>"},
        "address": {"<name> <new address>"},
    },
    "phone": {"<name>"},
    "search": {
        "contacts": {"<text_to_seach>"},
    },
    "good bye": None,
    "close": None,
    "exit": None,
    "show": {
        "notebook": None,
    },
    "days to birthday": {"<name>"},
    "birthdays": {"<number of days>"},
    "hello": None,
    "help": None,
})


def main():
    
    while True:
        
        command = prompt('Enter command: ', completer=completer)

        command = command.strip().lower()
        
        if command in ("exit", "close", "good bye", "."):
            say_goodbye()
            break
        else:
            for key in handlers:
                if key in command:
                    print(handlers[key](command[len(key):].strip()))
                    break


if __name__ == "__main__":
    main()
