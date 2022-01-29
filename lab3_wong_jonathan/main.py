# Name: Jonathan Wong
# Email: Jzwong@usc.edu
# Section: 31885
# Spring 2022
# Lab 3

# Parameters: The file name
# Returns: The first line/header of the file
# Description: Opens a file and returns the first line of it
# Side effects: None
def file_read_header(fileName):
    f_in=open(fileName,'r') # Open file in read mode
    header=f_in.readline() # Read the entire first line int a string
    f_in.close() # Close the file
    return header

def file_read_data(fileName):
    f_in=open(fileName,'r') # Open in read mode
    junk=f_in.readline() # Get rid of the first line of the file
    contents=[]
    for line in f_in: # Loop through the file
        contents.append(line) # Add each line to a list
    f_in.close() # Close and return
    return contents

def main():
    header=file_read_header("oscar_age_female.csv") # Call the read functions
    data=file_read_data("oscar_age_female.csv")
    print("Header:\n\t",header,end="") # Print out the header
    print("Data:\n",end="")
    for item in data: # Loop through data list and print lines one by one
        print("\t" + item,end="")

if __name__ == '__main__':
    main()