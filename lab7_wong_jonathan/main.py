# Name: Jonathan Wong
# Email: Jzwong@usc.edu
# Section: 31885
# Spring 2022
# Lab 7

import functools

def validator_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Testing arguments:")
        if isinstance(args[0], str) and isinstance(kwargs,dict):
            print("\tArguments accepted: all args are Strings, and all kwargs are dictionaries with")
            print("\ttwo k:v pairs.")
            func(*args, **kwargs)
        else:
            print("\tArguments rejected: not all kwargs have two key:value pairs.")
            func(*args, **kwargs)
    return wrapper

@validator_decorator
def print_all_the_things(message, dictionary):
    print("Printing args:")
    for word in message.split():
        print("\t",word)
    print("Printing kwargs:")
    print("\t",dictionary)

def main():
    dict={}
    dict["cat"]=True
    dict["dog"]=False
    print_all_the_things("Another lab involving animals.",dict)

if __name__ == "__main__":
    main()