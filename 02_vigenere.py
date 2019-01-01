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

class vigenere:
    def __init__(self):


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
