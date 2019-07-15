class ClassA:
    def hi(self):
        print('Hello!')


class ClassB:
    def hi(self):
        print('Hallo!')

    def another(self):
        print('We are in classB')


class ClassC(ClassA, ClassB):
    """
    In Python when we inherit from multiple classes
    when a method is invoked it will go and first check
    in the firt class, if it is there it will invoke it
    otherwise it will go and check the second class from
    which the class is inheriting.
    """
    pass


c = ClassC()
c.hi()
c.another()