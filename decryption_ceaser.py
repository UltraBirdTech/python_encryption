# [DOCS]
# rot暗号を解くためのスクリプト
import codecs
import sys

argv = sys.argv

if (len(argv) != 2):
    print('Argument is less. Please add char and rot num.')
    exit()

enc = argv[1]
for num in range(1,26):
    answer = ''
    for letter in enc:
        answer += chr(ord('A') + (ord(letter)-ord('A')-int(num)) % 26)
    print(str(num) + ': ' + answer)
