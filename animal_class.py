class Animal():

    # Characteristics

    def __init__(self, name, color, eyes = 2): # runs only one when you initialise an object
        self.name = name
        self.number_eyes = eyes
        self.alive = True
        self.number_animal_eaten = 0
        self.age = 0
        self.color = color


    # Behaviours - functions that belong to a class
    # Methods - functions that can only be used in this class instance

    def eat(self, food = 'Fajitas'):
        return 'NOM NOM NOM' + food
    def sleep(self):
        return 'ZZzzZZZzzz zzo zleeeppy'
    def hunt(self):
        return 'ATTAACKK!! THIS IS SPARTAAAA'
    def potty(self):
        return 'HUNNNN...PLOOP'
    def fly(self):
        return 'WOOIIIII Lukatdi view'
# Let's create an object of class animal
    # -- called initialising an object

#my_animal = Animal()
#print(type(my_animal))

