class Person():
    def __init__(self, name, age, sex, zipcode, illness):
        self.name = name
        self.age = (int(age), int(age))
        self.sex = sex
        self.zipcode = zipcode
        self.illness = illness

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}".format(self.name, self.print_age(), self.sex, self.zipcode, self.illness)

    def print_age(self):
        from_age = self.age[0]
        to_age = self.age[1]
        if from_age == to_age:
            return str(from_age)
        else:
            return "{0} bis {1}".format(from_age, to_age)