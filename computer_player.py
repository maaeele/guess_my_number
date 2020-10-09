#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:09:16 2020

@author: maelebelmont
"""

import random

from guess_my_number import MIN, MAX, GuessMachine

if __name__ == '__main__':
    guess_nachine = GuessMachine()
    while True:
        attempt = random.randint(MIN,MAX)
        result = guess_nachine.guess(attempt)
        print('tried: %d: %s' % (attempt, result))
        if result == 'found':
            print('Finished in %d attempts.' % guess_nachine.number_of_attempt)
            break