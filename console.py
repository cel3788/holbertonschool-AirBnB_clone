#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class contains a simple command interpreter
    that inherits from cmd.Cmd."""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Exits the program."""
        return True

    def do_EOF(self, arg):
        """Handles End of File, exits the program."""
        return True

    def emptyline(self):
        """called when an empty line is entered
        instead of repeating the last nonempty command entered,
        it shouldn't execute anyhing.
        """
        pass

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
