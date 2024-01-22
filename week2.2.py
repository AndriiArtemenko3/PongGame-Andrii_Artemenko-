# This app will count how many times a given letter appeared in a string of text 
# First I had to define a function for counting letters 
def lt_count(string):
    lt_newdictionary = {} # Creating empty dictionary to store the future values of letters

    for lt in string:
        if lt in lt_newdictionary:
            lt_newdictionary[lt] += 1
        else:
            lt_newdictionary[lt] = 1
    return lt_newdictionary
# function checks if the letter is in new dictionary and each time it does it adds 1 to its value

alphabet = 'abcdefghijklmnopqrstuvwxyz' #this is my basic dictionary that includes all the letters of eng alphabet 

# now I "look up" the letters in my alphabet dictionary and setting the basic count of each letter to 0, so if any letter appears in my string its value increases by1
for lt in alphabet:
    value = lt_count("Apple tree is very fruitful").get(lt, 0)
    print(f" '{lt}' count is {value} ")