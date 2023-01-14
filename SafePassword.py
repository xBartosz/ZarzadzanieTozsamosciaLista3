import string
import random
import re

def create_safe_password():
    asd = string.ascii_letters, string.punctuation, string.digits
    characters = "".join(asd)
    result = ""
    for i in range(8, 64):
        result += random.choice(characters)        
    result = result.replace(" ", "")
    #Sprawdzenie
    regex = ("^(?=.*[a-z])(?=." +
             "*[A-Z])(?=.*\\d)" +
             "(?=.*[-+_!@#$%^&*., ?]).+$")
    p = re.compile(regex)

    if re.search(p, result):
        print(result)
    else:
        create_safe_password()



create_safe_password()