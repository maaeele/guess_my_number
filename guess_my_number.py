#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:13:09 2020

@author: sbancal
"""

import random

MIN = 6
MAX = 1000

class GuessMachine():
    def __init__(self):
        self.number_to_guess = random.randint(MIN, MAX)
        self.number_of_attempt = 0

    def guess(self, num):
        self.number_of_attempt += 1

        if num < self.number_to_guess:
            return "too low"
        elif num > self.number_to_guess:
            return "too high"
        else:
            return "found"

if __name__ == '__main__':
    guess_nachine = GuessMachine()
    print("Hey! try to guess a number between %d and %d!" % (MIN, MAX))

    while True:
        user_input = input("Your guess?")
        try:
            user_attempt = int(user_input)
            result = guess_nachine.guess(user_attempt)
            if result == "found":
                print("Fantastic you could find the number I Had in mind in %d attempts" % guess_nachine.number_of_attempt)
                break
            else:
                print(result)
        except ValueError:
            print("You joker ... that was not an integer!")
