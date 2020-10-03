# [DOCS]
# https://docs.python.jp/3/library/codecs.html
# rot暗号を解くためのスクリプト
import codecs
import sys

argv = sys.argv

if (len(argv) != 3):
    print('Argument is less. Please add char and rot num.')
    exit()

enc = argv[1]
rot_num = argv[2]
answer = ''
for letter in enc:
    answer += chr(ord('A') + (ord(letter)-ord('A')+int(rot_num)) % 26)
print(answer)
