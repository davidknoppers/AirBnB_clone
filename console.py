#!/usr/bin/python3
"""
Console for AirBnb Clone
Two hundred lines of functionality, aww yeah
Can be used with direct commands, e.g. create BaseModel,
or by calling objects e.g. BaseModel.count()
"""
import cmd
from models import *



class HBNBCommand(cmd.Cmd):
    """
    Main class for the console
    Contains all helper function excluding memory management
    Memory management is handled by file_storage
    """
    storage.reload()
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
        """
        Prints all instances of an object
        """
        args = args.split()
        print("arg length: {}".format(len(args)))
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
        args = args.split()
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
            print("Usage: (hbnb) destroy <name> <id>")
        else:
            args = args.split()
            if len(args) < 1:
                print(self.errors["noclassname"])
            elif len(args) < 2:
                print(self.errors["noid"])
            elif args[0] not in self.classes:
                print(self.errors["noclass"])
            else:
                obj = storage.all()
                if args[1] in obj.keys():
                    del obj[args[1]]
                    storage.save()
                else:
                    print(self.errors["noinst"])

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
        args = args.split()
        if len(args) != 4:
            print("$ update BaseModel 1234-1234-1234 email"
            "aibnb@holbertonschool.com")
        else:
            all_ = storage.all()
            for id_ in all_.keys():
                if id_ == args[1]:
                    setattr(all_[id_], args[2], args[3])
            storage.save()

            """
            functionality for advanced tasks
            """

    def do_User(self, args):
        self.class_exec('User', args)

    def do_BaseModel(self, args):
        self.class_exec('BaseModel', args)

    def do_State(self, args):
        self.class_exec('State', args)

    def do_City(self, args):
        self.class_exec('City', args)

    def do_Amenity(self, args):
        self.class_exec('Amenity', args)

    def do_Place(self, args):
        self.class_exec('Place', args)

    def do_Review(self, args):
        self.class_exec('Review', args)

    def class_exec(self, classname, args):
        if args[:6] == '.all()':
            self.do_all(classname)
        elif args[:6] == '.show(':
            self.do_show(classname + ' ' + args[7:-2])
        elif args[:8] == ".count()":
            count = 0
            if classname in self.classes:
                storage.reload()
                all_ = storage.all()
                for key in all_.keys():
                    if classname in str(all_[key]):
                        count += 1
                    else:
                        storage.reload()
                        all_ = storage.all()
                        for key in all_.keys():
                            count += 1

            print(count)


        elif args[:9] == '.destroy(':
            self.do_destroy(classname + ' ' + args[10:-2])
        elif args[:8] == '.update(':
            if '{' in args and '}' in args:
                new_arg = args[8:-1].split('{')
                new_arg[1] = '{' + new_arg[1]
            else:
                new_arg = args[8:-1].split(',')
            if len(new_arg) == 3:
                new_arg = " ".join(new_arg)
                new_arg = new_arg.replace("\"", "")
                new_arg = new_arg.replace("  ", " ")
                self.do_update(classname + ' ' + new_arg)
            elif len(new_arg) == 2:
                try:
                    dty = eval(new_arg[1])
                except:
                    return
                for j in dty.keys():
                    self.do_update(classname + ' ' + new_arg[0][1:-3] + ' ' + str(j) + ' ' + str(dty[j]))
        else:
            print("Command not recognized")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
