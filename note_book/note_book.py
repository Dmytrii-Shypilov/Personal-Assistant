import pickle
import re

from collections import UserDict
from prettytable import PrettyTable


########## CLASSES ##################

class NoteBook(UserDict):
    def add_note(self):
        pass

    def get_note(self):
        pass

    def delete_note(self):
        pass

    def get_notes_by_tag(self):
        pass


class Note:
    def __init__(self, tag, title, content):
        self.title = title
        self.tag = tag
        self.content = content



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