class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


    def __len__(self):
        print(f'Колличество этажей в {self.name}: ', self.number_of_floors)

    def __str__(self):
        print(f'Название: ', self.name)

    def __eq__(self, other):
        isinstance(self, int)
        isinstance(other, int)
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        isinstance(self, int)
        isinstance(other, int)
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        isinstance(self, int)
        isinstance(other, int)
        return self.number_of_floors > other.number_of_floors

    def __gt__(self, other):
        isinstance(self, int)
        isinstance(other, int)
        return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        isinstance(self, int)
        isinstance(other, int)
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        isinstance(self, int)
        isinstance(other, int)
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value

        return self.number_of_floors

h1 = House('ЖК Горский', 2)
h2 = House('Домик в деревне', 2)

h1.go_to(17)
h2.go_to(5)

h1.__len__()
h2.__len__()

h1.__str__()
h2.__str__()

h1.__add__(7)
print(h1.number_of_floors)
h2.__add__(5)

print(h2.number_of_floors)
print(f'eq -',h1 == h2)
print(f'lt -',h1 < h2)
print(f'le -',h1 > h2)
print(f'gt -',h1 <= h2)
print(f'ge -',h1 >= h2)
print(f'ne -',h1 != h2)


