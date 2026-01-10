#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place  
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):


    prompt = "(hbnb) "

    valid_classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True 
    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True
    
    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, line):
  
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(args[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
    
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        print(all_objects[key])

    def do_destroy(self, line):

        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")    


    def do_all(self, line):

        all_objs = storage.all()
        list_objs = []
        if not line:
            for obj in all_objs.values():
                list_objs.append(str(obj))
        else:
            args = line.split()
            if args[0] not in self.valid_classes:
                print("** class doesn't exist **")
                return
            for key, obj in all_objs.items():
                if obj.__class__.__name__ == args[0]:
                    list_objs.append(str(obj))
        print(list_objs)


    def do_update(self, line):
      
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = all_objs[key]
        attr_name = args[2]
        attr_value = args[3]

        if attr_value.startswith('"') and attr_value.endswith('"'):
            attr_value = attr_value[1:-1]

        try:
            if attr_value.isdigit():
                attr_value = int(attr_value)
            elif float(attr_value):
                attr_value = float(attr_value)
        except ValueError:
            pass

        setattr(obj, attr_name, attr_value)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()