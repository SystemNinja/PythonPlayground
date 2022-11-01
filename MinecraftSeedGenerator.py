import random
import string

class SeedGenerator():
    def __init__(self):
        #super().__init__() # this one is only useful when dealing with methods
        self.seed_length = random.randint(6, 66)
        self.alphabet = string.ascii_letters + string.digits
        result = str(random.choices(self.alphabet, k=self.seed_length)).replace("[", "").replace("]", "").replace(",", "").replace(" ","").replace("'", "")
        print("Seed:")
        print(result)
        print("Seed length: ", len(result))


SeedGenerator()
