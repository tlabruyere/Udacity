#!/usr/bin/env python

import string

def Rot13( str ):
   rot13 = string.maketrans( 
       "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
           "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
   return string.translate( str, rot13)

print Rot13( 'HELLO' )

