# Name: Jonathan Wong
# Email: Jzwong@usc.edu
# Section: 31885
# Spring 2022
# Homework 5

# Creates a parent class that will be inherited by Boxer and Swimmer classes
class Athlete(object):
    # Set initial count to 0
    athlete_count=0
    # Description: Initializes an Athlete object
    # Inputs: name (str), dob (str), origin (str), medals (list of strings)
    # Returns: None
    # Side effects: Creates a new Athlete object
    def __init__(self, name_param, dob_param, origin_param,medals_param):
        # Set instance variables
        self.name=name_param
        self.dob=dob_param
        self.origin=origin_param
        self.medals=medals_param
        # Increment athlete count
        Athlete.athlete_count+=1
    # Create getters for each Athlete attribute
    def get_name(self):
        return self.name
    def get_dob(self):
        return self.dob
    def get_origin(self):
        return self.origin
    def get_medals(self):
        return self.medals
    # Description: Adds a medal to the athlete's medal list
    # Inputs: medal (str)
    # Return: None
    # Side effects: Appends a new medal to the medal list
    def add_medal(self, medal_param):
        self.medals.append(medal_param)
