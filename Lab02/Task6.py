import copy

class Demo:
    def __init__(self, value):
        self.value = value

    def __del__(self):
        print("Object destroyed automatically")

obj1 = Demo(30)

obj2 = copy.copy(obj1)
obj3 = copy.deepcopy(obj1)

print(obj1.value, obj2.value, obj3.value)
