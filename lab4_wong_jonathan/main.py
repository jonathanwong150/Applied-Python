# Name: Jonathan Wong
# Email: Jzwong@usc.edu
# Section: 31885
# Spring 2022
# Lab 4

import random

# Create arthropod class
class Arthropod(object):
    # Creates a class variable to keep track of number of instances
    count=0
    # Description: Creates a new arthropod object
    # Inputs: Parameters including name, number of limbs, and color
    # Returns: Nothing
    # Side effect: Creates a new object
    def __init__(self, name_param, limbs_count_param, color_param):
        self.name = name_param # Set self attributes equal to the input parameters
        self.limbs_count = limbs_count_param
        self.color = color_param
        Arthropod.count+=1 # Increment the number of arthropods
    # Description: Returns the name of the arthropod object
    # Inputs: None
    # Returns: Arthropod name
    # Side efect: None
    def get_name(self):
        return self.name
    # Description: Returns the color of the arthropod object
    # Inputs: None
    # Returns: Arthropod color
    # Side efect: None
    def get_color(self):
        return self.color
    # Description: Returns the number of limbs of the arthropod object
    # Inputs: None
    # Returns: Arthropod limb count
    # Side efect: None
    def get_limbs_count(self):
        return self.limbs_count
    # Description: Changes the color of the arthropod object
    # Inputs: Color parameter
    # Returns: None
    # Side efect: Alters arthropod instance color
    def set_color(self,color_param):
        self.color=color_param
    # Description: Generates a random number and subtracts from the arthropods limbs
    # Inputs: None
    # Returns: None
    # Side efect: Alters arthropod limbs
    def lose_fight(self):
        lost=random.randint(0,self.limbs_count) # Generate a random number up until the current limb count
        self.limbs_count-=lost # Subtract from current limbs