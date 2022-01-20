#!/usr/bin/env python
import requests
import logging

import string
import random

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
length = 10

def generate_random_password():
    ## shuffle the characters
    random.shuffle(characters)
    
    ## picking random characters from the list
    password = []
    
    for i in range(length):
        password.append(random.choice(characters))    
    random.shuffle(password)

    generated_password = ("".join(password))
    
    ## Returning auto generated password
    return generated_password

if __name__ == '__main__':
    generate_random_password()
