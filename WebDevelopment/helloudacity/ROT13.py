#!/usr/bin/env python

import string

def Rot13( str ):
   rot13 = string.maketrans( 
       "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
           "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
   return string.translate( str, rot13)

if __name__ == "__main__":
    print Rot13( 'HELLO' )
    print Rot13( 'HELLO *1adfas@' )
    print Rot13( 'HELLO if' )

