#!/usr/bin/python3
"""
Console for AirBnb Clone
"""
import cmd
from models import *

class ConsoleShell(cmd.Cmd):
    storage.reload()
    intro = 'Five Yearsssss'
    prompt = '(hbnb) '
    errors = {"noinst": "** no instance found **",
              "noid": "** instance id missing **",
              "noclass" :"** class doesn't exist **",
              "noclassname": "** class name missing **",
              "noval": "** value missing **",
              "cnm_inval": "**class name invalid**"}
    classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

    def do_all(self, args):
        """ Prints all instances of an object"""
        args = args.split(' ')
        if len(args) > 1:
            if args[0] in self.classes:
                storage.reload()
                my_dict = storage.all()
                for key in my_dict.keys():
                    if args[0] in str(my_dict[key]):
                        print(my_dict[key])
            else:
                print(self.errors[noclass])
        else:
            storage.reload()
            my_dict = storage.all()
            for key in my_dict.keys():
                print(my_dict[key])

    def do_create(self, args):
        """type 'create' to make an empty BaseModel"""
        if args is None:
            return
        args = args.split()
        print("length of args is: {}".format(len(args)))
        if len(args) != 1:
            print(self.errors['noclassname'])
        elif args[0] in self.classes:
            new = eval(args[0])()
            print(new.id)
            new.save()
        else:
            print(self.errors['cnm_inval'])

    def do_destroy(self, args):
        """Deletes an instance of an object
        Usage: (hbnb) destroy <name> <id>"""
        if args is None:
            return("Usage: (hbnb) destroy <name> <id>")
        args = args.split()
        if len(args) < 1:
            return self.errors["noclass"]
        if len(args) < 2:
            return self.errors["noid"]
        if args[0] not in self.classes:
            return self.errors["noclass"]
        obj = storage.all()
        if args[1] not in obj.keys():
            return self.errors["noinst"]
        del obj[args[1]]
        storage.save()

    def emptyline(self):
        """empty lines do nothing"""
        pass

    def do_EOF(self, args):
        """entering an EOF will exit the shell"""
        return True

    def do_quit(self, args):
        """type 'quit' to exit the program"""
        return True

    def do_show(self, args):
        """ displays object instances"""
        print("args received: {}".format(args))
        args = args.split()
        if len(args) != 2:
            print("Usage: show BaseModel <1234-1234-1234>")
        else:
            objects = storage.all()
            id_ = args[1]
            if id_ in objects.keys():
                print(objects[id_])
            else:
                print(self.errors["noid"])
    def do_update(self, args):
        """Usage: update <class name> <id> <attribute name> <attribute value>"""
        if args is None:
            return
        args = args.split()
        if len(args) != 4:
            return("$ update BaseModel 1234-1234-1234 email"
            "aibnb@holbertonschool.com")
        all_ = storage.all()
        for id_ in all_.keys():
            if id_ == args[1]:
                setattr(all_[id_], args[2], args[3])
        storage.save()

    def is_class(self, name):
        """checks if arg is in list of known classes"""
        classes = ["BaseModel", "User", "State", "City", "Review",
                         "Amenity", "Place"]
        return name in classes

if __name__ == '__main__':
    ConsoleShell().cmdloop()
