# [DOCS]
# https://docs.python.jp/3/library/codecs.html
# rot暗号を解くためのスクリプト
import codecs
import sys

argv = sys.argv

if (len(argv) != 2):
    print('Argument is less. Please add char')
    exit()

enc = argv[1]
print(codecs.decode(enc, 'rot13')) # rot13 is Ceaser encryption.
