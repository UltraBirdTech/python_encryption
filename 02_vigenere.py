#! /usr/bin/env python
# -*- coding: utf8 -*- #

import sys

class Vigenere:
    def __init__(self):
      self.result = ''
      self.cycle = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_'
      self.encryption_result = ''
      self.decryption_result = ''
    
    def execution(self, target, key):
        result = ''
        remove_num = 0
        for n in range(0, len(target)):
            index1 = self.cycle.find(key[(n - remove_num) % len(key)])
            if ((target[n] == '') or (target[n]== '.')):
                result = result + target[n]
                remove_num +=1
            else:
                index2 = self.cycle.find(target[n])
                index = self.calculate_index(index2, index1)
                if (index >= len(self.cycle)):
                    index = index % len(self.cycle)
                result = result + self.cycle[index]
            n = n + 1
        return result

    def encryption(self, target, key):
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
        self.encryption_result = result
        print self.encryption_result

    def descryption(self, target, key):
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
        self.decryption_result = result
        print self.decryption_result
    
    def calculate_index(self, i2, i1):
        # soemthing write for child class.
        print 'something write for child class.'
        exit()
        return

class EncVigenere(Vigenere):
    def __init__(self):
        super(Vigenere, self).__init__()
        return
        # something write

    def excution(self, target, key):
        result = super().excution(self, target, key)
        self.encryption_result = result
        return

    def calculate_index(i1, i2):
        return i2 + i1

    def display():
        print self.encryption_result
        return 

class DecVigenere(Vigenere):
    def __init__(self):
        super(Vigenere, self).__init__()
        return
        # something write

    def excution():
        result = super().excution(self, target, key)
        self.descryption_result = result
        return

    def calculate_index(i1, i2):
        return i2 - i1

    def display():
        print self.descryption_result
        return

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

#    vigenere = Vigenere()
#    vigenere.encryption(target, key)
#    vigenere.descryption(vigenere.encryption_result, key)

    enc_vigenere = EncVigenere()
    enc_vigenere.excute()
    enc_vigenere.display()

main()
