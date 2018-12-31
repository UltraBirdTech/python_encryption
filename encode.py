# [DOCS]
# https://docs.python.jp/3/library/codecs.html
import codecs
import sys

argv = sys.argv

if (len(argv) != 2):
    print 'Argument is less. Please add char'
    exit()

enc = argv[1]
print codecs.decode(enc, 'rot13') # rot13 is seaser encryption.
