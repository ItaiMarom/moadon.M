import re

def a(string):
    special_characters = re.compile(r'[ ^A-Za-z0-9\s]')
    return special_characters.search(string) is not None


def  MANIUAK(password):

    password1 = len(password)
    x = 0
    if(password1 > 7):
        y = any(char.isupper() for char in password)
        z = any(char.islower() for char in password)
        x = any(char.isdigit() for char in password)
        o = a(password)
        if y and x and z and o:
            return "the password is strong"
        else:
            if y and x or y and z or y and o or z and o or z and x or x and o:
                return "the password is mid"
            else:
                if y or x or z or o:
                    return "password is weak"
        
    else:
       return False,"pawword need 8 letters"




password = ("A@dasswodawd1")
print(MANIUAK(password))
