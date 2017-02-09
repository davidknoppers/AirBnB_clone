#!/usr/bin/python3
import cmd

class ConsoleShell(cmd.Cmd):
    intro = 'Five Yearsssss'
    prompt = '(hbnb)'

    def do_quit(self, args):
        """type 'quit' to exit the program"""
        quit()

    def do_EOF(self, args):
        """entering an EOF will exit the shell"""
        print("")
        quit()

if __name__ == '__main__':
    ConsoleShell().cmdloop()
