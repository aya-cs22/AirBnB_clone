#!/usr/bin/python3
""" A modulel that contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ Class for Console Commands"""

    prompt = "(hbnb)"
    def do_EOF(self, line):
        """A command interpreter to exit the program with EOF or Ctrl+D"""

        return True

    def do_quit(self, line):
        """A command interpreter to exit the program with quit"""

        return True

    def help_quit(self):
        """Shows functionality of quit"""

        print("Quit command to exit the program")

    def help_EOF(self):
        """Shows functionality of EndOfFile"""

        print("EOF command to exit the program")

    def emptyline(self):
        """Pressing enter doesn't execute anything"""

        pass
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
