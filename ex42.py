## Animal is-a object (Yes, Sort of confusing) look at the extra credit.
class Animal(object):
    pass

## Dog is-a object of Animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a attribute name
        self.name = name

## Cat is-a object of Animal
class Cat(Animal):

    def __init__(self, name):
        ##
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ##
        self.name = name

        ## Personal has-a pet of some kind
        self.pet = None
    def printhair(self):
        print("Your hair is black")
## Employee is a object og Person
class Employee(Person):

    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
        ##Employee has-a prop
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## salmo is-a object of Fish
class salmon(Fish):
    pass

##
class halibut(Fish):
    pass


# rover is-a dog
rover = Dog("Rover")

# santan is=a cat
satan = Cat("Satan")

# marry is-a Person
mary = Person("Marry")
mary.printhair()
## mary has-a pet santan
mary.pet = satan

# frank is=a Employee
frank = Employee("Frank",120000)

# frank has-a pet rover
frank.pet = rover

# flipper is-a fish
flipper = Fish()

# crouse is-a salmon
crouse = salmon()

#harry is-a halibut
harry = halibut()