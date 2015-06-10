#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Legion could add numbers to its name if its usual is occupied
#or you could give it some alternate names

import tarotmodule
import runesmodule
#import denshijisho
import ast
import glob
#chr(3)+"1,10abcdef"+chr(3)+"defabc"
#The first number is foreground, black, the second number is background, teal
#Starting at 0, the colors are: White, Black, Blue, Green, Pink, Red, Purple, Brown, Orange, Light Green, Teal,
#Turquoise, Light Blue, Magenta, Dark Grey, and Light Grey
#gold=unicode(gold, "latin-1")
#to quickly decode and encode to something?
#sync
import select
from traceback import print_exc, format_exc
import socket
import lxml.html
from lxml.html.clean import clean_html
import urllib.request, urllib.parse, urllib.error
import copy
#import cookielib
#cj = cookielib.CookieJar()
opener = urllib.request.build_opener()#urllib2.HTTPCookieProcessor(cj))
#opener.addheaders = [('User-agent', 'Mozilla/5.0')]
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0')]
#Host: show-ip.net
#User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0
#Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
#Accept-Language: en-us,en;q=0.5
#Accept-Encoding: gzip, deflate
#Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
#DNT: 1
#Connection: keep-alive
opener.addheaders = [('Accept', 'text/html')]
opener.addheaders = [('Accept', 'iso-8859-1')]
#opener.addheaders.append(('Cookie', 'YPF8827340282Jdskjhfiw_928937459182JAX666'))
import httplib2
import re
import sys
import os

import time
if sys.platform == "win32":
# On Windows, the best timer is time.clock()
	timer = time.clock
else:
# On most other platforms the best timer is time.time()
	timer = time.time

global quotedatabasefilename
quotedatabasefilename="legionquotes.txt"

import json
#import xml.etree.ElementTree as ET

import chardet

import html.entities
import random
random.seed()

numberfind=re.compile("\d+\.?\d*")
#add https support
#urlfind=re.compile(".*?(https?://(?:[^\s\r\n\[\]\{\}\(\)\'\"]+/?)).*?")

tlds=[x.rstrip("\n") for x in open("tlds.txt").readlines() if (x.count("#"))==0]
tlds.sort(key=lambda x:-len(x))
urlfind=re.compile("((?:(?:https|http)://)?(?:[\w-]+?\.)+(?:%s)(?:/[\S.\-%%&?=]*)*)(?:[^\w-]|$)" % ("|".join(tlds)).lower())
has_protocol=re.compile("((?:https|http)+://)")	
#urlcatcher=compile("((?:(?:https|http)://)?(?:[\w-]+?\.)+(?:%s)(?:/[\S.\-%%&?=]*)*)" % ("|".join(tlds)).lower())

#urlfinders = [re.compile("([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}|(((news|telnet|nttp|file|http|ftp|https)://)|(www|ftp)[-A-Za-z0-9]*\\.)[-A-Za-z0-9\\.]+)(:[0-9]*)?/[-A-Za-z0-9_\\$\\.\\+\\!\\*\\(\\),;:@&=\\?/~\\#\\%]*[^]'\\.}>\\),\\\"]"),
#re.compile("([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}|(((news|telnet|nttp|file|http|ftp|https)://)|(www|ftp)[-A-Za-z0-9]*\\.)[-A-Za-z0-9\\.]+)(:[0-9]*)?"),
#re.compile("(~/|/|\\./)([-A-Za-z0-9_\\$\\.\\+\\!\\*\\(\\),;:@&=\\?/~\\#\\%]|\\\\)+"),
#re.compile("'\\<((mailto:)|)[-A-Za-z0-9\\.]+@[-A-Za-z0-9\\.]+")]

#able to change the name of the config file? not just making it a configglefile

#chr(3)+"1,10abcdef"+chr(3)+"defabc"
#The first number is foreground, black, the second number is background, teal
#Starting at 0, the colors are: White, Black, Blue, Green, Pink, Red, Purple, Brown, Orange, Light Green, Teal,
#Turquoise, Light Blue, Magenta, Dark Grey, and Light Grey

from math import ceil


#from legionstandardlibrary import *
#from legion import legionconfig

global legionconfig

with open("legionstandardlibrary.py") as f:
    code = compile(f.read(), "legionstandardlibrary.py", 'exec')
    exec(code)
f.close()

global commands
commands=[]

#make this yet more modular, modify legionscript.sh so
#python legion.py --modules legionbonuscommands legionlaucommands
#main should be loaded by default

#legc.py is the string for a module
#legionmaincommands.legc.py
for i in glob.glob("*.legc.py"):
	
	with open(i) as f:
	    code = compile(f.read(), i, 'exec')
	    exec(code)
	f.close()



for command in Command.__subclasses__():
	#comm=command()
	commands.append(command())


#list for storing games, max?

#def pickasinglenick(userlist, nickstoremove=[]):

try:
	cool=sys.argv[1]
	global legionconfig
	legionconfigfile=open(sys.argv[1], "r")
	legionconfig=ast.literal_eval(legionconfigfile.read())
	legionconfigfile.close()
except:
	input("Please specify a config file, or make one with makelegionconfig.py!")
	sys.exit()


for i in legionconfig.keys():
	#legionconfig[network]=[legionname, #0
	#legionoperator, #1
	#port, #2
	#chanlist, #3
	#password] #4
	legionconfig[i].append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))#5, myconnection
	legionconfig[i].append(0)#6 amionyet
	legionconfig[i].append({})#7 userdictlist
	legionconfig[i].append([])#8, guessinggames
	legionconfig[i].append([])#9 tarotspreads
	legionconfig[i].append([])#10 runespreads
	legionconfig[i].append(0)#11 kickcount, networkwide

#myconnection.connect((network, port))
#legionconfig[i][4].connect((networklegionconfig[i], legionconfig[i][2]))

socket.setdefaulttimeout(600)
whattoping="legionping"

#amionyet=0

def logon(network):
	if legionconfig[network][6]==0:
		print("Just a moment, connecting to "+network+"...")
		time.sleep(3)
		legionconfig[network][5].send(bytesgoutf8("NICK "+legionconfig[network][0]+"\r\n" ))
		legionconfig[network][5].send(bytesgoutf8("USER "+legionconfig[network][0]+" "+legionconfig[network][0]+" "+legionconfig[network][0]+" :The Bot from Hell\r\n" ))
#		for chan in legionconfig[network][3]:	
#			legionconfig[network][5].send(bytesgoutf8("JOIN #"+chan+"\r\n" ))
		legionconfig[network][5].setblocking(0)

#logon()
userliststorage=""
channellookingoutfor=""
networksleft=[]
rejoinnetworksleft=[]
while True:
	if rejoinnetworksleft:
		for i in rejoinnetworksleft:
			del legionconfig[i]
			logon(i)
	rejoinnetworksleft=[]
	if networksleft:
		for i in networksleft:
			del legionconfig[i]
		networksleft=[]
	for network in legionconfig.keys():
		if not legionconfig[network][6]:
			legionconfig[network][5].connect((network, legionconfig[network][2]))
			while legionconfig[network][6]==0:

				data=""
				ready = select.select([legionconfig[network][5]], [], [], 5)
				if ready[0]:
					data = legionconfig[network][5].recv ( 4096 )
					try:
						data=data.decode("utf-8")
					except:
						try:
							data=str(data)
						except:
							print_exc()
					data=data.strip("\r\n")
					data=data.strip("\n")
					data=data.strip()
				if not data:
					if whattoping!="" and len(legionconfig[network][8]):
						legionconfig[network][5].send(bytesgoutf8("PING " + whattoping + "\r\n" )) #lag!
				print(data)
				if "Found your hostname" in data or "using your IP address instead" in data:
					legionconfig[network][5].setblocking(1)
					logon(network)
				if " 376 "+legionconfig[network][0]+" :" in data:
					if legionconfig[network][4]:
						legionconfig[network][5].send(bytesgoutf8("IDENTIFY "+legionconfig[network][4]+"\r\n"))
					for chan in legionconfig[network][3]:
						legionconfig[network][5].send(bytesgoutf8("JOIN #"+chan+"\r\n"))
					legionconfig[network][6]=1
					#if a netsplit happens, set it to 0 again?
				if "PONG" not in data and "PING" not in data and data!="" and len(data)>1:# or len(guessinggames) and "PONG" in data:
					print(data)
				if data.find ( "PING" ) != -1:
					legionconfig[network][5].send(bytesgoutf8("PONG "+data.split()[1]+"\r\n"))
					if whattoping=="":
						whattoping=data.split() [ 1 ]
	
		datad=""
		datas=[]
		ready = select.select([legionconfig[network][5]], [], [], 5)
		if ready[0]:
			if legionconfig[network][8]:
				legionconfig[network][5].send(bytesgoutf8("PING " + whattoping + "\r\n" ))
			#if there are games afoot, ping
			datad = legionconfig[network][5].recv ( 4096 )
			try:
				datad = datad.decode("utf-8")
			except:
				datad = datad.decode("latin-1")
			datad=datad.strip("\r\n")
			datad=datad.strip("\n")
			datad=datad.rstrip()
			if "\r\n" in datad:
				datas=datad.split("\r\n")
			elif "\n" in datad:
				datas=datad.split("\n")
			else:
				datas=[datad]
		for data in datas:
			checkagain=0
			if not data:
				if whattoping!="" and len(legionconfig[network][8]):
					legionconfig[network][5].send(bytesgoutf8("PING "+whattoping+"\r\n")) #lag!
		
			#if "Found your hostname" in data and amionyet==0:
				#myconnection.setblocking(1)
				#logon()
			#if " 376 "+legionname+" :" in data:
				#for chan in chanlist:	
					#myconnection.send(bytesgoutf8("JOIN #"+chan+"\r\n" ))
				#amionyet=1
				#if a netsplit happens, set it to 0 again?
			if "PONG" not in data and "PING" not in data and data!="":# or len(guessinggames) and "PONG" in data:
				print(data)
			if data.find ( "PING" ) != -1:
				legionconfig[network][5].send(bytesgoutf8("PONG "+data.split()[1]+"\r\n"))
				if whattoping=="":
					whattoping=data.split()[1]
			if " 333 " in data or ":"+legionconfig[network][0]+"!~" in data.split(" ")[0] and " JOIN :#" in data.split(":"+legionconfig[network][0]+"!~")[1]:
				if "333" in data or checkagain==1 and " 366 " not in data and " 332 " not in data:
					try:
						channellookingoutfor=data.split(" 333 "+legionconfig[network][0]+" ")[1].split(" ")[0]
						checkagain=0
					except:
						checkagain=1
				else:
					channellookingoutfor=data.split(" JOIN :")[1].rstrip()
			if " 353 " in data and channellookingoutfor:
				#try:
				#	userliststorage+=data.split(":")[2]
				userliststorage+=data.split(":")[-1]
				#except:
				#	userliststorage+=data.split(":")[1]
#				print("We're gonna talk to you all at a glance of the eye")
			if channellookingoutfor and " 333 " not in data and " 353 " not in data and " 366 " not in data and " 332 " not in data and "End of /NAMES list." not in data and len(userliststorage):
				userliststorage+=data.rstrip()
			if " 366 " in data and channellookingoutfor:
				#totally overwrite any current userlists
				userliststorage=userliststorage.replace("+", "")
				userliststorage=userliststorage.replace("&", "")
				userliststorage=userliststorage.replace("@", "")
				userliststorage=userliststorage.replace("~", "")
				userliststorage=userliststorage.replace("%", "")
				userliststorage=userliststorage.replace("= ", "")
				userliststorage=userliststorage.replace(" =", "")
				userliststorage=userliststorage.replace(" . ", " ")
				userliststorage=userliststorage.rstrip()
				if " " in userliststorage:
					legionconfig[network][7][channellookingoutfor]=userliststorage.split(" ")
				else:
					legionconfig[network][7][channellookingoutfor]=[userliststorage]
				print((legionconfig[network][7][channellookingoutfor]))
				channellookingoutfor=""
				userliststorage=""
				
				
			if data.find(" NICK :")!=-1:
				#wrap these up in try accept
				whothat, newnick=data.split(" NICK :")
				newnick=newnick.rstrip()
				whothat=nickanick(whothat)
				if whothat==legionconfig[network][1]:
					legionconfig[network][1]=newnick
				for game in legionconfig[network][8]:
					if game.asker==whothat:
						game.asker=newnick

				for keyofchan in list(legionconfig[network][7].keys()):
					for rrr in range(0, len(legionconfig[network][7][keyofchan])):
						if legionconfig[network][7][keyofchan][rrr]==whothat:
							legionconfig[network][7][keyofchan][rrr]=newnick
#after the quits and joins, print(the modified user lists, to make sure it's working
			if data.find(" QUIT :")!=-1:
				#wrap these up in try accept
				whothat=nickanick(data)
				for game in legionconfig[network][8]:
					if game.asker==whothat:
						gamestodel.append(game)

				for keyofchan in list(legionconfig[network][7].keys()):
					wehaveanumber="sentry"
					for rrr in range(0, len(legionconfig[network][7][keyofchan])):
						if legionconfig[network][7][keyofchan][rrr]==whothat:
							wehaveanumber=rrr
							break
					if wehaveanumber!="sentry":
						del legionconfig[network][7][keyofchan][rrr]
			
			if data.find ( " PART #") != -1:
				if data.split(":")[1].find ( " PART #") != -1:
					thechan=nickachan(data)
					theguy=nickanick(data)
					try:
						where=legionconfig[network][7][thechan].index(theguy)
						del legionconfig[network][7][thechan][where]
					except:
						pass
					
			if data.find ( " JOIN #") != -1:
				if data.split(":")[1].find ( " JOIN #") != -1 and nickanick(data)!=legionconfig[network][0]:
					thechan=nickachan(data)#thechan="#"+data.split(":")[1].split( " JOIN #")[1].split(" ")[0].rstrip()
					theguy=nickanick(data)
					legionconfig[network][7][thechan].append(theguy)

				
			if data.find ( " KICK #") != -1:
				if data.find ( " "+legionconfig[network][0]+" :") != -1:#and it's Legion
					kickedchan=data.split(" KICK #")[1]
					kickedchan=kickedchan.split(" "+legionconfig[network][0]+" :")[0]
					legionconfig[network][5].send(bytesgoutf8("JOIN #"+kickedchan+"\r\n"))
			else:
				if "KICK" in data.split(":")[0]:
					thechan=data.split(":")[0].split(" KICK ")[1].split(" ")[0]
					theguy=data.split(":")[0].split(" KICK ")[1].split(" ")[1]
					
					where=legionconfig[network][7][thechan].index(theguy)
					del legionconfig[network][7][thechan][where]


			if "ERROR :Closing Link: "+legionconfig[network][0] in data and "(Ping timeout: " in data:
				rejoinnetworksleft.append(network)
				

			if commandcheck(data, legionconfig[network][0].lower()+" quit", network):

				cleanuser=nickanick(data)
				if cleanuser.lower()==legionconfig[network][1].lower() or cleanuser.lower()=="starscream":
					#send to each channel
					for net in legionconfig.keys():
						for ch in legionconfig[net][3]:
							legionconfig[net][5].send(bytesgoutf8("PRIVMSG #"+ch+" :じゃ、またね！\r\n" ))
							if net!=network:
								legionconfig[net][5].send(bytesgoutf8("QUIT Leaving every network.\r\n"))
					legionconfig[network][5].send(bytesgoutf8("QUIT Leaving every network.\r\n"))
					#quit every network but this one?
					sys.exit()
				else:
					sendastringtowho(("You are not my master, "+cleanuser+". I refuse to obey your wishes."), data, network)
			if commandcheck(data, legionconfig[network][0].lower()+" reload", network):

				cleanuser=nickanick(data)
				if cleanuser.lower()==legionconfig[network][1].lower():
					sendastringtowho(("Reloading command modules."), data, network)
					oldcommandnames=[]
					oldcommands=copy.deepcopy(commands)
					for o in oldcommands:
						#oldcommandnames.append(o.__class__.__name__)
						oldcommandnames.append(o.__class__.__name__)
					for i in glob.glob("*.legc.py"):
						
						with open(i) as f:
						    code = compile(f.read(), i, 'exec')
						    exec(code)
						f.close()
					#global commands
					thecommands=[]
					for command in Command.__subclasses__():
						#check against names in use
						#they should be basically the same
						#erk, how will I know the newest subclass will be loaded?
						#I'm banking that it's a list and not a dict, so it will be in the order I loaded them
						#it appears to be in order, first complaint was Calc
						if command.__name__ in oldcommandnames:
							#print(command.__name__, "is already in oldcommands")
							#get the index number
							theindex=oldcommandnames.index(command.__name__)
							oldcommands[theindex]=command()
							
							#1, 3, 6
							#old
							#old new old
							#old new new old new old
						else:
							#print(command.__name__, "is brand new")
							thecommands.append(command())
					#global commands
					commands=oldcommands+thecommands
					
				else:
					sendastringtowho(("You are not my master, "+cleanuser+". I refuse to obey your wishes."), data, network)
			if commandcheck(data, legionconfig[network][0].lower()+" leavenetwork", network):
#				if data.lower().find ( ":!"+legionconfig[network][0].lower()+" quit" ) != -1:
				cleanuser=nickanick(data)
				if cleanuser.lower()==legionconfig[network][1].lower():
					#send to each channel
					for ch in legionconfig[network][3]:
						legionconfig[network][5].send(bytesgoutf8("PRIVMSG #"+ch+" :じゃ、またね！\r\n" ))
							
					legionconfig[network][5].send(bytesgoutf8("QUIT Leaving this network.\r\n"))
					networksleft.append(network)
					continue
				else:
					sendastringtowho(("You are not my master, "+cleanuser+". I refuse to obey your wishes."), data, network)


			if commandcheck(data, "guessthattrope", network) or commandcheck(data, "whosthatpokemon", network):
				numberofquestions=1
				taken=0
				tags=""
				datadyne=data
				gamer=""
				for chan in legionconfig[network][3]:
					if datadyne.split("PRIVMSG ")[1].split(" :")[0]=="#"+chan:
						gamer="#"+chan
						break
				if not gamer:
					gamer=nickanick(datadyne)
				if "guessthattrope" in data:
					tags=datadyne.lower().split("!guessthattrope")[1].lstrip().rstrip()
					agameof="Guess That Trope"
				elif "whosthatpokemon" in data:
					tags=datadyne.lower().split("!whosthatpokemon")[1].lstrip().rstrip()
					agameof="Who's That Pokemon"
				taken=0
				if tags:
					if "stop" in tags:					
						#find the game with the gamer as the asker, and kill it, set it to done
						thedelgame=None
						for game in legionconfig[network][8]:
							if game.asker==gamer:
								if agameof=="Who's That Pokemon" and game.game=="pokemon" or agameof=="Guess That Trope" and game.game=="trope":
		#							game.done=1
		#							game.numberofquestions=0
									thedelgame=game
									break
						
						if thedelgame:
							taken=1
							del legionconfig[network][8][legionconfig[network][8].index(thedelgame)]
							legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+gamer+" :Game of "+agameof+" stopped.\r\n"))
		
				
				for game in legionconfig[network][8]:
					if game.asker==gamer:
						if game.game=="pokemon" and agameof=="Who's That Pokemon" or game.game=="trope" and agameof=="Guess That Trope":
							taken=1
							break
						
				if taken==0 and len(legionconfig[network][8])<5:
					if tags:
						
						foundnumber=numberfind.findall(tags)
						try:
							numberofquestions=int(foundnumber[0])
							if numberofquestions<1:
								numberofquestions=1
							elif numberofquestions>10:
								numberofquestions=10
						except:
							numberofquestions=1
				#if there's no game with gamer as the asker
					else:
						numberofquestions=1
					adexentrymaybe=""
					if agameof=="Guess That Trope":
						agametoplay="trope"
						toguess=asktrope(gamer)
						
					elif agameof=="Who's That Pokemon":
						agametoplay="pokemon"
						toguess, adexentrymaybe=getapokemon(gamer)
					legionconfig[network][8].append(GuessingGame(toguess, numberofquestions, gamer, agametoplay, adexentrymaybe))
			gamestodel=[]	
			for game in legionconfig[network][8]:
				#print(chardet.detect(data)["encoding"],type(data))
				try:
					gold=data.split(" :")[1].strip()
				except:
					gold=data.strip()
				#gold=str(gold)#.encode("latin-1")
				gold=bytesgoutf8(gold).decode("utf-8")
				#take care of games that have
				if game.guessthis=="" and game.numberofquestions>0:
					game.another()
				if gold.lower().find ( game.guessthis.lower() ) != -1 and int(timer() - game.timestart)<240 and game.asker in data and game.done==0:
					if game.game=="trope" or game.game=="pokemon" and not gold.lower().replace(game.guessthis.lower(), "").rstrip():
						nowitis=(timer() - game.timestart)
						#cleanuser=data.split("PRIVMSG")[0]
						cleanuser=nickanick(data)
						#if we have the game.asker and it's not the mainchat, make sure that it's a PM to Legion
						if game.game=="pokemon":
							tackmeon="Pokémon"
						elif game.game=="trope":
							tackmeon="trope"
						legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+game.asker+" :Well done, "+cleanuser+"! "+game.guessthis+" was the "+tackmeon+".\r\n" ))
						grade=int((game.thehint.count("_")/(game.originalhint.count("_")*1.0)*50)+int(((240-int(nowitis))/240.0)*50))
						legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+game.asker+" :Your grade was "+str(grade)+"%.\r\n" ))
						if game.game=="pokemon":
							addscoretoscoreboard(cleanuser, "Who's That Pokémon?")
						elif game.game=="trope":
							addscoretoscoreboard(cleanuser, "Guess That Trope")
			
						game.numberofquestions-=1
						print(game.numberofquestions,"questions left")
						if game.numberofquestions<=0:
							gamestodel.append(game)
							game.done=1					
						else:
							game.another()
				
				if "!pokemonhint" in data.lower() and game.game=="pokemon" or "!tropehint" in data.lower() and game.game=="trope":
					
					if int(timer() - game.timestart)<240 and game.asker in data and game.done==0 and game.guessthis!="":
		
						testforit=""
						if "!tropehint" in data.lower():
							testforit=commandcheck(data, "tropehint", network)
						elif "!pokemonhint" in data.lower():
							testforit=commandcheck(data, "pokemonhint", network)
						if testforit:
						#check if game.asker is in the data before proceeding
							cleanuser=data.split("PRIVMSG")[0]
							cleanuser=nickanick(cleanuser)
							if "#" in game.asker and testforit==2 or game.asker==cleanuser and testforit==1:
								print(str(int(timer() - game.timestart)),"seconds have passed")
								
								#less than 10, but once you're had both PokeDex entries
								#total hints will be 1
								#first hint is a PokeDex entry
								#or make sure that at least 20% of thehint is still _s#
								if game.totalhints<10 and game.thehint.count("_")>int(game.originalhint.count("_")*.2):
									if "!pokemonhint" in data:
										if game.totalhints==0:
											ahintforyou=game.dexentry.encode("utf-8")
										else:
											if game.totalhints==1:
												pass
											elif game.totalhints>1 and game.totalhints<10:
												howmany=game.countthis
												
												while howmany:
													eee=random.randrange(0, len(game.thehint))
													if game.thehint[eee]=="_":
														game.thehint=game.thehint[:eee]+game.guessthis[eee]+game.thehint[eee+1:]
														howmany-=1
											ahintforyou=game.thehint
									elif "!tropehint" in data:
										if game.totalhints==0:
											pass
										elif game.totalhints>0 and game.totalhints<10:
											howmany=game.countthis
											
											while howmany:
												eee=random.randrange(0, len(game.thehint))
												if game.thehint[eee]=="_":									
													game.thehint=game.thehint[:eee]+game.guessthis[eee]+game.thehint[eee+1:]
													howmany-=1
										ahintforyou=game.thehint
									try:
										legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+game.asker+" :Here's a hint: ")+ahintforyou.encode("latin-1")+bytesgoutf8("\r\n") )
									except:
										legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+game.asker+" :Here's a hint: ")+ahintforyou+bytesgoutf8("\r\n" ))
									game.totalhints+=1
									
								else:
									try:
										legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+game.asker+" :Here's the last hint you got:  ")+ahintforyou.encode("latin-1")+bytesgoutf8("\r\n") )
									except:
										legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+game.asker+" :Here's the last hint you got: ")+ahintforyou+bytesgoutf8("\r\n" ))
		#						game.totalhints+=1
							
		
				elif int(timer() - game.timestart)>=240 and game.done==0 and game.guessthis!="":
					legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+game.asker+" :Time's up! The answer was: ")+game.guessthis.encode("latin-1")+bytesgoutf8("\r\n" ))
					game.numberofquestions-=1
					print((game.numberofquestions,"questions left"))
					if game.numberofquestions==0:
						game.done=1
						gamestodel.append(game)
					else:
						game.guessthis=""
		
			for g in gamestodel:
				del legionconfig[network][8][legionconfig[network][8].index(g)]
			gamestodel=[]
			spreadstodel=[]
			caststodel=[]
			for spread in legionconfig[network][9]:
				for line in spread[1].actualspread:
					if len(line)>400:
						cf= lambda s,p: [ s[i:i+p] for i in range(0,len(s),p) ]
						choppedline=cf(line, 400)
						for x in choppedline:
							legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+spread[0]+" :"+x+"\r\n"))
					else:
						legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+spread[0]+" :"+line+"\r\n"))
				spreadstodel.append(spread)
			for s in spreadstodel:
				del legionconfig[network][9][legionconfig[network][9].index(s)]
			spreadstodel=[]
			for cast in legionconfig[network][10]:
				for line in cast[1].actualcast:
					if len(line)>400:
						cf= lambda s,p: [ s[i:i+p] for i in range(0,len(s),p) ]
						choppedline=cf(line, 400)
						for x in choppedline:
							legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+cast[0]+" :"+x+"\r\n"))
					else:
						legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+cast[0]+" :"+line+"\r\n"))
				caststodel.append(cast)
			for c in caststodel:
				del legionconfig[network][10][legionconfig[network][10].index(c)]
			caststodel=[]
			if chr(1) in data:
				ctcp=data.split(chr(1))[1]
				if ctcp=="USERINFO":
					legionconfig[network][5].send(bytesgoutf8("NOTICE "+nickanick(data)+" :My name is Legion, for we are many.\r\n"))

				elif ctcp=="TIME":
					legionconfig[network][5].send(bytesgoutf8("NOTICE "+nickanick(data)+" :In the current body that houses Legion, the time is... "+time.strftime("%Y-%m-%d %H:%M:%S")+"\r\n"))
			#The hearts and souls of Legion...
			for command in commands:
				command.check(network, data)
				
#!joinanetwork blah.net -permanent -password blah
