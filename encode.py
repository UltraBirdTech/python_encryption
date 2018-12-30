# [DOCS]
# https://docs.python.jp/3/library/codecs.html
import codecs

enc = "Pnrfne SYNT{PGS_Rnfl}"
print codecs.decode(enc, 'rot13') # rot13 is seaser encryption.
