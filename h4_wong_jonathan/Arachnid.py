from Arthropod import Arthropod
import random

# Create Arachnid class
class Arachnid(Arthropod):
    # Create variable that holds the number of arachnids
    arachnid_count = 0
    # Description: Initializes an Arachnid object
    # Inputs: name (str), limbs (int), color (str), and venomous parameters (bool)
    # Returns: None
    # Side effects: Creates an instance of arachnid
    def __init__(self, name_param, limbs_count_param, color_param, venomous_param):
        # Call super to use Arthropod constructor
        super(Arachnid,self).__init__(name_param, limbs_count_param, color_param)
        # Assign venmouous value
        self.venomous = venomous_param
        # Increment the number of arachnids
        Arachnid.arachnid_count+=1
    # Description: Retrieves data of the arachnid when printing
    # Inputs: None
    # Returns: A string with arachnid info
    # Side effects: Prints to screen
    def __str__(self):
        # Create a result variable
        result = "The",self.color
        # Add different value depending on if the arachnid is venomous
        if self.venomous:
            result += "venomous"
        else:
            result += "non-venomous"
        # Add rest of string to result and return
        result += self.name,"has",self.limbs_count,"limbs."
        return result
    # Description: Returns information on if the Arachnid is venomous
    # Inputs: None
    # Returns: self.venomous
    # Side effects: None
    def get_venomous(self):
        return self.venomous
    # Description: Returns information on Arachnid power
    # Inputs: None
    # Returns: Power of the arachnid
    # Side effects: None
    def get_power(self):
        # Multiply the power by 2 if arachnid is poisonous
        if self.venomous:
            return self.limbs_count*2
        else:
            return self.limbs_count