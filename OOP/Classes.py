"""Classes are used to create objects by defining types 

ex: Program for building doors. 

Class = DoorClass 
Properties = height, color 
Behaviors = open(), close()

You can substantiate multiple indpendent objects from this class, ex: door1 and door2 are independent. The class just tells them how to be built

ex 2: Video Game

Class = EnemyClass
Attributes = name, health, power_level
Behaviors = attack(), takedamage()

ex 3: Web Browsers 

Class = TabClass
Attributes = title (would be a string), is_current(would be a boolean), page(this could be anything...we can make a custome type)
Behaviors = close(), reload() 

**** Behaviors are really known as "Instance methods"

* How would we make a custom page type?
by making a PageClass that allows for multiple types!

"""

'''Dry: Don't Repeat Yourself'''

# Example 1: 
# pass just tells python it is empty 
class Dog: 
    pass

'''now let's create some dogs with this'''

a = Dog()
b = Dog()
# Why is it false? Dog initializes a unique object everytime its called ! 
a == b

type(a)


# 1.b 
# Now let's make a real Dog class
# now we give our class "Attributes" 

# What's the __init__(self)?, its an initializer. It allows Python to AUTOMATICALLY call this function when the class is called. 
## This means that when we substantiate the Dog class, we'll have to pass in a name and an age for each dog. 

class Dog: 
    # Class Attributes: applies to the whole class, so every dog we substantiate is a mammal. 
    species = 'mammal'

    # Instance Attributes: unique for each object in the class
    def __init__(self, name, age,):
        self.name = name
        self.age = age

    # Instance Methods: Gives behaviors that can be called
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)    

    # This method doesnt actually return anything, it just adds 1 to the age
    def birthday(self): 
        self.age += 1

'''Now if we go to initialize dogs from this class'''
# Notice the error message when you try to do this:
dog1 = Dog()

#instead do thisss
Buck = Dog('Buck', 1)
mikey = Dog('mikey', 5)

print(Buck.name)
print(Buck.species)
print(Buck.age)

print("{} is {} and {} is {}".format(Buck.name, Buck.age, mikey.name, mikey.age))

if Buck.species == 'mammal':
    print("{} is a {}".format(Buck.name, Buck.species))
else: 
    print("{} is not a mammal".format(Buck.name))

## Important note: The dogs are independent from each other and the class after created. Watch! 

Buck.species = 'fish'

print(Buck.species)

'''Now let's play with the instance methods '''

print(mikey.speak("Gruff Gruff!"))

print(Buck.description())

# Everytime I run this, he will gain a year in age. 
Buck.birthday()

print(Buck.description())


'''PART 2: OOP Inheritance

We like to stick by the code of DRY, so what if you are creating a class of people, and every person has the same possibilities of attributes,
but babies are a little different. They are still people though so...what do we do that doesnt require copying and pasting two classes? '''

# A baby is a person always, but a person isnt always a baby

'''Inheritance will allow us to make one class a base class and another class a deriviate of that class.

So the baby class will automatically inherit every attribute of the person class, but we can add or modify more that are unique to baby'''

class Person:
    description = "general person"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("My name is {} and I am {} years old".format(self.name, self.age))

    def eat(self, food):
        print("{} eats {}".format(self.name, food))

    def action(self):
        print("{} spins around !".format(self.name))

# here is the syntax. Now the Baby class has all the attributes of a Person by default unless we change them (like we do description and speak), 
#     and we can add more like nap
#     Also, if we change the action function in Person, it will change in Baby too!
'''Baby is a "Child" class or also known as a "derived" class'''
class Baby(Person):
    description = "baby"

    def speak(self):
        print("ba ba ba ba")

    def nap(self):
        print("{} takes a nap".format(self.name))


person1 = Person("Steve", 20)

person1.speak()
person1.eat("pasta")
person1.action()

baby = Baby("Ian", 1)
baby.speak()
baby.eat("Baby food")
baby.action()

print(person1.description)
print(baby.description)

# Only baby has access to the nap method. 
baby.nap()