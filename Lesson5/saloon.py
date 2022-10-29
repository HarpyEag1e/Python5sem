from random import seed, choice


class Human:
    def __init__(self, name: str, age: int, sex: str, \
                 hairs_length: int, nails_length: int, nails_colour: str = "colorless"):
        self.name = name
        self.age  = age
        self.sex  = sex
        self.hairs_length = hairs_length
        self.nails_length = nails_length
        self.nails_colour = nails_colour

    def __str__(self) -> str:
        return f'{self.name}, {self.age}, {self.sex}; hairs: {self.hairs_length}; ' + \
               f'nails: {self.nails_length}, {self.nails_colour}; job: {self.__class__.__name__}'

    def __repr__(self) -> str:
        return f'Human({self.name}, {self.age}, {self.sex}; hairs: {self.hairs_length}; ' + \
               f'nails: {self.nails_length}, {self.nails_colour}; job: {self.__class__.__name__})'

class Manicurist(Human):
    def do_job(self, human: Human):
        if human.nails_length > 0:
            human.nails_length -= 1
        human.nails_colour = choice(["red", "violet", "green"])

class Hairdresser(Human):
    def do_job(self, human: Human):
        if human.hairs_length > 0:
            human.hairs_length -= 1

class Barber(Human):
    def do_job(self, human: Human):
        if human.sex != "M":
            raise ValueError("Error: wrong sex! (males only)")
        if human.hairs_length > 0:
            human.hairs_length -= 1

if __name__ == "__main__":
    seed()

    neo = Human(name = "Neo", sex = "M", age = 30, hairs_length = 10, nails_length = 2)
    ann = Human(name = "Ann", sex = "F", age = 18, hairs_length = 20, nails_length = 4)
    bob = Human(name = "Bob", sex = "M", age = 24, hairs_length = 3,  nails_length = 1)


    manicurist = Manicurist(name = "Samara", sex = "F", age = 25, hairs_length = 30, nails_length = 5)
    hairdresser = Hairdresser(name = "Sasha", sex = "F", age = 35, hairs_length = 8, nails_length = 3)
    barber = Barber(name = "Pavel", sex = "M", age = 41, hairs_length = 0, nails_length = 1)

    print("All the people:")
    print(neo)
    print(ann)
    print(bob)
    print(manicurist)
    print(hairdresser)
    print(barber)

    print("\nNeo, Ann and Bob after some cutting:")
    manicurist.do_job(neo)
    hairdresser.do_job(ann)
    barber.do_job(bob)

    print(neo)
    print(ann)
    print(bob)
