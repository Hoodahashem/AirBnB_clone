#!/usr/bin/python3
"""entry point of the command interpreter."""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    do_EOF = do_exit = do_quit

    def emptyline(self):
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
