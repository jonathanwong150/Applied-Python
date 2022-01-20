def main():
    str= input("Please enter an input to be converted: ") # Get input from user
    print("String: ",end="")
    for char in str: # Iterate through the string
        print(char + ", ",end="") # Print out each letter
    print() # Newline for formatting

    charList=list(str) # Cast to a list
    print("List: ",end="")
    for char in charList: # Iterate through the list
        print(char + ", ",end="") # Print each index followed by a comma
    print()

    charTuple=tuple(str) # Cast to a tuple
    print("Tuple: ",end="")
    for char in charTuple: # Loop through the tuple
        print(char + ", ", end="") # Print each index
    print()

    charSet=set(str) # Cast to a set
    print("Set: ", end="")
    for char in charSet: # Loop through the set
        print(char + ", ", end="") # Print each item
    print()

    charDict={}
    for char in str: # Loop through the string
        if char not in charDict: # If the char is not already in the dictionary,
            charDict[char]=1 # Add the char and set value to 1
        else:
            charDict[char]+=1 # If it already exists, increment the value
    print("Dictionary: ")
    for key in charDict: # Loop through dictionary and print
        print("\t" + key + ":",charDict[key])

if __name__ == '__main__':
    main()