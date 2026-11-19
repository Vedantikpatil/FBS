#Write a program which calculates toll calculation on some location following is data provided:
#Many vehicles goes through the toll every vehicle has to pay the basic toll + extra charges if any.two wheelers have to pay basic toll Rs 20 three wheelers have to pay 30 and four wheelers have to pay 40
#heavy veheicles i.e. Vehicles having wheels more than four, have to pay 60 Rs as basic toll extra charges :
#for two wheelers if no. of persons are more than two extra charge=10/person
#for three wheelers if no. of persons are more than 3 extra charge=20/person
#for four wheelers if no. of persons are more than 4 extra charge=40/person
#for heavy vehicle if no. of person are more than 6 extra charges=100/person.
#Show polymorphic behaviour in main. Main module should be designed in such way that toll should easily operate it through interactive menu driven program .
#Object of vehicle class should not be possible.


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def calculate_toll(self):
        pass


class TwoWheeler(Vehicle):

    def __init__(self, person):
        self.person = person

    def calculate_toll(self):
        toll = 20
        if self.person > 2:
            toll = toll + (self.person - 2) * 10
        return toll


class ThreeWheeler(Vehicle):

    def __init__(self, person):
        self.person = person

    def calculate_toll(self):
        toll = 30
        if self.person > 3:
            toll = toll + (self.person - 3) * 20
        return toll


class FourWheeler(Vehicle):

    def __init__(self, person):
        self.person = person

    def calculate_toll(self):
        toll = 40
        if self.person > 4:
            toll = toll + (self.person - 4) * 40
        return toll


class HeavyVehicle(Vehicle):

    def __init__(self, person):
        self.person = person

    def calculate_toll(self):
        toll = 60
        if self.person > 6:
            toll = toll + (self.person - 6) * 100
        return toll


while True:

    print("\n1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        p = int(input("Enter number of persons: "))
        v = TwoWheeler(p)

    elif ch == 2:
        p = int(input("Enter number of persons: "))
        v = ThreeWheeler(p)

    elif ch == 3:
        p = int(input("Enter number of persons: "))
        v = FourWheeler(p)

    elif ch == 4:
        p = int(input("Enter number of persons: "))
        v = HeavyVehicle(p)

    elif ch == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
        continue

    print("Total Toll = Rs.", v.calculate_toll())
