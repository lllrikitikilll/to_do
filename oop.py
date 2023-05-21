class Person:

    def __init__(self, name, job, pay):
        self.name = name
        self.job = job
        self.pay = pay

    def get_last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay =  self.pay * (1 + (percent / 100))

    def __repr__(self):
        return f'Person({self.name}, {self.job})'

    def __str__(self):
        return self.name


class Manager(Person):
    def give_raise(self, percent, bonus=10):
        super().give_raise(percent + bonus)




if __name__ == '__main__':
    bob = Person('Alex PAnin', 'DevOps', '10_000')
    print(bob.get_last_name())


