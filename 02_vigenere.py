#! /usr/bin/env python
# -*- coding: utf8 -*- #

class Vigenere(object):
    def __init__(self):
      self.cycle = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_'
    
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
                index = self.calculate_index(index1, index2)
                if (index >= len(self.cycle)):
                    index = index % len(self.cycle)
                result = result + self.cycle[index]
            n = n + 1
        self.result = result

    def calculate_index(self, i2, i1):
        print 'something write for child class.'
        exit()
        return

    def display(self):
        print self.result
        return

class EncVigenere(Vigenere):
    def __init__(self):
        super(Vigenere, self).__init__()
        self.result = ''
        self.cycle = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_'
        return

    def calculate_index(self, i1, i2):
        return i2 + i1

class DecVigenere(Vigenere):
    def __init__(self):
        super(Vigenere, self).__init__()
        self.result = ''
        self.cycle = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_'
        return

    def calculate_index(self, i1, i2):
        return i2 - i1

def main():
    target = 'There are four pencils in the pencil case.'.upper()
    print target
    key = 'FLAG{CTF_FINDKEY}'.upper()
    print key

    enc_vigenere = EncVigenere()
    enc_vigenere.execution(target, key)
    enc_vigenere.display()

    dec_vigenere = DecVigenere()
    dec_vigenere.execution(enc_vigenere.result, key)
    dec_vigenere.display()

main()
