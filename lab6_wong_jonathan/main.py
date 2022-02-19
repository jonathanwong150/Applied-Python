# Name: Jonathan Wong
# Email: Jzwong@usc.edu
# Section: 31885
# Spring 2022
# Lab 6

def main():
    # Use comprehension to generate a list of all numbers that are multiples of 7
    # Exclude 0 from list
    sevens = [i for i in range(1000) if i % 7 == 0 and i != 0]
    # Print lis of sevens to check
    print(sevens)

    # Hard-code name and genus lists
    name = ['Great potoo', 'Smew', 'Tundra bean goose', 'Southern pied babbler']
    genus_and_species = ['Nyctibius grandis', 'Mergellus albellus', 'Anser serrirostris', 'Turdoides bicolor']
    # Use comprehension to generate a dictionary that maps names to genus and species
    birdos = {name:genus for name,genus in zip(name,genus_and_species)}
    print(birdos)

    # Use generator expression to find all squares in a certain range
    square_gen= (i**2 for i in range(10))
    # Iterate up until the generators bound and print
    for number in range(10):
        print(number, 'squared:', next(square_gen))

if __name__ == "__main__":
    main()