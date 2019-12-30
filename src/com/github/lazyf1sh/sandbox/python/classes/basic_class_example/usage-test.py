import unittest

from src.com.github.lazyf1sh.sandbox.python.classes import AttributeOverriding
from src.com.github.lazyf1sh.sandbox.python.classes.basic_class_example.InstanceVariables import InstanceVariables


class MyTest2(unittest.TestCase):
    def test1(self):
        # instance variables
        print("instance variables")
        d = InstanceVariables('Fido')
        e = InstanceVariables('Buddy')

        self.assertEqual(d.kind, "canine")
        self.assertEqual(e.kind, "canine")
        self.assertEqual(d.name, "Fido")
        self.assertEqual(e.name, "Buddy")

    def test__attribute_overriding(self):
        a = AttributeOverriding()
        self.assertEqual(a.name, "qqq")
        self.assertEqual(a.name2(), "name 2")

        exception = False
        try:
            a.name()  # method is overriden by instance variable
        except TypeError as e:
            exception = True
        self.assertTrue(exception)
