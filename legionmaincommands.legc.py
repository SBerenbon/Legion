class URLChecker(Command):
	def __init__(self):
		Command.__init__(self, [" "], 1)
	def check(self, network, data):
		if data.find("PRIVMSG ")!=-1 and "#astral_observatory" not in data and "#fluffington" not in data.lower() and nickanick(data) and nickanick(data).lower()!="dragobot" and nickanick(data)!="esting12345" and nickanick(data).lower()!="bitrelaybot":
			#data.find("PRIVMSG #")!=-1 or data.find("PRIVMSG "+legionconfig[network][0])!=-1:
			checktheurlplease=0
			if nickachan(data):
	
				if nickachan(data) in legionconfig[network][7]:
					if nickachan(data) in legionconfig[network][7] and not "bot" in legionconfig[network][7][nickachan(data)] and not "aigis" in legionconfig[network][7][nickachan(data)] and not "Bot" in legionconfig[network][7][nickachan(data)] and not "Aigis" in legionconfig[network][7][nickachan(data)] and not "Misaka" in legionconfig[network][7][nickachan(data)] and not "misaka" in legionconfig[network][7][nickachan(data)] or nickachan(data)=="":
						checktheurlplease=1
					else:
						checktheurlplease=0
			else:
				checktheurlplease=1
			if checktheurlplease==1:
				
				if nickachan(data)=="":
					recipient=nickanick(data)
				else:
					recipient=nickachan(data)
				self.action(network, recipient, data)

	def action(self, network, recipient, data):
		#pool=""
		#join fuses the list elements together in one string, the connector being...the thing before .join
		#split's opposite, joins, with the specified char as a connector
#		("((?:https|http)+://)")
		pool=str(":".join(data.split(":")[2:]))
		listoflinks=[]
		listoflinks=urlfind.findall(pool)
		
		#remove dupes
		if listoflinks:
			wearephonies=[]
			for i in listoflinks:
				if ".jpg" in i:#or, if there's an extension and it ain't html
					if i.split(".jpg")[1]=="":
						
						wearephonies.append(i)
			for i in wearephonies:
				del listoflinks[listoflinks.index(i)]

			for i in listoflinks:
				if not has_protocol.match(i): i="http://"+i
				try:
					if "youtu.be" in i:
						videoroot=i.split("youtu.be/")[1]
						i="http://www.youtube.com/watch?v="+videoroot
					elif "tinyurl.com" in i:
						linkroot=i.split("tinyurl.com/")[1]
						newlink="http://tinyurl.com/preview.php?num="+linkroot
						pagette=opener.open(newlink).read().decode("utf-8").split("\n")
						somelink=""
						for lineline in pagette:
							if "redirecturl" in lineline:
								firstpart=lineline.split("<p><b><a id=\"redirecturl\" href=\"")[1]
								i=firstpart.split("\">Proceed to this site.</a></b></p>")[0]
				except:
					pass
				dataplease=""
				try:
					h = httplib2.Http(timeout=1)
					#set timeout for this sucker?
					try:
						#remove body=" ", that's there for Google search pages compatibility
						try:
							resp = h.request(i, "HEAD", body=" ", headers={'Accept':'text/html', 'Accept':'iso-8859-1', 'User-agent':'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0'})[0]
						except:
							resp = h.request(i, "HEAD")[0]
						if "text/html" in resp["content-type"] and resp["status"] != "403" and resp["status"] != "406":
							if resp["status"] and not i.lower().startswith("http://irc."):# == "200" or resp["status"] == "405":

								#i=i.split("#")[0]
								try:
									pageme=opener.open(i)#, data=" ")
								except:
									pageme=urllib.request.urlopen(i)
								pager=pageme.read()
								try:
									pager=pager.decode("utf-8")
								except:
									pager=pager.decode("latin-1")
								if "</TITLE>" in pager:
									item=pager.split("</TITLE>")[0]
								else:
									item=pager.split("</title>")[0]
								if "<TITLE>" in item:
									dataplease=str(item.split("<TITLE>")[1])
									
								else:
									if "<title>" in item:
										dataplease=str(item.split("<title>")[1])
									else:
										raise ValueError('No title tag, what a shame')
								dataplease=dataplease.replace("   &"," &")
								dataplease=dataplease.replace("  &"," &")
								#reg = re.compile("\\\\[u]([0-9a-f]{4})", re.I | re.S)
								#dataplease = reg.sub(lambda m: chr(int(m.group(1).lstrip(), 16)), dataplease)
								#print(chardet.detect(pager)["encoding"])
								#find its encoding, and decode?
								try:
									dataplease=dataplease.decode("utf-8")
								except:
									pass
								try:
									dataplease=dataplease.replace("Main/", "")
								except:
									pass
								try:
									dataplease=unescape(dataplease)
								except:
									dataplease=dataplease.replace(" - Television Tropes &amp; Idioms"," - Television Tropes & Idioms")
									dataplease=dataplease.replace(" - Television Tropes &AMP; Idioms"," - Television Tropes & Idioms")
									pass
								try:
									if chardet.detect(pager)["encoding"]=="SHIFT_JIS":
										dataplease = str(dataplease, 'shiftjis')
									dataplease=dataplease.encode("utf-8")
								except:
									pass
								#dataplease=urllib2.unquote(dataplease)
								if "youtube.com" in i and "v=" in i:
									#dataplease=str(dataplease.replace("    YouTube\n        - ",""))
									dataplease=dataplease.replace("\n", "")
									dataplease=dataplease.replace("      - YouTube", " - YouTube")
									dataplease=dataplease.lstrip()
									dataplease=dataplease.rstrip()
									dataplease=dataplease.replace(" - YouTube", "")
									views=""
									uploader=""
									uploaddate=""
									likespercent=""
									dislikespercent=""
									baseofthelik=""
									likes=""
									dislikes=""
									comments=""
									try:
										views=pager.split("stat view-count")[1].split(">")[1].split(" views")[0].replace(",", "")
									except:
										pass
									try:
										try:
											uploader=pager.split("http://schema.org/Person")[1].split("http://www.youtube.com/user/")[1].split(">")[0].replace("\"", "").replace("'", "")
										except:
											pass#uploader=pager.split("Published on <span id=\"eow-date\"")[1].split("<a href=\"/user/")[1].split("\"")[0]
									except:
										pass
									try:
										uploaddate=pager.split("datePublished")[1].split(" content=")[1].split(">")[0].replace("\"", "").replace("'", "")
									except:
										pass
									try:
										likespercent=str(round(float((pager.split("video-extras-sparkbar-likes")[1].split("width: ")[1].split("%")[0] )), 2))
									except:
										pass
									try:
										dislikespercent=str(round(float((pager.split("video-extras-sparkbar-dislikes")[1].split("width: ")[1].split("%")[0] )), 2))
									except:
										pass
									try:
										likesbase=pager.split("watch-like-dislike-buttons")[1].split("like this video along with ")[1:]
										likes=likesbase[0].split(" other people")[0].replace(",", "")
										dislikes=likesbase[1].split(" other people")[0].replace(",", "")
									except:
										pass
									try:
										comments=pager.split("interactionCount")[1].split(" content=")[1].split(">")[0].replace("\"", "").replace("'", "")
									except:
										pass

									dataplease="Title: "+dataplease
									if views:
										dataplease+=" - Views: "+views
									if likes:
										dataplease+=" Likes: "+likes+" ("+likespercent+"%)"
									if dislikes:
										dataplease+=" Dislikes: "+dislikes+" ("+dislikespercent+"%)"
									if comments:
										dataplease+=" Comments: "+comments
									if uploader:
										dataplease+=" Uploaded by: "+uploader+" On: "+uploaddate
									sendastringtowho(str(dataplease), data, network)

									#sendastringtowho("YouTube Video: %s\r\n' % str(dataplease), data, network)
								else:
									dataplease=dataplease.lstrip().rstrip().replace("\r\n    ", " ").replace("\n    ", " ").replace("\r\n", "").replace("\n", "").replace("							", " ").replace("\t", "").replace("  ", " ")
									dataplease=dataplease.replace("&eacute;", "é").replace("&apos;", "'")
									if "Incompatible Browser | Facebook" not in dataplease:
										sendastringtowho("URL Title: "+str(dataplease), data, network)
							else:
								#print(resp['status'],"and",resp['content-type'])
								#print_exc()
								pass
#						except timeout:
						#print_exc()
					except:
						print_exc()
				except:
					print_exc()
					print(dataplease)
					print(error)


class Calc(Command):
	def __init__(self):
		Command.__init__(self, ["calc "])
	def action(self, network, recipient, data):
		sendme=data.lower().split("!calc ")[1]
		sendme=sendme.lstrip().rstrip()
		try:
			urltoopen="https://duckduckgo.com/?q="+urllib.parse.quote(sendme)
			textofsite=opener.open(urltoopen).read().decode("utf-8")
			sendmenow=textofsite.split("document.x.q.value=")[1].split(";document.x.q.focus()")[0].replace("\\\"", "")#.replace(",", "")
			if sendmenow:
				stringsender(str(sendmenow), recipient, network)
		except:
			print(textofsite)
			print_exc()

class Roll(Command):
	def __init__(self):
		Command.__init__(self, ["roll "])
	def action(self, network, recipient, data):
		numberme=data.lower().split("!roll ")[1]
		try:
			if numberme[1]=="d":
				rollme, dicesides=numberme.split("d")
				rollme=int(rollme)
				dicesides=int(dicesides)
			else:
				dicesides=int(numberme.split("d")[1])
				rollme=1

			if dicesides<2:
				dicesides=6
			if rollme==0:
				rollme=1
			elif rollme>20:
				rollme=20
			if rollme==1:
				text="1 time"
			else:
				text=str(rollme)+" times"

			results=[]
			totalrolls=""
			for i in range(0, rollme):
				rolled=random.randrange(1,dicesides+1)
				if i==rollme-1:
					totalrolls+=str(rolled)
				else:
					totalrolls+=str(rolled)+" "
			sendastringtowho("You rolled the "+str(dicesides)+"-sided die "+str(text)+" and got: "+str(totalrolls), data, network)
		except:
			pass

class CoinFlip(Command):
	def __init__(self):
		Command.__init__(self, ["flip"], 1)
	def action(self, network, recipient, data):
		name=nickanick(data)
		coin=random.choice(["heads", "tails"])
		sendastringtowho(name+", you flip a coin, and you get... "+coin+"!", data, network)


class SmallestViolin(Command):
	def __init__(self):
		Command.__init__(self, ["smallestviolin"], 1)
	def action(self, network, recipient, data):
		sendastringtowho(chr(1)+"ACTION plays a song full of mourning on the world's smallest Sadivarius violin."+chr(1), data, network)

class Dance(Command):
	def __init__(self):
		Command.__init__(self, ["dance"], 1)
	def action(self, network, recipient, data):
		sendastringtowho(chr(1)+"ACTION dances the Mephisto Waltz with "+nickanick(data)+"."+chr(1), data, network)

class ShowFC(Command):
	def __init__(self):
		Command.__init__(self, ["showfc"])
	def action(self, network, recipient, data):
		try:
			cleanuser=data.split("showfc ")[1].split(" ")[0]
			try:
				cleangame=data.split(cleanuser+" ")[1].rstrip()
			except:
				cleangame=""
			try:
				fcdb=open("fcdatabase.txt", "r")
				fcdatabase=ast.literal_eval(fcdb.read())
				fcdb.close()
				if cleangame:
					cleanfc=fcdatabase[cleanuser][cleangame]
					sendastringtowho(str(cleangame+" FC for "+cleanuser+": "+cleanfc[0]), data, network)
				else:
					for i in fcdatabase[cleanuser].keys():
						sendastringtowho(str(i+" FC for "+cleanuser+": "+fcdatabase[cleanuser][i][0]), data, network)
						
			except:
				sendastringtowho(str(cleanuser+" has no FC registered for "+i+"."), data, network)
				print_exc()
		except:
			pass
class UnregFC(Command):
	def __init__(self):
		Command.__init__(self, ["unregfc "])
	def action(self, network, recipient, data):
		try:
			cleanuser=data.split("unregfc ")[1].split(" ")[0]
			cleangame=data.split(cleanuser+" ")[1].rstrip()
			try:
				fcdb=open("fcdatabase.txt", "r")
				fcdatabase=ast.literal_eval(fcdb.read())
				fcdb.close()
				del fcdatabase[cleanuser][cleangame]
				fcdb=open("fcdatabase.txt", "w")
				fcdb.write(repr(fcdatabase))
				fcdb.close()
				sendastringtowho(str(cleangame+" FC for "+cleanuser+" unregistered."), data, network)
			except:
				pass			
		except:
			pass
		
class RegFC(Command):
	def __init__(self):
		Command.__init__(self, ["regfc "])
	def action(self, network, recipient, data):
		#!regfc Spiffy White 1111-1111-1111
		#if you can convert more than one of the items into int...it's baad
		try:
			cleanuser=data.split("regfc ")[1].split(" ")[0]
			cleanfc=data.split(" ")[-1]
			cleangame=data.split(cleanuser+" ")[1].split(" "+cleanfc)[0]
			#cleanfc=data.split(cleangame+" ")[1].rstrip()
			#make it into camelcase, though the
			try:
				fcdb=open("fcdatabase.txt", "r")
				fcdatabase=ast.literal_eval(fcdb.read())
				fcdb.close()
			except:
				fcdb=open("fcdatabase.txt", "w")
				fcdb.close()
				fcdatabase={}
			
			try:
				if type(fcdatabase[cleanuser])==dict:
					pass
			except:
				fcdatabase[cleanuser]={}
				#pass
			fcdatabase[cleanuser][cleangame]=[cleanfc]
			fcdb=open("fcdatabase.txt", "w")
			fcdb.write(repr(fcdatabase))
			fcdb.close()
			sendastringtowho(str(cleangame+" FC for "+cleanuser+" registered: "+cleanfc), data, network)
		except:
			print_exc()
			
class FCHelp(Command):
	def __init__(self):
		Command.__init__(self, ["fchelp"], 1)
	def action(self, network, recipient, data):
		sendastringtowho("Syntax for !regfc: USERNAME GAME FRIENDCODE", data, network)
		sendastringtowho("Syntax for !showfc: USERNAME GAME", data, network)
		sendastringtowho("Syntax for !unregfc (usable by the operator of "+legionconfig[network][0]+" only): USERNAME GAME", data, network)
		sendastringtowho("Do not put spaces in usernames or friend codes.", data, network)

class SuperSaying(Command):
	def __init__(self):
		Command.__init__(self, ["supersaying "])
	def action(self, network, recipient, data):
		if nickanick(data)==legionconfig[network][1]:
			try:
				karkar=data.find(":!supersaying ")
				#cut the trigger off, get to parsing the tail
				spammerintheworks=data[karkar:]
				spammerintheworks=spammerintheworks[14:]
				spamchan=spammerintheworks.split(" ")[0].lower()
				if "#" in spamchan and spamchan[1:] in legionconfig[network][3] or "#" not in spamchan:
					listsong=spammerintheworks.split(spamchan+" ")[1]
					legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+spamchan+" :"+listsong+"\r\n"))
			except:
				print_exc()

class SuperActing(Command):
	def __init__(self):
		Command.__init__(self, ["superacting "])
	def action(self, network, recipient, data):
		if nickanick(data)==legionconfig[network][1]:
			try:
				karkar=data.find(":!superacting ")
				spammerintheworks=data[karkar:]
				spammerintheworks=spammerintheworks[14:]
				spamchan=spammerintheworks.split(" ")[0].lower()
				if "#" in spamchan and spamchan[1:] in legionconfig[network][3] or "#" not in spamchan:
					listsong=spammerintheworks.split(spamchan+" ")[1]
					legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+spamchan+" :"+chr(1)+"ACTION "+listsong+chr(1)+"\r\n"))
			except:
				pass

class TooCommanding(Command):
	def __init__(self):
		Command.__init__(self, ["toocommanding "])
	def action(self, network, recipient, data):
		if nickanick(data)==legionconfig[network][1]:
			try:
				datar=data.split("!toocommanding ")[1]
				if "join" in datar.lower():
					datare=datar.split(" ")[1]
					legionconfig[network][3].append(datare[1:])
				elif "part" in datar.lower():
					datare=datar.split(" ")[1]
					caar=legionconfig[network][3].index(datare[1:])
					del legionconfig[network][3][caar]
				legionconfig[network][5].send(bytesgoutf8(datar+"\r\n"))
			except:
				print_exc()

"""
class JishoEToJ(Command):
	def __init__(self):
		Command.__init__(self, ["jishoetoj "])
	def action(self, network, recipient, data):
		tolookup=data.split("jishoetoj ")[1].rstrip()
		if tolookup:
			result=denshijisho.wordlookup(tolookup, "English")
			if result:
				sendastringtowho(result, data, network)
class JishoJToE(Command):
	def __init__(self):
		Command.__init__(self, ["jishojtoe "])
	def action(self, network, recipient, data):
		tolookup=data.split("jishojtoe ")[1].rstrip()
		if tolookup:
			result=denshijisho.wordlookup(tolookup, "Japanese")
			if result:
				sendastringtowho(result, data, network)
		denshijisho.wordlookup("Cat", "Japanese")
class EToJishoKanji(Command):
	def __init__(self):
		Command.__init__(self, ["jishoetokanji "])
	def action(self, network, recipient, data):
		tolookup=data.split("jishoetokanji ")[1].rstrip()
		if tolookup:
			result=denshijisho.kanjilookup(tolookup, "English")
			if result:
				sendastringtowho(result, data, network)
class JishoKanjiToE(Command):
	def __init__(self):
		Command.__init__(self, ["jishokanjitoe "])
	def action(self, network, recipient, data):
		tolookup=data.split("jishokanjitoe ")[1].rstrip()
		if tolookup:
			result=denshijisho.kanjilookup(tolookup, "Japanese")
			if result:
				sendastringtowho(result, data, network)
"""

class LaughTrack(Command):
	def __init__(self):
		Command.__init__(self, ["laughtrack"], 1)
	def action(self, network, recipient, data):
		sendastringtowho(random.choice(["Ha ha ha ha ha.", "Ah ha ha! Ah ha, ah ha ha!", "Lollerskates!"]), data, network)


class Runes(Command):
	def __init__(self):
		Command.__init__(self, ["runes"], 2)
	def action(self, network, recipient, data):
		fortheuser,searchforme=data.lower().split("!runes")
		searchforme=searchforme.lstrip().rstrip()
		user=nickanick(fortheuser)
		if searchforme.lower()=="help" or searchforme=="":
			pmsomebigline("List of methods:", data, network)
			pmsomebigline("One Rune (!runes 1-rune)", data, network)
			pmsomebigline("The Norns (!runes thenorns)", data, network)
			pmsomebigline("The Roman Method (!runes roman)", data, network)
			pmsomebigline("Five-Rune (!runes 5-rune)", data, network)
			pmsomebigline("Seven-Rune (!runes 7-rune)", data, network)
			pmsomebigline("Nine-Rune cast (!runes 9-rune)", data, network)
		elif searchforme.lower()=="1-rune":
			legionconfig[network][10].append([user, runesmodule.OneRune()])
		elif searchforme.lower()=="thenorns":
			legionconfig[network][10].append([user, runesmodule.TheNorns()])
		elif searchforme.lower()=="roman":
			legionconfig[network][10].append([user, runesmodule.TheRomanMethod()])
		elif searchforme.lower()=="5-rune":
			legionconfig[network][10].append([user, runesmodule.FiveRune()])
		elif searchforme.lower()=="7-rune":
			legionconfig[network][10].append([user, runesmodule.SevenRune()])
		elif searchforme.lower()=="9-rune":
			legionconfig[network][10].append([user, runesmodule.NineRuneCast()])

class Tarot(Command):
	def __init__(self):
		Command.__init__(self, ["tarot"], 2)
	def action(self, network, recipient, data):
		fortheuser,searchforme=data.lower().split("!tarot")
		searchforme=searchforme.lstrip().rstrip()
		user=nickanick(fortheuser)
		if searchforme.lower()=="help" or searchforme=="":
			pmsomebigline("List of spreads:", data, network)
			pmsomebigline("Three-card spread (!tarot 3-card)", data, network)
			pmsomebigline("Five-card spread (!tarot 5-card)", data, network)
			pmsomebigline("Seven-card Draw (!tarot 7-card)", data, network)
			pmsomebigline("Horseshoe (!tarot horseshoe)", data, network)
			pmsomebigline("General spread (!tarot general)", data, network)
			pmsomebigline("Celtic Cross (!tarot celtic)", data, network)
			pmsomebigline("Tree Of Life (!tarot treeoflife)", data, network)
			pmsomebigline("Horoscope (!tarot horoscope)", data, network)
		elif searchforme.lower()=="3-card":
			legionconfig[network][9].append([user, tarotmodule.ThreeCard()])
		elif searchforme.lower()=="5-card":
			legionconfig[network][9].append([user, tarotmodule.FiveCard()])
		elif searchforme.lower()=="7-card":
			legionconfig[network][9].append([user, tarotmodule.SevenCardDraw()])
		elif searchforme.lower()=="horseshoe":
			legionconfig[network][9].append([user, tarotmodule.Horseshoe()])
		elif searchforme.lower()=="general":
			legionconfig[network][9].append([user, tarotmodule.General()])
		elif searchforme.lower()=="celtic":
			legionconfig[network][9].append([user, tarotmodule.CelticCross()])
		elif searchforme.lower()=="treeoflife":
			legionconfig[network][9].append([user, tarotmodule.TreeOfLife()])
		elif searchforme.lower()=="horoscope":
			legionconfig[network][9].append([user, tarotmodule.Horoscope()])

class ShowTropeScores(Command):
	def __init__(self):
		#I could make these commands take the sender as the default value
		Command.__init__(self, ["showtropescores "])
	def action(self, network, recipient, data):
		try:
			cleanuser=data.split("showtropescores ")[1]
			showscores(cleanuser, "Guess That Trope", data, network)
		except:
			print_exc()
		
class ShowOverallTropeScores(Command):
	def __init__(self):
		Command.__init__(self, ["showoveralltropescore "])
	def action(self, network, recipient, data):
		try:
			cleanuser=data.split("showoveralltropescore ")[1]
			showoverallscore(cleanuser, "Guess That Trope", data, network)
		except:
			print_exc()

class ShowPokemonScores(Command):
	def __init__(self):
		Command.__init__(self, ["showpokemonscores "])
	def action(self, network, recipient, data):
		cleanuser=data.split("showpokemonscores ")[1]
		try:
			cleanuser=data.split("showpokemonscores ")[1]
			showscores(cleanuser, "Who's That Pokémon?", data, network)
		except:
			print_exc()

class ShowOverallPokemonScores(Command):
	def __init__(self):
		Command.__init__(self, ["showoverallpokemonscore "])
	def action(self, network, recipient, data):
		try:
			cleanuser=data.split("showoverallpokemonscore ")[1]
			showoverallscore(cleanuser, "Who's That Pokémon?", data, network)

		except:
			print_exc()
		
class ShowGameScores(Command):
	def __init__(self):
		Command.__init__(self, ["showgamescores "])
	def action(self, network, recipient, data):
		try:
			cleanuser=data.split("showgamescores ")[1]
			showscores(cleanuser, None, data, network)

		except:
			print_exc()
		
				
class ShowOverallGameScores(Command):
	def __init__(self):
		Command.__init__(self, ["showoverallgamesscore "])
	def action(self, network, recipient, data):
		try:
			cleanuser=data.split("showoverallgamesscore ")[1]
			showoverallscore(cleanuser, None, data, network)

		except:
			print_exc()

class Dice(Command):
	def __init__(self):
		Command.__init__(self, ["dice "], 1)
	def action(self, network, recipient, data):
		numberme=data.lower().split("!dice")[1]
		foundnumber=[]
		try:
			foundnumber=numberfind.findall(numberme)
			#if there's no other number, just do 6
			if len(foundnumber)<2:
				dicesides=6
			else:
				dicesides=int(foundnumber[1])
			if len(foundnumber)==0:
				rolltimes=1
			else:
				rolltimes=int(foundnumber[0])
			if rolltimes>20:
				rolltimes=20
			if rolltimes==1:
				text="1 time"
			else:
				text=str(rolltimes)+" times"
			totalrolls=""
			for i in range(0, rolltimes):
				rolled=random.randrange(1,dicesides+1)
				if i==rolltimes-1:
					totalrolls+=str(rolled)
				else:
					totalrolls+=str(rolled)+" "
			sendastringtowho("You rolled the "+str(dicesides)+"-sided die "+str(text)+" and got: "+str(totalrolls), data, network)
		except:
			print_exc()

class F2C(Command):
	def __init__(self):
		Command.__init__(self, ["f2c "])
	def action(self, network, recipient, data):
		numberme=data.lower().split("!f2c ")[1]
		#foundnumber=numberfind.findall(numberme)
		foundnumber=numberme
		try:
			#foundnumber=foundnumber[0]
			try:
				foundnumber=float(foundnumber)
			except:
				foundnumber=int(foundnumber)
			celsius=((foundnumber-32)*5)/9.0
			if celsius==int(celsius):
				celsius=int(celsius)
			else:
				celsius=round(celsius, 1)
			sendastringtowho("Your temperature in Celsius is "+str(celsius)+".", data, network)
		except:
			pass
class C2F(Command):
	def __init__(self):
		Command.__init__(self, ["c2f "])
	def action(self, network, recipient, data):
		numberme=data.lower().split("!c2f ")[1]
		#foundnumber=numberfind.findall(numberme)
		foundnumber=numberme
		try:
			#foundnumber=foundnumber[0]
			try:
				foundnumber=float(foundnumber)
			except:
				foundnumber=int(foundnumber)
			fahrenheit=((foundnumber*9)/5.0)+32
			if fahrenheit==int(fahrenheit):
				fahrenheit=int(fahrenheit)
			else:
				fahrenheit=round(fahrenheit, 1)
			sendastringtowho("Your temperature in Fahrenheit is "+str(fahrenheit)+".", data, network)
		except:
			pass
					

class LocalTime(Command):
	def __init__(self):
		Command.__init__(self, ["localtime"], 1)
	def action(self, network, recipient, data):
		sendme=data.lower().split("!localtime ")[1]
		sendme=sendme.lstrip().rstrip()
		themessage=localtimereturn(sendme)
		if themessage:
			sendastringtowho(themessage, data, network)
				
class AddQuote(Command):
	def __init__(self):
		Command.__init__(self, ["addquote "])
	def action(self, network, recipient, data):
		#just lower the addquote part?
		addthis=data.split("!addquote ")[1].rstrip()
		#better way to store quotes
		if addthis:
			#addthis.replace("\'","SLASHANDAPOSTRAPHE")
			#addthis.replace("'","\'")
			#addthis.replace("SLASHANDAPOSTRAPHE", "\'")
			try:
				quotesfile=open(quotedatabasefilename, "r")
			except:
				quotesfile=open(quotedatabasefilename, "w")
				quotesfile.write(repr([]))
				quotesfile.close()
				quotesfile=open(quotedatabasefilename, "r")
			quotes=ast.literal_eval(quotesfile.read())
			quotesfile.close()
			quotes.append(addthis)
			indexnumber=len(quotes)
			quotesfile=open(quotedatabasefilename, "w")
			quotesfile.write(repr(quotes))
			quotesfile.close()
			sendastringtowho("Quote #"+str(indexnumber)+" added.", data, network)
	
class ViewQuote(Command):
	def __init__(self):
		Command.__init__(self, ["viewquote "], 1)
	def action(self, network, recipient, data):
		#just lower the addquote part?
		viewthis=data.lower().split("!viewquote ")[1]
		if viewthis:
			if " " in viewthis:
				viewthis=viewthis.split(" ")[0]
			try:
				viewthis=int(viewthis)
				quotesfile=open(quotedatabasefilename, "r")
				quotes=ast.literal_eval(quotesfile.read())
				quotesfile.close()
				sendastringtowho("Quote #"+str(viewthis)+": "+quotes[viewthis-1], data, network)
			except:
				print_exc()

class RandomQuote(Command):
	def __init__(self):
		Command.__init__(self, ["randomquote"], 1)
	def action(self, network, recipient, data):
		try:
			quotesfile=open(quotedatabasefilename, "r")
			quotes=ast.literal_eval(quotesfile.read())
			quotesfile.close()
			daquote=random.choice(quotes)
			quotenumber=quotes.index(daquote)
			sendastringtowho("Quote #"+str(quotenumber+1)+": "+daquote, data, network)
		except:
			print_exc()

class QuoteSearch(Command):
	def __init__(self):
		Command.__init__(self, ["quotesearch "])
	def action(self, network, recipient, data):
		#just lower the addquote part?
		try:
			searchthis=data.lower().split("!quotesearch ")[1].rstrip()
			if searchthis:
				foundthat=[]
				quotesfile=open(quotedatabasefilename, "r")
				quotes=ast.literal_eval(quotesfile.read())
				quotesfile.close()
				for i in range(0, len(quotes)):
					if searchthis.lower() in quotes[i].lower():
						foundthat.append(i+1)
				if foundthat:
					results=""
					for i in foundthat:
						results+=str(i)
						results+=" "
					results=results.rstrip(" ")
					sendastringtowho("Results: "+results, data, network)
		except:
			print_exc()

class RemoveQuote(Command):
	def __init__(self):
		Command.__init__(self, ["removequote "])
	def action(self, network, recipient, data):
		#just lower the addquote part?
		cleanuser, removethis=data.lower().split("!removequote ")
		#cleanuser=data.split("PRIVMSG #"+channelname+" :!")[0]
		cleanuser=nickanick(cleanuser)
		#separate the numbers by space, try to int them all, then sort them from biggest to smallest, then do the delling
		if removethis and cleanuser.lower()==legionconfig[i][1].lower():
			if " " in removethis:
				removethis=removethis.split(" ")
				for i in removethis:
					try:
						i=int(i)
					except:
						pass
				for i in reversed(removethis):
					try:
						j=int(i)
						if j<1:
							del removethis[removethis.index(i)]
					except:
						del removethis[removethis.index(i)]
				if len(removethis)>0:
					removethis=sorted(removethis, reverse=True)
					quotesfile=open(quotedatabasefilename, "r")
					quotes=ast.literal_eval(quotesfile.read())
					quotesfile.close()
					for i in removethis:
						i=int(i)
						try:
							del quotes[i-1]
							sendastringtowho("Quote #"+str(i)+" removed.", data, network)
						except:
							pass
					quotesfile=open(quotedatabasefilename, "w")
					quotesfile.write(repr(quotes))
					quotesfile.close()					
			else:
				try:
					removethis=int(removethis)
				except:
					pass
				
				quotesfile=open(quotedatabasefilename, "r")
				quotes=ast.literal_eval(quotesfile.read())
				quotesfile.close()
				if removethis>=len(quotes) and removethis>0:
					del quotes[removethis-1]
					sendastringtowho("Quote #"+str(removethis)+" removed.", data, network)
				quotesfile=open(quotedatabasefilename, "w")
				quotesfile.write(repr(quotes))
				quotesfile.close()

class Weather(Command):
	def __init__(self):
		Command.__init__(self, ["weather "])
	def action(self, network, recipient, data):
		if nickachan(data) in legionconfig[network][7] and not "bot" in legionconfig[network][7][nickachan(data)] and not "aigis" in legionconfig[network][7][nickachan(data)] and not "Bot" in legionconfig[network][7][nickachan(data)] and not "Aigis" in legionconfig[network][7][nickachan(data)] and not "Misaka" in legionconfig[network][7][nickachan(data)] and not "misaka" in legionconfig[network][7][nickachan(data)] or nickachan(data)=="":
			searchforme=data.lower().split("!weather ")[1].rstrip()
			later=getweather(searchforme)
	#!weather detroit, mi
	#<Legion>	Current conditions for Detroit, MI: Sunny, 85°F (29°C) Humidity: 72% Wind: SW at 10 mph
	#<Legion>	Thu: Sunny, 99°F/74°F - Fri: Partly Cloudy, 91°F/75°F - Sat: Scattered Thunderstorms, 91°F/73°F - Sun: Scattered Thunderstorms, 87°F/73°F
				#later=later[:-3]
			if later:
				sendastringtowho(later, data, network)
class Grab(Command):
	def __init__(self):
		Command.__init__(self, ["grab "])
	def action(self, network, recipient, data):
		thegrabbed=data.split("grab ")[1]
		cleanuser=nickanick(data)
		sendastringtowho(cleanuser+" grabs "+thegrabbed+"!", data, network)
