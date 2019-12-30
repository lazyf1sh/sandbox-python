from src.com.github.lazyf1sh.sandbox.python.classes import InitMethod
from src.com.github.lazyf1sh.sandbox.python.classes import InitMethodArgs
from src.com.github.lazyf1sh.sandbox.python.classes import MyClass

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