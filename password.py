import string
import random


def password_generator(length):
    """ Function that generates a password given a length """

    uppercase_loc = random.randint(1,4)  # random location of lowercase
    symbol_loc = random.randint(5, 6)  # random location of symbols
    lowercase_loc = random.randint(7,12)  # random location of uppercase

    password = ''  # empty string for password

    pool = string.ascii_letters + string.punctuation  # the selection of characters used

    for i in range(length):

        if i == uppercase_loc:   # this is to ensure there is at least one uppercase
            password += random.choice(string.ascii_uppercase)

        elif i == lowercase_loc:  # this is to ensure there is at least one uppercase
            password += random.choice(string.ascii_lowercase)

        elif i == symbol_loc:  # this is to ensure there is at least one symbol
            password += random.choice(string.punctuation)

        else:  # adds a random character from pool
            password += random.choice(pool)

    return password  # returns the string

print(password_generator(12))
