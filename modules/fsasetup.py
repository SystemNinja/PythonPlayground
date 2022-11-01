"""
This module is used for FSA setup scripts
Basically just process setup form and call it from Autokey scripts.
"""

import re

def process_form(dict_key):
    myfile = "/home/white/Programming/Python/sci/fsa_new_user_form.txt"
    data = {}

    with open(myfile, "r") as file:
        for line in file:
            key, value = line.strip().split(":")
            data[" ".join(key.split())] = value.strip()
    return re.sub(" +", " ", str(data.get(dict_key)))
