from animal_class import *
class Reptile(Animal): #Inheritance
    # it will run all the same method as Animal

    # adding characteristics and overrides the previous __init__ method. The super() calls the previous method so our objects have the previous methods.
    # AND THEN!! we add more characteristics

    def __init__(self, name, color, number_heart, camo, eyes = 2):
        super().__init__(name, color, eyes) # Runs the __init in parent class
        self.number_heart = number_heart
        self.camo = camo


    def eat(self, food = 'bugs'): # Polymorphism where we override the method .eat()
        return ('ssssslrrrruuppppp tasssstyyyy' + food)
    def hunt(self):
        return ('HUNT HUNT HUNT HUNT GRR')

    def seek_heat(self): #adding new methods to this class (polymorphing how the class looks)
        return ('Mmmmm isaa bit chilly, why did I sit at the back of the class?')
    pass