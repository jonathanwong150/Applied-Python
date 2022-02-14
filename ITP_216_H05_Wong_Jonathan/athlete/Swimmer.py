# Name: Jonathan Wong
# Email: Jzwong@usc.edu
# Section: 31885
# Spring 2022
# Homework 5

from Athlete import Athlete


# Create Swimmer class that inherits from Athlete
class Swimmer(Athlete):
    # Set swimmer count
    swimmer_count=0
    # Description: Initializes a swimmer object
    # Inputs: name (str), dob (str), origin (str), medals (list of strings), strokes (list of strings)
    # Returns: None
    # Side effects: Creates a new Swimmer object
    def __init__(self, name_param, dob_param, origin_param,medals_param, strokes_param):
        # Calls Athlete's constructor
        super(Swimmer, self).__init__(name_param, dob_param, origin_param, medals_param)
        # Set strokes value
        self.strokes=strokes_param
        Swimmer.swimmer_count+=1
    # Description: Returns string information on the swimmer
    # Inputs: None
    # Returns: String containing swimmer information
    # Side effects: None
    def __str__(self):
        result = self.name + " is a swimmer from " + self.origin + " born on " + self.dob + ". " + self.name + " knows " + str(self.strokes) + ", and has won " + str(len(self.medals)) + " medals: " + str(self.medals) + "."
        return result
    # Gets list of known strokes
    def  get_strokes(self):
        return self.strokes
    # Adds a stroke to the swimmers list
    def add_strokes(self, stroke_param):
        if stroke_param not in self.strokes:
            self.strokes.append(stroke_param)