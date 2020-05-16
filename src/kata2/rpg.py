#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    result = str(random.choice(string.ascii_letters)) + str(random.choice(string.digits)) + str(random.choice(string.punctuation))
    for len in range(passLen - 3): 
        result += random.choice([str(random.choice(string.ascii_letters)), str(random.choice(string.digits)), str(random.choice(string.punctuation))])

    return result

RandomPasswordGenerator()