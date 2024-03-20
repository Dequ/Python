from datetime import datetime


def get_instantiation_time(self):
    return self.instantiation_time

class MyMeta(type):
    class_names = []
    def __new__(mcs, name, bases, dictionary):
        dictionary["get_instantiation_time"] = get_instantiation_time
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.instantiation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mcs.class_names.append(name)
        return obj


class My_Class1(metaclass=MyMeta):
    pass


x = My_Class1()

print(x.instantiation_time)
print(MyMeta.class_names)
