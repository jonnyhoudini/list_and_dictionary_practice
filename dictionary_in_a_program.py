napoleon = {
    "full name": "Napoleon Bonaparte",
    "place of birth": "Corsica",
    "born": 1769,
    "died": 1821,
    "place of death": "Saint Helena"

}

def find_age(person):
    return person["died"] - person["born"]

napoleon_age = find_age(napoleon)

print(napoleon_age)

# In a comment at the bottom of the file, write a few sentences answering the questions: 1) What are lists/dictionaries used for in programming? 2) What is the code you’ve submitted doing?