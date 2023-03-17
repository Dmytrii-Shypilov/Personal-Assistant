import pickle
import re

from collections import UserDict
from prettytable import PrettyTable


########## COMMANDS ################

COMMANDS = ['add note', 'delete note', 'get by tag', 'get by title', 'exit']



########## CLASSES ##################

class NoteBook(UserDict):
    def add_note(self, note):
        self.data.update({(note.title): note})

    def get_note(self, title):
        note = self.data.get(title, None)
        return note

    def delete_note(self, title):
        deleted = self.data.pop(title)
        return deleted

    def get_notes_by_tag(self, tag):
        notes_list = self.data.values()
        notes = list(filter(lambda x: x.tag == tag, notes_list))
        return notes


class Note:
    def __init__(self):
        self._title = None
        self._tag = None
        self._text = None

    @property
    def title(self):
        return self._title
    
    @property
    def tag(self):
        return self._tag
    
    @property
    def text(self):
        return self._text

    @title.setter
    def title(self, title):
        if title == '':
            raise ValueError("Value shood not be empty")
        elif len(title) > 20:
            raise ValueError("Title should not exceed 20 characters")
        else:
            self._title = title

    @tag.setter
    def tag(self, tag):
        if tag == '':
            raise ValueError("Value shood not be empty")
        elif len(tag) > 20:
            raise ValueError("Title should not exceed 20 characters")
        else:
            self._tag = tag

    @text.setter
    def text(self, text):
        if text == '':
            raise ValueError("Value shood not be empty")
        if len(text) > 250:
            raise ValueError("Title should not exceed 250 characters")
        else:
            self._text = text



class Tag:
    def __init__(self, value):
        self.value = value

class Title:
    def __init__(self, value):
        self.value = value

class Content:
    def __init__(self, value):
        self.value = value

##############  MODULE FUNCTIONS ################

chat_in_progress = True ##### RUNNING PROGRAM STATUS

note_book = NoteBook()


def input_error(func):
    def inner_func(args=None):
        try:
            if not args:
                result = func()
            else:
                result = func(args)
            return result
        except IndexError:
            print(
                "Assistant: Please, type ...")
        except ValueError as err:
            print(err.args[0])
            return None
    return inner_func

def get_instructions(message):
    command_not_found = True

    for command in COMMANDS:
        if message.startswith(command):
            if command == "add note":
                args = create_note_object()
                return (command, args)
            args = message.replace(command, '').strip().split(' ')
            command_not_found = False
            return (command, args)
    if command_not_found:
        raise ValueError(
            f"Assistant: Please enter a valid command: {', '.join(COMMANDS)}")

def check_validity(value, status, type):
    if value != "":
        status[type] = True
    else:
        print("It should not be empty!")


def create_note_object():
    new_note = Note()
    while True:
        try:
            title = input("Enter a title: ")
            new_note.title = title
        except ValueError as err:
            print(err.args[0])
            continue
        break
    while True:
        try:
            tag = input("Enter a tag: ")
            new_note.tag = tag
        except ValueError as err:
            print(err.args[0])
            continue
        break
    while True:
        try:
            text = input("Type your note: ")
            new_note.text = text
        except ValueError as err:
            print(err.args[0])
            continue
        break

    return [new_note]

@input_error
def add_note(args):
    [note] = args
    note_book.add_note(note)
    return f"Note with title {note.title} was successfully added"



def greet():
    print("How can I help you with managing the notes?")


def terminate_assitant():
    global chat_in_progress 
    chat_in_progress = False




def main():
    message = input("Enter command: ")
    command_args = get_instructions(message)
    bot_message = None

    if not command_args:
        return

    command, args = command_args

    # print(command)
    # print(args)

    match command:
        case "add note":
            bot_message = add_note(args)
        case "exit":
            terminate_assitant()

    if bot_message:
        print(bot_message)


while chat_in_progress:
    main()