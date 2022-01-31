# Name: Jonathan Wong
# Email: Jzwong@usc.edu
# Section: 31885
# Spring 2022
# Homework 3

# Description: Retrieves file contents
# Parameters: Name of file
# Returns: Header list and list containing all data in file
# Side effects: None
def file_reader(fileName):
    f_in = open(fileName, 'r')  # Open file in read mode
    header = f_in.readline()  # Read the entire first line into a string
    contents = []
    for line in f_in:  # Loop through the file
        contents.append(line.strip().split(", "))  # Split and strip each line and add each line to a list
    f_in.close()  # Close the file
    return header, contents # Returns two items

# Description: Calculates the average value of all Deniro movies
# Parameters: List of integers
# Returns: Mean score
# Side effect: None
def calculate_mean(intList):
    sum=0.0 # Create a float to store sum value
    for num in intList:
        sum+=num # Loop through list and add to sum
    return sum/len(intList) # Divide by length of list and return

# Description: Retrieves all movies from a list that have a higher score than mean
# Parameters: A list of movies and a target score
# Returns: List of all movies that have a higher score
# Side effects: None
def find_movies_above_score(movieList, score):
    results=[]
    for line in movieList:
        if int(line[1])>score: # If movie has a higher than average score,
            results.append(line) # Append to results list
    return results # Return

def main():
    head,data=file_reader("deniro.csv") # Retrieves the header and data from the input file
    scoreList=[]
    for line in data: # Loop through the movie data
        scoreList.append(int(line[1])) # Add scores to a list
    mean=calculate_mean(scoreList) # Use list to calculate mean
    goodMovies=find_movies_above_score(data,mean) # Find all movies that have an above average score
    print("I love Robert Deniro!\nThe average Rotten Tomatoes score for his movies is",str(mean) + ".") # Print menu
    print("Of",len(scoreList),"movies,",len(goodMovies),"are above average.\nHere they are:") # Print amount of movies above average
    print("\tYear\tScore\tTitle")
    for movie in goodMovies: # Loop through all the movies that meet criteria
        print("\t" + movie[0] + "\t" + movie[1] + "\t\t" + movie[2].strip("\"")) # Print all

if __name__ == '__main__':
    main()