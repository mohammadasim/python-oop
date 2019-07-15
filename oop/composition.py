class Leg:
    pass


class Back:
    pass


class Chair:
    """
    Composition means when one class is made up of other classes
    """
    def __init__(self, number_of_legs):
        self.legs = [Leg() for leg in range(number_of_legs)]
        self.back = Back()

    def __repr__(self):
        return 'I have {} legs and one back.' . format(len(self.legs))


print(Chair(5))

