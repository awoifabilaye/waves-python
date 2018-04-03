#!/usr/bin/python
# -*- coding: utf-8 -*-

#facilisimoDeveloper: roberto

import pywaves as pw
import base58


pw.setChain(chain='L')
newAddress = pw.Address()

encodeSeed = base58.b58encode(newAddress.seed.encode('utf-8'))

print "---Wallet encoded seed---"
print encodeSeed
print ""
print "---data Address---"
print newAddress
