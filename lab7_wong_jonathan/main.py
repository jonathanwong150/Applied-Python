# Name: Jonathan Wong
# Email: Jzwong@usc.edu
# Section: 31885
# Spring 2022
# Lab 7

import functools

# Description: Validate the input of the function
# Inputs: Takes in a function to validate
# Returns: Prints validation messages and all values of our input
# Side Effects: Prints to output
def validator_decorator(func):
    # Import from functools
    @functools.wraps(func)
    # Wrapper function that takes in args and kwargs
    def wrapper(*args, **kwargs):
        print("Testing arguments:")
        # Check if args are strings and the kwargs are dictionaries
        if isinstance(args[0], str) and isinstance(kwargs,dict):
            # If true, print validation message
            print("\tArguments accepted: all args are Strings, and all kwargs are dictionaries with")
            print("\ttwo k:v pairs.")
            # Call the print function to print our output
            func(*args, **kwargs)
        # If one of the args or kwargs is of the wrong type
        else:
            # Print an invalid message and print all the inputs
            print("\tArguments rejected: not all kwargs have two key:value pairs.")
            func(*args, **kwargs)
    return wrapper

# Description: Prints all args and kwargs
# Inputs: A string message and dictionary of animals
# Returns: None
# Side effects: Print to output
@validator_decorator
def print_all_the_things(message, dictionary):
    print("Printing args:")
    # Loop through message and print each word one by one
    for word in message.split():
        print("\t",word)
    # Print entire dictionary
    print("Printing kwargs:")
    print("\t",dictionary)

def main():
    # Initialize a dictionary
    dict={}
    dict["cat"]=True
    dict["dog"]=False
    # Call print function
    print_all_the_things("Another lab involving animals.",dict)

if __name__ == "__main__":
    main()