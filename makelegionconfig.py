#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
legionconf={}

networknumber=input("Please enter the number of networks you want Legion to join.\n")
try:
	networknumber=int(networknumber)
except:
	networknumber=1
for j in range(0, networknumber):
	network=input("Please enter the name of a network you want Legion to connect to.\n")
	legionname=input("Please enter the name you want Legion to have on this network.\n")
	legionoperator=input("Please enter the nickname of the user you want Legion to answer to on this network.\n")
	
	port=input("Please enter the name of the port you want Legion to connect to this network through.\n")
	try:
		port=int(port)
	except:
		port=6667
	numberoftimes=input("Please enter the number of channels you want Legion to join on this network.\n")
	try:
		numberoftimes=int(numberoftimes)
	except:
		numberoftimes=1
	chanlist=[]
	for i in range(0, numberoftimes):
		c=input("Channel name? (no # needed)\n")
		chanlist.append(c)
	password=input("If Legion is registered, what is its password? Otherwise, leave this space blank.\n")
	legionconf[network]=[legionname, legionoperator, port, chanlist, password]

config=open("legionconfig", "w")
config.write(repr(legionconf))
config.close()
