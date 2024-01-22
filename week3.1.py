# Make a function that takes two arguments (given name and family name), the second of which is optional. Print a greeting according to which arguments are provided.
def hi_there(name, family_name):
    if family_name:
        print(name + " " + family_name) # " " for space between them
    else:
        print(name)

name = input("First Name:")

family_name = input("Family Name (optional):")

if name: #this logical structure makes the name mabdatory now
  hi_there(name, family_name)
else: 
    print("Error")

