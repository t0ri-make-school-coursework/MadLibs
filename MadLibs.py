import sys

# Original Plan, Input in Dictionary (unused)
# var word_dict = {
#     "plural_noun": {
#         "plural_noun_1": "", #print (word_dict["plural_noun"][plural_noun_1]) prints ""
#         "plural_noun_2": "",
#     },
#     "adjective": {
#         "adjective_1": "",
#         "adjective_2": "",
#     },
#     "number": {
#         "number_1": "",
#         "number_2": "",
#     }
#     "store_1": "",
#     "animal_1": "",
#     "letter_1": "",
#     "silly_word_1": ""
# }

# List containing tuples for each blank in MadLib.
# Tuples hold string of blank's part of speech, and the type the part of speech requires.
word_type = [('an adjective', str),     #1, 0
         ('a plural noun', str),        #2, 1
         ('a plural noun', str),        #3, 2
         ('a number', int),             #4, 3
         ('a silly word', str),         #5, 4
         ('a food', str),               #6, 5
         ('an animal', str),            #7, 6
         ('an adjective', str),         #8, 7
         ('a letter', str),             #9, 8
         ('a dollar amount', float)]    #10, 9

# List containing words to fill blanks in MadLib.
words = []

# Checks if input (w) is an int.
def is_int(w):
    try:
        int(w)
        return True
    except ValueError:
        return False

# Checks if input (w) is a float.
def is_float(w):
    try:
        float(w)
        return True
    except ValueError:
        return False

# Calls is_int() and is_float() to determine and reassign its type.
def sort_type(w):
    # If input has no "." (ie is not a float) and is an int, reassign input as int.
    if "." not in w:
        if is_int(w):
            w = int(w)
            # If input isn't an int, but is a float, reassign as float.
    elif is_float(w):
        w = float(w)
    # If input isn't a float or int, input will return as string.
    # Return the newly assigned input.
    return w

# If user enters "exit", exit program
def exit_story(w):
    if w == "exit":
        print("Thanks for playing!")
        sys.exit()

# Function takes value of word (ie each blank in MadLib).
def store_user_input(word):
    # Input is called using first value of each tuples.
    # Input is sorted in sort_type() and assigned to variable w.
    w = sort_type(input("Please enter {}: ".format(word[0])))

    exit_story(w)
    # Checks if the input type matches the type in index 1 of each tuple.
    if type(w) == word[1]:
        # If the type is correct, input is added to words list.
        words.append(w)
    else:
        print("Wrong type!  Try again!")
        # If type is incorrect, store_user_input() is called again using the same tuple.
        store_user_input(word)

# Function that runs entire program.
def start_libs():
    print(chr(27) + "[2J")
    print("Welcome to San Francisco MadLibs!")
    print("Type \"exit\" at any time to exit the game.")
    # For each tuple in word_type, call store_user_input using that tuple.
    for word in word_type:
        store_user_input(word)
    print("Welcome to San Francisco!  A(n) {} city full of {}, {} — and home to over {} diverse neighborhoods to explore!  My favorite neighborhood in SF is the {} which is home to a famous restaurant that sells the country’s best {}, plenty of {} owners out and about with their pets, and even a(n) {} park to visit with friends!  You can get there via the {} Muni Line for only ${}!".format(*words))

start_libs()
# Test Function inputs word type into each blank and calls the print with those words
# def test_libs():
#
#     words[0] = "[adjective]"
#     words[1] = "[plural noun]"
#     words[2] = "[plural noun]"
#     words[3] = "[number_1]"
#     words[4] = "[silly word]"
#     words[5] = "[food]"
#     words[6] = "[animal]"
#     words[7] = "[adjective]"
#     words[8] = "[letter]"
#     words[9] = "[dollar amount]"
#
#     print(words)
#     print("Welcome to San Francisco!  A(n) {} city full of {}, {} — and home to over {} diverse neighborhoods to explore!  My favorite neighborhood in SF is the {} which is home to a famous restaurant that sells the country’s best {}, plenty of {} owners out and about with their pets, and even a(n) {} park to visit with friends!  You can get there via the {} Muni Line for only ${}!".format(*[_ for _ in words]))
#
# test_libs()

# print(words)

# IDEAS
    # add is_empty(w):
    # to the end of sort_type(w):
