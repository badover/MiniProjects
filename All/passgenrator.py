# -*- coding:utf -8 -*-
#!/usr/bin/python
#made by - github.com/badover

import random
import tkinter as tk

def passgen():
    symbols = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    number = int(input('Enter a number of passwords: '))
    length = int(input('Enter a password length: '))

    for i in range(number):
        password = ''
        for j in range(length):
            password += random.choice(symbols)
        print(password)

passgen()