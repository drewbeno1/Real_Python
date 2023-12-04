class SomeClass:
    pass

# The () is the constructor which is used to create an object of the class
SomeClass()

# Python classes have some special methods for instantiation:
# __new__(), __init__(), __call__(), __class__()
# __new__() is called when an object is created
# __init__() is called when an object is initialized
# __call__() is called when an object is called
# __class__() is called when an object is created

## Example: Point Class

'''New and init functions are always automatically called, 
but here we just add add a print statement to actually see that they are called.'''

class Point: 
    # args and kwargs allow for an arbitrary number of arguments
    def __new__(cls, *args, **kwargs):
        print('1. Create a new instance of Point.')
        return super().__new__(cls)
    
    def __init__(self, x, y):
        print('2. Initialize the new instance of Point.')
        self.x = x
        self.y = y

point = Point(21, 42) 

# our init function gave us the x and y values we passed in
# if we didnt include an init function, we would not have x and y values to be passed in at all
point.y

# if we want to run just one function at a time, we can bypass the init function
point = Point.__new__(Point)

# Now we can initialize the object with the init function
point = Point.__init__(point, 21, 42)

'''THIS IS A DEMONSTRATION OF HOW IT WORKS NOT HOW IT SHOULD BE USED'''

# .__init__() is the most commonly overriden spoecial method and can be useful to customizing your classes

## Example: Rectangle Class

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # init should not have a return statement ! 

Rectangle = Rectangle(10, 20)

Rectangle.width

## WE can also use init as a test for users to ensure that object attributes are valid
class Rectangle2: 
    def __init__(self, width, height):
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError('The width must be a positive number.')
        self.width = width
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError('The height must be a positive number.')
        self.height = height

# notice what happens when we try to create a rectangle with a negative width
rectangle = Rectangle2(-10, 20)


# in cases where we are using class inheritance, we can inherit the init function from the parent class

# EXAMPLE: Person and Employee 

class Person: 
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date   

class Employee(Person):
    def __init__(self, name, birth_date, position):
        # Super .__init__() calls the init function of the parent class
        super().__init__(name, birth_date)
        self.position = position

john = Employee('John Cleese', '1939-10-27', 'actor')

## We can also pass in otional atttributes to the init function

class Greeter:
    # if you don't specify anything it defaults to False
    def __init__(self, name, formal=False):
        self.name = name
        self.formal = formal

    def greet(self):
        if self.formal:
            print('Hello, Mr. {}'.format(self.name))


'''Objct creation with .__new__()'''

# Custom __new__() methods are rarely used, but can be useful in some cases
# it allows you to customize the object creation process by returning an object of a different class which means you can create objects of immutable classes

## Honestly dont get this concept yet

class SomeClass():
    # args and kwargs allow for an arbitrary number of arguments
    # cls is a call back to the parent class which in this case is SomeClass
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        # customize your instanc in the blank space here and then return it

        return instance



'''Class Attributes and Instance Attributes'''
