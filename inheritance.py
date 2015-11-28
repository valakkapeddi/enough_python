class Parent:
    def public_method(self):
        return 'from Parent.public_method'

    def another_public_method(self):
        return 'from Parent._private_method'


class Child(Parent):
    def public_method(self):
        return 'from Child.public_method'

    def another_public_method(self):
        return 'calling base-class method - ' + Parent.another_public_method(self)

a = Child()
print a.public_method()
print a.another_public_method()


class NewStyleParent(object):
   def public_method(self):
        return 'from NewStyleParent.public_method'

   def another_public_method(self):
        return 'from NewStyleParent.public_method'

   def __mangled_method(self):
       return 'from NewStyleParent.mangled_method'


class NewStyleChild(NewStyleParent):
    def public_method(self):
        super(NewStyleChild, self).public_method()


class AnotherParent(object):
   def public_method(self):
        return 'from AnotherParent._private_method'

   def another_public_method(self):
        return 'from AnotherParent._private_method'

   def __mangled_method(self):
       return 'from AnotherParent.mangled_method'


class AnotherChild(AnotherParent, NewStyleParent):

    # In case of multiple inheritance,
    def public_method(self):
        super(AnotherChild, self).public_method()

    def calls_mangled_methods(self):
        return super(AnotherChild, self)._AnotherParent__mangled_method() + ' and ' + super(AnotherChild, self)._NewStyleParent__mangled_method()

b = AnotherChild()
print b.calls_mangled_methods()
