#!/usr/bin/python3
"""entry point of the command interpreter."""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
import re


def parse(args):
    """parses the arguments"""

    args_list = args.split(" ")
    return args_list
class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = "(hbnb)"

    __av_classes = ['BaseModel']
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    do_EOF = do_exit = do_quit

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        parsed = parse(arg)
        if parsed[0] == '':
            print("** class name missing **")
        elif parsed[0] not in HBNBCommand.__av_classes:
            print("** class doesn't exist **")
        else:
            print(eval(parsed[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        parsed = parse(arg)
        dict = storage.all()
        if parsed[0] == '':
            print("** class name missing **")
        elif parsed[0] not in HBNBCommand.__av_classes:
            print("** class doesn't exist **")
        elif len(parsed) != 2:
            print("** instance id missing **")
        elif "{}.{}".format(parsed[0], parsed[1]) not in dict:
            print("** no instance found **")
        else:
            print(dict["{}.{}".format(parsed[0],parsed[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""

        parsed = parse(arg)
        dict = storage.all()
        if parsed[0] == '':
            print("** class name missing **")
        elif parsed[0] not in HBNBCommand.__av_classes:
            print("** class doesn't exist **")
        elif len(parsed) != 2:
            print("** instance id missing **")
        elif "{}.{}".format(parsed[0], parsed[1]) not in dict:
            print("** no instance found **")
        else:
            del dict["{}.{}".format(parsed[0], parsed[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""

        parsed = parse(arg)
        if len(parsed) > 0 and parsed[0] not in HBNBCommand.__av_classes:
            print("** class doesn't exist **")
        else:
            return_list = []
            for obj in storage.all().values():
                if len(parsed) > 0 and parsed[0] == obj.__class__.__name__:
                    return_list.append(obj.__str__())
                elif len(parsed) == 0:
                    return_list.append(obj.__str__())
            print(return_list)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""

        parsed = parse(arg)
        dictionary = storage.all()
        if parsed[0] == '':
            print("** class name missing **")
            return False
        if parsed[0] not in HBNBCommand.__av_classes:
            print("** class doesn't exist **")
            return False
        if len(parsed) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(parsed[0], parsed[1]) not in dictionary.keys():
            print("** no instance found **")
            return False
        if len(parsed) == 2:
            print("** attribute name missing **")
            return False
        if len(parsed) == 3:
            try:
                type(eval(parsed[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(parsed) == 4:
            obj = dictionary["{}.{}".format(parsed[0], parsed[1])]
            if parsed[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[parsed[2]])
                obj.__dict__[parsed[2]] = value_type(parsed[3])
            else:
                obj.__dict__[parsed[2]] = parsed[3]
        elif type(eval(parsed[2])) == dict:
            obj = dictionary["{}.{}".format(parsed[0], parsed[1])]
            for k, v in eval(parsed[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    value_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = value_type(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
