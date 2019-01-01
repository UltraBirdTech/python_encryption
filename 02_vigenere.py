#! /usr/bin/env python
# -*- coding: utf8 -*- #

import sys

def enc_Vigenere( target, key ):
    result = ''
    cycle = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_'
    remove_num = 0
    for n in range(0, len(target)):
        index1 = cycle.find(key[(n - remove_num) % len(key)])
        if ((target[n] == '') or (target[n]== '.')):
            result = result + target[n]
            remove_num +=1
        else:
            index2 = cycle.find(target[n])
            index = index2 + index1
            if (index >= len(cycle)):
                index = index % len(cycle)
            result = result + cycle[index]
        n = n + 1
    return result

def dec_Vigenere( target, key ):
    result = ''
    cycle = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_'
    remove_num = 0
    for n in range(0, len(target)):
        index1 = cycle.find(key[(n - remove_num) % len(key)])
        if ((target[n] == '') or (target[n]== '.')):
            result = result + target[n]
            remove_num +=1
        else:
            index2 = cycle.find(target[n])
            index = index2 - index1
            if (index >= len(cycle)):
                index = index % len(cycle)
            result = result + cycle[index]
        n = n + 1
    return result

class Vigenere:
    def __init__(self):
      self.result = ''
      self.cycle = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_'
      self.encription = ''
      self.decription = ''
    
    def encryption(target, key):
        result = ''
        remove_num = 0
        for n in range(0, len(target)):
            index1 = self.cycle.find(key[(n - remove_num) % len(key)])
            if ((target[n] == '') or (target[n]== '.')):
                result = result + target[n]
                remove_num +=1
            else:
                index2 = self.cycle.find(target[n])
                index = index2 + index1
                if (index >= len(self.cycle)):
                    index = index % len(self.cycle)
                result = result + self.cycle[index]
            n = n + 1
        self.encription = result
        print self.encription

    def descryption(target, key):
        result = ''
        remove_num = 0
        for n in range(0, len(target)):
            index1 = self.cycle.find(key[(n - remove_num) % len(key)])
            if ((target[n] == '') or (target[n]== '.')):
                result = result + target[n]
                remove_num +=1
            else:
                index2 = self.cycle.find(target[n])
                index = index2 - index1
                if (index >= len(self.cycle)):
                    index = index % len(self.cycle)
                result = result + self.cycle[index]
            n = n + 1
        self.decription = result
        print self.decription
    
    def calulate_index():
        # soemthin write
        return

class EncVigenere(Vigenere):
    def __init__():
        return
        # something write

    def calculate_index(i1, i2):
        return i2 + i1

class DecVigenere(Vigenere):
    def __init__():
        return
        # something write

    def calculate_index(i1, i2):
        return i2 - i1

def main():
    
    argv = sys.argv
#    print argv
#    if (len(argv) != 2):
#        print 'Argument is less. Please add char'
#        exit()
#    enc = argv[1]

    target = 'There are four pencils in the pencil case.'.upper()
    print target
    key = 'FLAG{CTF_FINDKEY}'.upper()
    print key
    enc_str = enc_Vigenere( target, key )
    print enc_str

    print dec_Vigenere( enc_str, key )

main()
