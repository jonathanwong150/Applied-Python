# Name: Jonathan Wong
# Email: Jzwong@usc.edu
# Section: 31885
# Spring 2022
# Homework 2

def main():
    cats_names = ('Cassandra', 'Sir Whiskington', 'Truck') # Lists of names for dictionary
    dogs_names = {'Barkey McBarkface', 'Leeloo Dallas', 'Taro'}
    parrots_names = ['Squawk', 'Squawk 2: the Squawkquel', 'Larry']
    names = ['peter', 'paul', 'mary']
    animals = ('cat', 'cat', 'hamster')

    count=0 # Keep track of number of animals
    dict={} # Initialize an empty dictionary
    temp = [] # Temporary list variable
    for name in cats_names: # Loop through cat list
        temp.append(name) # Add each name to a list
        count+=1 # Increment count
        dict["cat"]=temp # Set dictionary value equal to the list
    temp = []
    for name in dogs_names: # Loop through dogs
        temp.append(name) # Append to list
        count+=1 # Increment
        dict["dog"]=temp # Set dictionary value to the list
    temp = []
    for name in parrots_names: # Loop through parrots
        temp.append(name) # Append name to list
        count+=1 # Increment
        dict["parrot"]=temp # Set dict value to list
    for num in range(3): # Loop through the other collection using range
        if animals[num] in dict: # If animal already exists in dictionary
            dict[animals[num]].append(names[num].title()) # Append to existing list
        else: # Otherwise,
            temp = [] # Create an empty list
            temp.append(names[num].title()) # Add name to list
            dict[animals[num]]=temp # Set dict key for that animal to the list
        count+=1 # Increment
    print("Hello!") # Print menu
    print("Please choose from the following options:")
    print("\t1. See all your pets' names.\n\t2. Add a pet.\n\t3. Exit")
    choice=input("What would you like to do? (1, 2, 3): ")
    print()
    while True: # Keep going until we get a 3
        if choice=="1":
            print("You have",count,"pets.") # Print number of pets
            for key in dict: # Loop through dictionary keys
                print(key,end=": ") # Print each key
                for value in dict[key]: # Loop through each list at dict[key]
                    print(value,end=", ") # Print values
                print()
        elif choice=="2":
            count+=1 # Increment
            animal=input("What kind of animal is this?: ") # Ask user for an animal and name
            name=input("What is the name of the " + animal + "?: ")
            if animal in dict: # If it already exists
                dict[animals].append(name.title()) # Append
            else: # Otherwise
                temp = [] # Create temp list
                temp.append(name.title()) # Append name
                dict[animal]=temp # Set dict to list
            print("Great!",name.title(),"the",animal,"is now added to your pets.") # Success message
        elif choice=="3":
            print("Goodbye!") # Goodbye message and exist program
            return
        else:
            print("That's not a number.") # Error message

        print("Please choose from the following options:")
        print("\t1. See all your pets' names.\n\t2. Add a pet.\n\t3. Exit")
        choice = input("What would you like to do? (1, 2, 3): ")
        print()

if __name__ == '__main__':
    main()