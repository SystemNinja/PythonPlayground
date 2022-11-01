r"""
Generate password using words from english dictionary.
Requirements:
-Total number of characters must be at least 8 or 9
-Words will start with first capital letter, if password has more than one word, first letter of each will be uppercase
-Must contain one of the symbols: ! @ #
-Must contain one number


Get list from dictionary by picking key value and get value from list using index.
print(pick_list.get(1)[4])

Test output with multiple entries writen to a file:
with open("test-output.txt", "a") as file1:
    n = 0
    while (n <= 100):
        gen_number = random.randint(1, 99)
        output = rand_words[random.randint(0, len(rand_words)-1)].capitalize()+symbols[random.randint(0, len(symbols)-1)]+str(gen_number)
        file1.writelines(output+"\n")
        n+=1

"""

import random
import os

def generate_password():
    colors = ['red', 'green', 'yellow', 'white', 'blue', 'black', 'pink', 'purple', 'cyan', 'gray', 'silver', 'orange', 'brown']
    animals = ['fox', 'wolf', 'eagle', 'tiger', 'parrot', 'lion']
    rand_words = ['sky', 'grass', 'tree', 'leaf', 'rain', 'rainy', 'fire', 'fiery']
    symbols = ['!', '@', '#']
    gen_number = random.randint(1, 99)

    # place above arrays into dictionary
    pick_list = {
        1: colors,
        2: animals,
        3: rand_words
    }

    pick_list_seed = random.randint(1,3)

    output = pick_list.get(pick_list_seed)[random.randint(0, len(pick_list.get(pick_list_seed))-1)].capitalize()+symbols[random.randint(0, len(symbols)-1)]+str(gen_number)
    if (len(output) < 9):
        dice = random.randint(1, 3)
        if(dice == 1): # print colors+animals 
            output = pick_list.get(1)[random.randint(0, len(pick_list.get(1))-1)].capitalize()+pick_list.get(2)[random.randint(0, len(pick_list.get(2))-1)].capitalize()+symbols[random.randint(0, len(symbols)-1)]+str(gen_number)
        elif(dice == 2): # print colors+rand_words
            output = pick_list.get(1)[random.randint(0, len(pick_list.get(1))-1)].capitalize()+pick_list.get(3)[random.randint(0, len(pick_list.get(3))-1)].capitalize()+symbols[random.randint(0, len(symbols)-1)]+str(gen_number)
        elif(dice == 3): #print rand_words+animals
            output = pick_list.get(3)[random.randint(0, len(pick_list.get(3))-1)].capitalize()+pick_list.get(2)[random.randint(0, len(pick_list.get(2))-1)].capitalize()+symbols[random.randint(0, len(symbols)-1)]+str(gen_number)
        else:
            print("Shit got screwed up...")
    print(output)

generate_password()
while(True):
    prompt = str.lower(input("Generate another name (Y/N)? "))
    if(prompt == "y"):
        os.system("cls")
        generate_password()
    elif(prompt == "n"):
        break
    else:
        os.system("cls")
        print("Wrong option, try again.")
        continue