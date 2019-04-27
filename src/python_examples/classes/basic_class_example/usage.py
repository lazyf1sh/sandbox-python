from src.python_examples.classes.basic_class_example.InitMethod import InitMethod
from src.python_examples.classes.basic_class_example.InitMethodArgs import InitMethodArgs
from src.python_examples.classes.basic_class_example.MyClass import MyClass

# default way to call a class method
x = MyClass()
message = x.f()
print(message)

# another way to call a class method:
message = MyClass.f(x)

print(message)

# init method
init = InitMethod()

# init method args
initArgs = InitMethodArgs(1, "123")