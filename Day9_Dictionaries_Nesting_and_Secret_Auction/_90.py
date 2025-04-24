programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Bug"])
print()

programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)
print()

empty_dict={}

#Wipe an Existing Dictionary 
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an Existing Dictionary 
programming_dictionary["Bug"] = "A moth in your computer"


# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])