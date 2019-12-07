from abc import ABC, abstractmethod, ABCMeta


class A:
    pass


class B(A):
    pass


b = type('AB', (A, ), {})

print(b)


class myAbstract(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def myMethode(self):
        pass


b = B()
print("b is instance A: ", isinstance(b, A))
print("b is instance B: ", isinstance(b, B))

print(A.__class__)
print(B.__class__)

print("A is subclass of object: ", issubclass(A, object))
print("A is instance of object: ", isinstance(A, object))
print("A is subclass of type: ", issubclass(A, type))
print("A is instance of type: ", isinstance(A, type))

print("myAbstract is subclass of object: ", issubclass(myAbstract, object))
print("myAbstract is instance of object: ", isinstance(myAbstract, object))
print("myAbstract is subclass of type: ", issubclass(myAbstract, type))
print("myAbstract is instance of type: ", isinstance(myAbstract, type))

print("object is instance of type: ", isinstance(object, type))
print("object is subclass of type: ", issubclass(object, type))

print("type is instance of object: ", isinstance(type, object))
print("type is subcalss of object: ", issubclass(type, object))


print("B is subclass of A: ", issubclass(B, A))
print("B is instance of A: ", isinstance(B, A))

# print("b is subclass of A: ", issubclass(b, A))
print("b is instance of A: ", isinstance(b, A))


def f():
    pass


print(myAbstract.__class__)
print(ABCMeta.__class__)
# a = myAbstract()


print(eval("print(\'salam\')"))
