from Arthropod import Arthropod
import random

# Create insect class
class Insect(Arthropod):
    # Variable to track number of insects
    insect_count = 0
    # Description: Initializes an Insect object
    # Inputs: name (str), limbs (int), color (str), and wings (int) parameters
    # Returns: None
    # Side effects: Creates an instance of insect
    def __init__(self, name_param, limbs_count_param, color_param, wings_count_param):
        # Call super to initialize Arthropod values
        super(Insect,self).__init__(name_param, limbs_count_param, color_param)
        # Set the number of wings and increment insect count
        self.wings_count = wings_count_param
        Insect.insect_count+=1
    # Description: Retrieves data of the insect when printing
    # Inputs: None
    # Returns: A string with insect info
    # Side effects: Prints to screen
    def __str__(self):
        return "The",self.color,self.name,"has",self.limbs_count,"limbs and",self.wings_count,"wings."
    # Description: Returns information on number of insect wings
    # Inputs: None
    # Returns: self.wings_count
    # Side effects: None
    def get_wings_count(self):
        return self.wings_count
    # Description: Returns information on Insect power
    # Inputs: None
    # Returns: self.limbs_count + self.wings_count
    # Side effects: None
    def get_power(self):
        self.limbs_count + self.wings_count
    # Description: Overrides the lose_fight method from Arthropod to include losing wings
    # Inputs: None
    # Returns: None
    # Side effects: Alters the amount of wings an insect has
    def lose_fight(self):
        super(Insect,self).lose_fight() # Calls lose_fight method on legs
        lost=random.randint(0,self.wings_count) # Generate a random number up until the current wing count
        self.wings_count -= lost  # Subtract from current wings