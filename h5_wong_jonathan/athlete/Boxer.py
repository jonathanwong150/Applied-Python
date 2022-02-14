# Name: Jonathan Wong
# Email: Jzwong@usc.edu
# Section: 31885
# Spring 2022
# Homework 5

from athlete.Athlete import Athlete

# Create a Boxer class that inherits from Athlete
class Boxer(Athlete):
    # Declare an initial boxer count
    boxer_count=0
    # Description: Initializes a Boxer object
    # Inputs: name (str), dob (str), origin (str), medals (list of strings), weight_class (str), record (list of ints)
    # Returns: None
    # Side effects: Creates a new Boxer object
    def __init__(self, name_param, dob_param, origin_param, medals_param, weight_class_param, record_param):
        # Call the Athlete constructor
        super(Boxer, self).__init__(name_param, dob_param, origin_param, medals_param)
        # Set rest of instance variables
        self.weight_class=weight_class_param
        self.record=record_param
        # Increment boxer count
        Boxer.boxer_count+=1
    # Description: Returns string information on the boxer
    # Inputs: None
    # Returns: String containing boxers information
    # Side effects: None
    def __str__(self):
        result = self.name + " is a " + self.weight_class + " boxer from " + self.origin + " born on " + self.dob + ". " + self.name + " has a " + str(self.record[0]) + "-" + str(self.record[1]) + " record, and has won " + str(len(self.medals)) + " medals: " + str(self.medals) + "."
        return result
    # Define getters for  new instance attributes
    def get_weight_class(self):
        return self.weight_class
    def get_record(self):
        return self.record
    # Description: Changes a boxers weight class
    # Inputs: Weight class parameter (str)
    # Returns: None
    # Side effects: Changes the boxers current weight class
    def set_weight_class(self, weight_class_param):
        self.weight_class=weight_class_param
    # Description: Adds a win to the boxers fight record
    # Input: None
    # Return: None
    # Side effect: Changes value of boxers record list
    def win_fight(self):
        self.record[0]+=1
    # Description: Adds a loss to the boxers fight record and determine if they should retire
    # Input: None
    # Return: None
    # Side effect: Changes value of boxers record list
    def lose_fight(self):
        self.record[1]+=1
        # If the additional loss gives the boxer more than 10 losses,
        if self.record[1]>10:
            # The boxer must retire
            return "This boxer has retired."
        else:
            # Otherwise, return the amount of fights the boxer has left
            fights_left= 10-self.record[1]
            return "This boxer has " + str(fights_left) + " losses before retirement."