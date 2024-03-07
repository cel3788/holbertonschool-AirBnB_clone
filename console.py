import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it to the JSON file, and print the id"""
        if arg == "":
            print("** class name missing **")
        elif arg not in models.classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = models.storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = models.storage.all()
            if key in all_objs:
                del all_objs[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances based on the class name"""
        if arg and arg not in models.classes:
            print("** class doesn't exist **")
        else:
            all_objs = models.storage.all()
            if arg:
                filtered_objs = [str(obj) for key, obj in all_objs.items() if arg == key.split(".")[0]]
            else:
                filtered_objs = [str(obj) for key, obj in all_objs.items()]
            print(filtered_objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id with a new attribute value"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = models.storage.all()
            if key in all_objs:
                obj = all_objs[key]
                attr_name = args[2]
                attr_value = args[3]
                try:
                    attr_value = eval(attr_value)
                except:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
