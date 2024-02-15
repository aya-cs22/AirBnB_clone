#!/usr/bin/python3
""" A modulel that contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import sys
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class for Console Commands"""

    prompt = "(hbnb)"

    def do_EOF(self, line):
        """A command interpreter to exit the program with EOF or Ctrl+D"""

        return True

    def help_EOF(self):
        """Shows functionality of EndOfFile"""

        print("EOF command to exit the program")

    def emptyline(self):
        """Pressing enter doesn't execute anything"""

        pass

    def do_create(self, cName):
        '''Creates new instance of BaseModel'''

        if not cName:
            print ("** class name missing **")
            return
        if cName != "BaseModel":
            print ("** class doesn't exist **")
            return
        else:
            newInstance = BaseModel()
            storage.save()
            print (newInstance.id)

    def do_show(self, args):
        '''Prints the string representation of an instance'''

        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all()
        if key in instance:
            print(instance[key])
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
