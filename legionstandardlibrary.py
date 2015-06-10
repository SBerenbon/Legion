#from legion import legionconfig

def bytesgoutf8(strung):
	return bytes(strung, "UTF-8")

def bytesgooutlatin1(strung):
	return bytes(strung, "latin-1")


#by default, commandcheck thinks the command has arguments
def commandcheck(datatocheck, command, network, argless=0):
	datatocheck=datatocheck.rstrip()
	if datatocheck.lower().find ( "privmsg "+legionconfig[network][0].lower()+" :") != -1:
		if datatocheck.lower().find ( "privmsg "+legionconfig[network][0].lower()+" :!"+command.lower()) != -1:
			if argless==1:
				try:
					if not data.lower().split("privmsg #"+chan.lower()+" :!"+command.lower())[1].strip():
						return 1
				except:
					pass
			else:
				return 1
	#if you find the lower form of a channel in chanlist
	else:
		for chan in legionconfig[network][3]:
			if datatocheck.lower().find ( "privmsg #"+chan.lower()) != -1:
				if datatocheck.lower().find ( "privmsg #"+chan.lower()+" :!"+command.lower() ) != -1:
					if argless==1:
						try:
							if not data.lower().split("privmsg #"+chan.lower()+" :!"+command.lower())[1].strip():
								return 2
						except:
							pass
					else:
						return 2
	return 0


def averagefinder(numberlist):
	dasum = sum(numberlist)
	dalen=len(numberlist)
	return dasum/(dalen*1.0)

def list2string(listy):
	return str(listy)[1:-1]

def showscores(user, game, data, network):
	try:
		line=""
		linelist=[]
		vtable=open("legionscoreboard", "r")
		victorytable=ast.literal_eval(vtable.read())
		for thek in victorytable[network].keys():
			if thek.lower()==user.lower():
				if game!=None:
					percentedlist=[]
					for this in victorytable[network][user][game]:
						percentedlist.append(str(this)+"%")
					
					line="Scores for "+game+" under the name "+user+": "+list2string(percentedlist).replace("'","")
				else:
					for g in victorytable[network][user].keys():
						percentedlist=[]
						for this in victorytable[network][user][g]:
							percentedlist.append(str(this)+"%")
						linelist.append("Scores for "+g+" under the name "+user+": "+list2string(percentedlist).replace("'",""))
					#line=list2string(victorytable[network][user][g])
				if line:
					pmsomebigline(line, data, network)
				if linelist:
					for ll in linelist:
						pmsomebigline(ll, data, network)
	except:
		print_exc()

#do a function, check the sender	

def showoverallscore(user, game, data, network):
	try:
		vtable=open("legionscoreboard", "r")
		victorytable=ast.literal_eval(vtable.read())
		for thek in victorytable[network].keys():
			if thek.lower()==user.lower():
				if game!=None:
					theaverage=averagefinder(victorytable[network][user][game])
					if theaverage:
						legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+nickanick(data)+" :Average score for "+game+" under the name "+user+": "+str(ceil(theaverage))+"%\r\n"))
				else:
					finallist=[]
					for g in victorytable[network][user].keys():
						finallist+=victorytable[network][user][g]
						
					theaverage=averagefinder(finallist)
					if theaverage:
						legionconfig[network][5].send(bytesgoutf8( "PRIVMSG "+nickanick(data)+" :Average score for all games under the name "+user+": "+str(ceil(theaverage))+"%\r\n"))
	except:
		print_exc()


def nickanick(string):
	if ":" in string and "!" in string:
		return string.split(":")[1].split("!")[0]
	else:
		return ""
		

def nickachan(string):

#:Spiffy!sarah@the.byte.is.life PRIVMSG #bulbagarden :https://www.youtube.com/watch?v=OyaePcQqrrQ
	if " #" in string and " :" in string:
		try:
			return "#"+string.split(":")[1].split( " #")[1].split(" :")[0].rstrip()
		except:
			return ""
	else:
		return ""


def astringweknow(string, recipient, network):
	legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+recipient+" :"+string+"\r\n"))

def sendastringtowho(string, data, network):
	if " PRIVMSG "+legionconfig[network][0]+" :" not in data and " PRIVMSG #" in data:#the data being judged
		#send to channel
		cleanchan=data.split("PRIVMSG #")[1]
		cleanchan=cleanchan.split(" :")[0]
		#could it just return the next part of the string
		legionconfig[network][5].send(bytesgoutf8("PRIVMSG #"+cleanchan+" :"+string+"\r\n"))
	else:
		cleanuser=data.split(" PRIVMSG ")[0]
		cleanuser=nickanick(cleanuser)
		legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+cleanuser+" :"+string+"\r\n"))
		#send to user

def pmsomebigline(line, data, network):
	if len(line)>400:
		cf= lambda s,p: [ s[i:i+p] for i in range(0,len(s),p) ]
		choppedline=cf(line, 400)
		for x in choppedline:
			legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+nickanick(data)+" :"+x+"\r\n"))
	else:
		legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+nickanick(data)+" :"+line+"\r\n"))

#dict: userlists, channame as key, value as list of users

def unescape(text):
	def fixup(m):
		text = m.group(0)
		if text[:2] == "&#":
			# character reference
			try:
				if text[:3] == "&#x":
					return chr(int(text[3:-1], 16))
				else:
					return chr(int(text[2:-1]))
			except ValueError:
				pass
		else:
			# named entity
			try:
				text = chr(html.entities.name2codepoint[text[1:-1]])
			except KeyError:
				pass
		return text # leave as is
	return re.sub("&#?\w+;", fixup, text)

def addscoretoscoreboard(user, game):
	try:
		vtable=open("legionscoreboard", "r")
		victorytable=ast.literal_eval(vtable.read())
	except:
		victorytable=open("legionscoreboard", "w")
		victorytable.write(repr({}))
		victorytable.close()
		vtable=open("legionscoreboard", "r").read()
		victorytable=ast.literal_eval(vtable)
	try:
		victorytable[legionconfig[2]][user][game].append(grade)
	except:
		try:
			victorytable[legionconfig[2]][user][game]=[]
			victorytable[legionconfig[2]][user][game].append(grade)
		except:
			try:
				victorytable[legionconfig[2]][user]={}
				victorytable[legionconfig[2]][user][game]=[]
				victorytable[legionconfig[2]][user][game].append(grade)
			except:
				try:
												
					victorytable[legionconfig[2]]={}
					victorytable[legionconfig[2]][user]={}
					victorytable[legionconfig[2]][user][game]=[]
					victorytable[legionconfig[2]][user][game].append(grade)
				except:
					pass
					
	vtable=open("legionscoreboard", "w")
	vtable.write(repr(victorytable))
	vtable.close()

def getatrope():
	htmletter=opener.open("http://tvtropes.org/pmwiki/randomitem.php?p=1").read().decode("latin-1")
	return htmletter

def gettropeexample():
	sentry=1
	while sentry==1:
		title=""
		truehtml=""
		cutme=0
		htmlette=None
		listtodel=[]
		cutonme=0
		newihtmlette=""
		newtitlesection=""
		newhtmlette=""
		cutting=""
		while not htmlette:
			htmlette=getatrope()
		htmlette=htmlette.split("\n")

		for i in range(0,len(htmlette)):
			if "folderlabel" in htmlette[i] or "asscaps" in htmlette[i] or "\"indent\"" in htmlette[i] or "'indent'" in htmlette[i]:
				listtodel.append(i)
			elif htmlette[i].count("</a>")==1 and "</li><li> <a class=\"twikilink\">" in htmlette[i] or htmlette[i].count("</a>")==1 and "</li><li> <a class='twikilink'>" in htmlette[i]:
				listtodel.append(i)

		for i in reversed(listtodel):
			del htmlette[i]
		
		for i in range(0,len(htmlette)):
			if "<h2>" in htmlette[i] or "Examples" in htmlette[i] and "</strong>" in htmlette[i]:
				cutting=htmlette[i]
				cutonme=i
				break
		
		cutonmenow=cutonme-1
		titlesection=htmlette[0:cutonmenow]
		htmlette=htmlette[cutonme:]
		
		for i in titlesection:
			newtitlesection+=(i+"\n")
		
		for i in htmlette:
			if not "setAllFolders('');" in i:
				newihtmlette+=(i+"\n")
			else:
				break
		try:
			newihtmlette=newihtmlette.split(cutting)[1]
			for i in newihtmlette:
				newhtmlette+=(i)
			
			htmler = lxml.html.fromstring(newhtmlette)
			titlehtml = lxml.html.fromstring(newtitlesection)
			#titlehtml=titlehtml.text_content().encode("utf-8").lstrip()
			titlehtml=titlehtml.text_content().strip()#.decode("latin-1").lstrip()
			#htmler=htmler.text_content().encode("utf-8")
			htmler=htmler.text_content()#.decode("latin-1")
			try:
				title=titlehtml.split(" - TV Tropes")[0]
			except:
				title=titlehtml.split(" - TV Tropes")[0]
					
			examples=[]
			examples=htmler.split("\n")[:-1]
			try:
				examples.remove("")
			except:
				pass
			
			for i in range(0,len(examples)):
				try:
					if examples[i][0]==" ":
						examples[i]=examples[i].lstrip()
				except:
					pass
			nowant=[]
			for i in range(0,len(examples)):
				if len(examples[i])<40 or examples[i][-1]==":" or title.lower() in examples[i].lower():
					nowant.append(i)
			for p in reversed(nowant):
				del examples[p]
			if len(examples)>0:
				sentry=0
		except:
			print_exc()
	examples=examples[:-2]
	choice=random.choice(examples)
	return title, choice

def asktrope(gamer):
	thetrope, theexample=gettropeexample()
	
	print(thetrope,"is your trope.")#,chardet.detect(thetrope)["encoding"]
	if len(theexample)>400:
		msg=theexample
		cf= lambda s,p: [ s[i:i+p] for i in range(0,len(s),p) ]
		newmessages=cf(msg, 400)

		for x in newmessages:
			legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+gamer+" :"+x+"\r\n"))
	else:
		legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+gamer+" :"+theexample+"\r\n"))
	return thetrope
#now for the command functions...gotta keep everything untangled

def getapokemon(gamer):
	numnum=random.randrange(1, 722)
	thepokedict=open("pokedex", "rt")
	pokedex=eval(thepokedict.read())
	thepokedict.close()
	hint=pokedex[numnum][0]
	#you either get a pokedex entry or a "This is a Grass type..."
#	hint=pokedex[numnum][0].encode("utf-8")#you either get a pokedex entry or a "This is a Grass type..."
#	print("The hint is",hint)
	entry=random.choice(pokedex[numnum][2])
	pokemon=pokedex[numnum][1]
	print(pokemon+" is your Pokemon.")
	legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+gamer+" :"+hint+"\r\n"))
	return pokemon, entry
#now for the command functions...gotta keep everything untangled

def legioncussout(data, network):
	cleanuser, cleanme=data.split("PRIVMSG")
	cleanme=cleanme.split(":!")[1]
	if " " not in cleanme:
		cleanme+=" "
	cleanme=cleanme.split(" ")[0]
	cleanme=cleanme.rstrip()
	cleanme=cleanme.rstrip("\r\n")
	cleanme=cleanme.rstrip("\n")
	cleanuser=nickanick(cleanuser)
	sendastringtowho("Now you just shut the fuck up "+cleanuser+", and stick your damn !"+cleanme+" up your asshole, you fucking lazy bastard!", data, network)

#just name the data something special for each function if you have problems?

def localtimereturn(place):
	try:
		titleline=""
		goodline=""
		placeline=""
		timeline=""
		cleaning=""
		urltoopen="http://www.wolframalpha.com/input/?i=time+in+"+urllib.parse.quote_plus(place)
		textofsite=opener.open(urltoopen).read().decode("utf-8").split("\n")

		for line in textofsite:
			if "context.jsonArray.popups.pod_0100.push( {\"stringified\": \"" in line:
				placeline=line
			if "context.jsonArray.popups.pod_0200.push( {\"stringified\": \"" in line:
				timeline=line
		if placeline:
			
		#	try:				cleaning=placeline.split("current time in ")[1]
			cleaning=placeline.split("\",\"mInput")[0].split("\"stringified\": \"current time in ")[1]
			title=unescape("Current time in "+cleaning)#.decode("utf-8")
		#	except:
		#		cleaning=placeline.split("In ")[1]
		#		cleaning=cleaning.split("\",\"mInput")[0]
		#		title=unescape("Current time in "+cleaning).encode("utf-8")
		if timeline:
			cleaning=timeline.split("stringified\": \"")[1]
			cleaning=cleaning.split("\",\"mInput")[0]
			time=cleaning.replace("  ", " ")
		if time and title:
			return title+": "+time
	except:
		print_exc()


def notaselfcase(i, data):
	if data.split(i)[1]:
		return 0
	else:
		return 1

#def jsonstringvalextractor(stringer, value):
#separate sections for numbers and strings
#	return stringer.split

def getweather(searchforme):
	searchforme=searchforme.replace(". ", ", ").replace("St, ", "St. ").replace("st, ", "st. ").replace("ST, ", "ST. ")
	#<Legion>	Current conditions for Detroit, MI: Sunny, 85°F (29°C) Humidity: 72% Wind: SW at 10 mph
	#<Legion>	Thu: Sunny, 99°F/74°F - Fri: Partly Cloudy, 91°F/75°F - Sat: Scattered Thunderstorms, 91°F/73°F - Sun: Scattered Thunderstorms, 87°F/73°F

	#<Spiffy> !weather detroit, mi
	#<Legion> Current conditions for Detroit, Michigan: Heavy Snow, 23°F (-5°C) Humidity: 24% Wind: ENE at 20 mph
	#<Legion> Sat: Partly Cloudy, 23°F/1°F (-5°C/-17°C) - Sun: Snow, 21°F/9°F (-6°C/-12°C) - Mon: Mostly Cloudy, 10°F/-6°F (-12°C/-21°C) - Tue: Partly Cloudy, 5°F/-4°F (-15°C/-20°C) - Wed: Partly Cloudy, 9°F/4°F (-12°C/-15°C)
	#<Spiffy> !weather hell, mi
	#<Legion> Current conditions for Hell, Michigan: Light Snow, 22°F (-5°C) Humidity: 23% Wind: NW at 18 mph
	#<Legion> Sat: Mostly Cloudy, 27°F/-7°F (-2°C/-21°C) - Sun: Snow, 20°F/6°F (-6°C/-14°C) - Mon: Mostly Cloudy, 8°F/-10°F (-13°C/-23°C) - Tue: Mostly Cloudy, 9°F/-7°F (-12°C/-21°C) - Wed: Partly Cloudy, 13°F/2°F (-10°C/-16°C)

#<Legion> Current conditions for Detroit, Michigan: Snow, 23°F/1°F (-5°C/-17°C) Humidity: 77% Wind: WNW at 19 mph/30 kph
#<Legion> Sat: Snow, 23°F/1°F (-5°C/-17°C) - Sun: Chance of Snow, 19°F/9°F (-7°C/-13°C) - Mon: Mostly Cloudy, 14°F/-9°F (-10°C/-23°C) - Tue: Fog, 3°F/-9°F (-16°C/-23°C)

#<Misaka> Current conditions for Detroit, MI: Overcast (24.7°F/-4.1°C). Feels like 14°F/-10°C. Humidity: 81%. Wind: From the WNW at 12.0 MPH Gusting to 13.0 MPH (19.3kph).
#<Misaka> Saturday: Snow. High of 23°F/-5°C. Low of 1°F/-17°C. Sunday: Chance of Snow. High of 19°F/-7°C. Low of 9°F/-13°C. 

	whatisthisplace=""
	url="http://autocomplete.wunderground.com/aq?query="+urllib.parse.quote(searchforme)
	auto=opener.open(url).read().decode("utf-8")
	if "\"name\"" in auto:
		whatisthisplace=auto.split("\"name\"")[1].split("\"")[1]
	if whatisthisplace:
		try:
			rightnow="Current conditions for "+str(whatisthisplace)+": "
			later=""
			if "/q/locid:" in auto:
				autocompleteresult=auto.split("\"l\": \"")[1].split("\",")[0]
				theactualpage="http://api.wunderground.com/api/b49b003cc2b0496f/forecast"+autocompleteresult+".json"
			else:
				autocompleteresult=auto.split("\"zmw\": \"")[1].split("\",")[0]
				theactualpage="http://api.wunderground.com/api/b49b003cc2b0496f/forecast/q/zmw:"+autocompleteresult+".json"
			#theactualpage="http://api.wunderground.com/api/b49b003cc2b0496f/forecast/q/zmw:"+autocompleteresult+".json"
			noreallythepage=opener.open(theactualpage).read().decode("utf-8").split("\"simpleforecast\"")[1].split("\"date\"")[1:]
			for i in range(0, len(noreallythepage)):
				dayoftheweek=noreallythepage[i].split("weekday_short\":\"")[1].split("\"")[0]
				condition=noreallythepage[i].split("conditions\":\"")[1].split("\"")[0]
				highinf=noreallythepage[i].split("fahrenheit\":\"")[1].split("\"")[0]
				lowinf=noreallythepage[i].split("fahrenheit\":\"")[2].split("\"")[0]
				highinc=noreallythepage[i].split("celsius\":\"")[1].split("\"")[0]
				lowinc=noreallythepage[i].split("celsius\":\"")[2].split("\"")[0]
				if i==0:
					averagehumidity=noreallythepage[i].split("avehumidity\": ")[1].split(",")[0]
					winddir=noreallythepage[i].split("avewind\": {")[1].split("dir\": \"")[1].split("\"")[0]
					windspeedenglish=noreallythepage[i].split("avewind\": {")[1].split("mph\": ")[1].split(",")[0]
					windspeedmetric=noreallythepage[i].split("avewind\": {")[1].split("kph\": ")[1].split(",")[0]
					
					#currenturl="http://www.wolframalpha.com/input/?i=weather+"+urllib.parse.quote(whatisthisplace)
					if "/q/locid" in autocompleteresult:
						currenturl="http://www.wunderground.com"+autocompleteresult
					else:
						currenturl="http://www.wunderground.com/cgi-bin/findweather/getForecast?query="+autocompleteresult
					wund=opener.open(currenturl).read().decode("utf-8")
					#print(wund)
					wund=wund.split("curCond")[1]


					#.split("small-3 columns")[0]
#					#</dd><dt>wind:</dt><dd>WSW<span> at </span>3mph</dd><dt>humidity:</dt><dd>59%</dd></span></td><td><h3>T
#					conditions=wolf.split("conditions")[1].split(">")[1].split("</")[0]
#					humidity=wolf.split("</dd><dt>humidity:</dt><dd>")[1].split("</dd></span></td><td>")[0]
#					wind=wolf.split("</dd><dt>wind:</dt><dd>")[1].split("</dd><dt>")[0]

#-4&deg;F
					condition=wund.split("wx-value")[1].split(">")[1].split("</span")[0]
					degrees=wund.split("wx-value")[2].split(">")[1].split("</span")[0]+wund.split("wx-unit")[1].split(">")[1].split("</span")[0].replace("&deg;", "°")
					if "°F" in degrees:
						fdegrees=degrees
						degrees=degrees.split("°F")[0]
						try:
							degrees=float(degrees)
						except:
							degrees=int(degrees)
						cdegrees=((degrees-32)*5)/9.0
						if cdegrees==int(cdegrees):
							cdegrees=int(cdegrees)
						else:
							cdegrees=round(cdegrees, 1)
						cdegrees=str(cdegrees)+"°C"

					elif "°C" in degrees:
						cdegrees=degrees
						degrees=degrees.split("°C")[0]
					
						try:
							degrees=float(degrees)
						except:
							degrees=int(degrees)
						fdegrees=((foundnumber*9)/5.0)+32
						if fdegrees==int(fdegrees):
							fdegrees=int(fdegrees)
						else:
							fdegrees=round(fdegrees, 1)
						fdegrees=str(fdegrees)+"°F"
					#more
					currenthumidity=wund.split("<dfn>Humidity</dfn>")[1].split("wx-value")[1].split(">")[1].split("<")[0]
					thedegrees=fdegrees+" ("+cdegrees+")"
					newbert=thedegrees+", "+condition+", Highs/Lows: "+highinf+"°F/"+lowinf+"°F ("+highinc+"°C/"+lowinc+"°C) Humidity: "+currenthumidity+"% Wind: "+winddir+" at "+windspeedenglish+" mph/"+windspeedmetric+" kph"
					#newbert=thedegrees+", "+condition+", Highs/Lows: "+highinf+"°F/"+lowinf+"°F ("+highinc+"°C/"+lowinc+"°C) Humidity: "+averagehumidity+"% Wind: "+winddir+" at "+windspeedenglish+" mph/"+windspeedmetric+" kph"
					rightnow+=newbert
				if later:
					later+=" - "
				later+=dayoftheweek+": "+condition+", "+highinf+"°F/"+lowinf+"°F ("+highinc+"°C/"+lowinc+"°C)"
			sendastringtowho(rightnow, data, network)
			return later
		except:# AttributeError:
			print_exc()


class GuessingGame:
	def __init__(self, guessthis, numberofquestions, asker, game, dexentry):
		self.guessthis=guessthis
		self.numberofquestions=numberofquestions
		self.asker=asker
		self.game=game

		self.timestart= timer()
		self.done=0
		self.totalhints=0
		spacey=0
		thehint=len(self.guessthis)*"_"#.encode("latin-1")
		for i in range(0, len(self.guessthis)):
			if self.guessthis[i]==" ":
				thehint=thehint[:i]+" "+thehint[i+1:]
				spacey+=1
		self.countthis=int(ceil(((len(self.guessthis)-spacey)-1)*.1))
		if self.countthis==0:
			self.countthis=1
		if dexentry:
			self.dexentry=dexentry
		else:
			self.dexentry=""
		self.thehint=thehint
		self.originalhint=thehint

	def another(self):
		if self.game=="trope":
			self.guessthis=asktrope(self.asker)
		elif self.game=="pokemon":
			self.guessthis, self.dexentry=getapokemon(self.asker)
		self.timestart=timer()
		self.done=0
		self.totalhints=0
		spacey=0
		thehint=len(self.guessthis)*"_"#.encode("latin-1")
		for i in range(0, len(self.guessthis)):
			if self.guessthis[i]==" ":
				thehint=thehint[:i]+" "+thehint[i+1:]
				spacey+=1
		self.countthis=ceil(((len(self.guessthis)-spacey)-1)*.1)
		if self.countthis==0:
			self.countthis=1
		#self.dexentry=""
		
class Command:
	def __init__(self, triggerlist, noargs=0):
		#self.command=command
		self.triggerlist=triggerlist
		self.noargs=noargs
		#2 should be for args or noargs
	def check(self, network, data):
		data=data.strip()
		for command in self.triggerlist:
			
			if nickachan(data)=="":
				recipient=nickanick(data)
			#if "privmsg "+legionconfig[network][0].lower()+" :" in data.lower():
				if "privmsg "+legionconfig[network][0].lower()+" :!"+command.lower() in data.lower():
					
					if self.noargs==1:
						try:
							if not data.lower().split(" :!"+command.lower())[1].strip():
								self.action(network, recipient, data)
						except:
							pass
					elif self.noargs==2:
						try:
							if not data.lower().split(" :!"+command.lower())[1].strip() or data.lower().split(" :!"+command.lower())[1][0]==" ":
								self.action(network, recipient, data)
						except:
							pass
					else:
						self.action(network, recipient, data)
	
			#if you find the lower form of a channel in chanlist
			#return a 2? you need an argument!
			else:
				chan=nickachan(data)
				if "privmsg "+chan.lower()+" :!"+command.lower() in data.lower():
					if self.noargs==1:
						try:
							if not data.lower().split("privmsg "+chan.lower()+" :!"+command.lower())[1].strip():
								self.action(network, chan, data)
						except:
							pass
					else:
						self.action(network, chan, data)
			#return 0
		def action(self, network, recipient, data):
			pass



"""


class TriggerlessCommand(Command):
	def __init__(self, triggerlist):
		self.noargs=1
		#self.command=command
		self.triggerlist=triggerlist
		self.noargs=noargs
		Command.__init__(self, self.triggerlist, self.noargs)
		#2 should be for args or noargs
	def check(self, network, data):
		data=data.strip()
		for command in self.triggerlist:
			if data.lower().find ( command.lower() ) != -1:			
				if nickachan(data)=="":
					recipient=nickanick(data)
				else:
					recipient=nickachan(data)
				self.action(network, recipient, data)
"""

def bytesgoutf8(strung):
	return bytes(strung, "UTF-8")

def bytesgooutlatin1(strung):
	return bytes(strung, "latin-1")


def averagefinder(numberlist):
	dasum = sum(numberlist)
	dalen=len(numberlist)
	return dasum/(dalen*1.0)

def list2string(listy):
	return str(listy)[1:-1]

def showscores(user, game, data, network):
	try:
		line=""
		linelist=[]
		vtable=open("legionscoreboard", "r")
		victorytable=ast.literal_eval(vtable.read())
		for thek in victorytable[network].keys():
			if thek.lower()==user.lower():
				if game!=None:
					percentedlist=[]
					for this in victorytable[network][user][game]:
						percentedlist.append(str(this)+"%")
					
					line="Scores for "+game+" under the name "+user+": "+list2string(percentedlist).replace("'","")
				else:
					for g in victorytable[network][user].keys():
						percentedlist=[]
						for this in victorytable[network][user][g]:
							percentedlist.append(str(this)+"%")
						linelist.append("Scores for "+g+" under the name "+user+": "+list2string(percentedlist).replace("'",""))
					#line=list2string(victorytable[network][user][g])
				if line:
					pmsomebigline(line, data, network)
				if linelist:
					for ll in linelist:
						pmsomebigline(ll, data, network)
	except:
		print_exc()

#do a function, check the sender	

def showoverallscore(user, game, data, network):
	try:
		vtable=open("legionscoreboard", "r")
		victorytable=ast.literal_eval(vtable.read())
		for thek in victorytable[network].keys():
			if thek.lower()==user.lower():
				if game!=None:
					theaverage=averagefinder(victorytable[network][user][game])
					if theaverage:
						legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+nickanick(data)+" :Average score for "+game+" under the name "+user+": "+str(ceil(theaverage))+"%\r\n"))
				else:
					finallist=[]
					for g in victorytable[network][user].keys():
						finallist+=victorytable[network][user][g]
						
					theaverage=averagefinder(finallist)
					if theaverage:
						legionconfig[network][5].send(bytesgoutf8( "PRIVMSG "+nickanick(data)+" :Average score for all games under the name "+user+": "+str(ceil(theaverage))+"%\r\n"))
	except:
		print_exc()


def nickanick(string):
	if ":" in string and "!" in string:
		return string.split(":")[1].split("!")[0]
	else:
		return ""
		

def nickachan(string):

#:Spiffy!sarah@the.byte.is.life PRIVMSG #bulbagarden :https://www.youtube.com/watch?v=OyaePcQqrrQ
	if " #" in string and " :" in string:
		try:
			return "#"+string.split(":")[1].split( " #")[1].split(" :")[0].rstrip()
		except:
			return ""
	else:
		return ""


def stringsender(string, recipient, network):
	legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+recipient+" :"+string+"\r\n"))

def sendastringtowho(string, data, network):
	if " PRIVMSG "+legionconfig[network][0]+" :" not in data and " PRIVMSG #" in data:#the data being judged
		#send to channel
		cleanchan=data.split("PRIVMSG #")[1]
		cleanchan=cleanchan.split(" :")[0]
		#could it just return the next part of the string
		legionconfig[network][5].send(bytesgoutf8("PRIVMSG #"+cleanchan+" :"+string+"\r\n"))
	else:
		cleanuser=data.split(" PRIVMSG ")[0]
		cleanuser=nickanick(cleanuser)
		legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+cleanuser+" :"+string+"\r\n"))
		#send to user

def pmsomebigline(line, data, network):
	if len(line)>400:
		cf= lambda s,p: [ s[i:i+p] for i in range(0,len(s),p) ]
		choppedline=cf(line, 400)
		for x in choppedline:
			legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+nickanick(data)+" :"+x+"\r\n"))
	else:
		legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+nickanick(data)+" :"+line+"\r\n"))

#dict: userlists, channame as key, value as list of users

def unescape(text):
	def fixup(m):
		text = m.group(0)
		if text[:2] == "&#":
			# character reference
			try:
				if text[:3] == "&#x":
					return chr(int(text[3:-1], 16))
				else:
					return chr(int(text[2:-1]))
			except ValueError:
				pass
		else:
			# named entity
			try:
				text = chr(html.entities.name2codepoint[text[1:-1]])
			except KeyError:
				pass
		return text # leave as is
	return re.sub("&#?\w+;", fixup, text)

def addscoretoscoreboard(user, game):
	try:
		vtable=open("legionscoreboard", "r")
		victorytable=ast.literal_eval(vtable.read())
	except:
		victorytable=open("legionscoreboard", "w")
		victorytable.write(repr({}))
		victorytable.close()
		vtable=open("legionscoreboard", "r").read()
		victorytable=ast.literal_eval(vtable)
	try:
		victorytable[legionconfig[2]][user][game].append(grade)
	except:
		try:
			victorytable[legionconfig[2]][user][game]=[]
			victorytable[legionconfig[2]][user][game].append(grade)
		except:
			try:
				victorytable[legionconfig[2]][user]={}
				victorytable[legionconfig[2]][user][game]=[]
				victorytable[legionconfig[2]][user][game].append(grade)
			except:
				try:
												
					victorytable[legionconfig[2]]={}
					victorytable[legionconfig[2]][user]={}
					victorytable[legionconfig[2]][user][game]=[]
					victorytable[legionconfig[2]][user][game].append(grade)
				except:
					pass
					
	vtable=open("legionscoreboard", "w")
	vtable.write(repr(victorytable))
	vtable.close()

def getatrope():
	htmletter=opener.open("http://tvtropes.org/pmwiki/randomitem.php?p=1").read().decode("latin-1")
	return htmletter

def gettropeexample():
	sentry=1
	while sentry==1:
		title=""
		truehtml=""
		cutme=0
		htmlette=None
		listtodel=[]
		cutonme=0
		newihtmlette=""
		newtitlesection=""
		newhtmlette=""
		cutting=""
		while not htmlette:
			htmlette=getatrope()
		htmlette=htmlette.split("\n")

		for i in range(0,len(htmlette)):
			if "folderlabel" in htmlette[i] or "asscaps" in htmlette[i] or "\"indent\"" in htmlette[i] or "'indent'" in htmlette[i]:
				listtodel.append(i)
			elif htmlette[i].count("</a>")==1 and "</li><li> <a class=\"twikilink\">" in htmlette[i] or htmlette[i].count("</a>")==1 and "</li><li> <a class='twikilink'>" in htmlette[i]:
				listtodel.append(i)

		for i in reversed(listtodel):
			del htmlette[i]
		
		for i in range(0,len(htmlette)):
			if "<h2>" in htmlette[i] or "Examples" in htmlette[i] and "</strong>" in htmlette[i]:
				cutting=htmlette[i]
				cutonme=i
				break
		
		cutonmenow=cutonme-1
		titlesection=htmlette[0:cutonmenow]
		htmlette=htmlette[cutonme:]
		
		for i in titlesection:
			newtitlesection+=(i+"\n")
		
		for i in htmlette:
			if not "setAllFolders('');" in i:
				newihtmlette+=(i+"\n")
			else:
				break
		try:
			newihtmlette=newihtmlette.split(cutting)[1]
			for i in newihtmlette:
				newhtmlette+=(i)
			
			htmler = lxml.html.fromstring(newhtmlette)
			titlehtml = lxml.html.fromstring(newtitlesection)
			#titlehtml=titlehtml.text_content().encode("utf-8").lstrip()
			titlehtml=titlehtml.text_content().strip()#.decode("latin-1").lstrip()
			#htmler=htmler.text_content().encode("utf-8")
			htmler=htmler.text_content()#.decode("latin-1")
			try:
				title=titlehtml.split(" - TV Tropes")[0]
			except:
				title=titlehtml.split(" - TV Tropes")[0]
					
			examples=[]
			examples=htmler.split("\n")[:-1]
			try:
				examples.remove("")
			except:
				pass
			
			for i in range(0,len(examples)):
				try:
					if examples[i][0]==" ":
						examples[i]=examples[i].lstrip()
				except:
					pass
			nowant=[]
			for i in range(0,len(examples)):
				if len(examples[i])<40 or examples[i][-1]==":" or title.lower() in examples[i].lower():
					nowant.append(i)
			for p in reversed(nowant):
				del examples[p]
			if len(examples)>0:
				sentry=0
		except:
			print_exc()
	examples=examples[:-1]
	choice=random.choice(examples)
	return title, choice

def asktrope(gamer):
	thetrope, theexample=gettropeexample()
	
	print(thetrope,"is your trope.")#,chardet.detect(thetrope)["encoding"]
	if len(theexample)>400:
		msg=theexample
		cf= lambda s,p: [ s[i:i+p] for i in range(0,len(s),p) ]
		newmessages=cf(msg, 400)

		for x in newmessages:
			legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+gamer+" :"+x+"\r\n"))
	else:
		legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+gamer+" :"+theexample+"\r\n"))
	return thetrope
#now for the command functions...gotta keep everything untangled

def getapokemon(gamer):
	numnum=random.randrange(1, 722)
	thepokedict=open("pokedex", "rt")
	pokedex=eval(thepokedict.read())
	thepokedict.close()
	hint=pokedex[numnum][0]
	#you either get a pokedex entry or a "This is a Grass type..."
#	hint=pokedex[numnum][0].encode("utf-8")#you either get a pokedex entry or a "This is a Grass type..."
#	print("The hint is",hint)
	entry=random.choice(pokedex[numnum][2])
	pokemon=pokedex[numnum][1]
	print(pokemon+" is your Pokemon.")
	legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+gamer+" :"+hint+"\r\n"))
	return pokemon, entry
#now for the command functions...gotta keep everything untangled

def legioncussout(data, network):
	cleanuser, cleanme=data.split("PRIVMSG")
	cleanme=cleanme.split(":!")[1]
	if " " not in cleanme:
		cleanme+=" "
	cleanme=cleanme.split(" ")[0]
	cleanme=cleanme.rstrip()
	cleanme=cleanme.rstrip("\r\n")
	cleanme=cleanme.rstrip("\n")
	cleanuser=nickanick(cleanuser)
	sendastringtowho("Now you just shut the fuck up "+cleanuser+", and stick your damn !"+cleanme+" up your asshole, you fucking lazy bastard!", data, network)

#just name the data something special for each function if you have problems?

def localtimereturn(place):
	try:
		titleline=""
		goodline=""
		placeline=""
		timeline=""
		cleaning=""
		urltoopen="http://www.wolframalpha.com/input/?i=time+in+"+urllib.parse.quote_plus(place)
		textofsite=opener.open(urltoopen).read().decode("utf-8").split("\n")

		for line in textofsite:
			if "context.jsonArray.popups.pod_0100.push( {\"stringified\": \"" in line:
				placeline=line
			if "context.jsonArray.popups.pod_0200.push( {\"stringified\": \"" in line:
				timeline=line
		if placeline:
			
		#	try:				cleaning=placeline.split("current time in ")[1]
			cleaning=placeline.split("\",\"mInput")[0].split("\"stringified\": \"current time in ")[1]
			title=unescape("Current time in "+cleaning)#.decode("utf-8")
		#	except:
		#		cleaning=placeline.split("In ")[1]
		#		cleaning=cleaning.split("\",\"mInput")[0]
		#		title=unescape("Current time in "+cleaning).encode("utf-8")
		if timeline:
			cleaning=timeline.split("stringified\": \"")[1]
			cleaning=cleaning.split("\",\"mInput")[0]
			time=cleaning.replace("  ", " ")
		if time and title:
			return title+": "+time
	except:
		print_exc()


def notaselfcase(i, data):
	if data.split(i)[1]:
		return 0
	else:
		return 1

#def jsonstringvalextractor(stringer, value):
#separate sections for numbers and strings
#	return stringer.split

def getweather(searchforme):
	searchforme=searchforme.replace(". ", ", ").replace("St, ", "St. ").replace("st, ", "st. ").replace("ST, ", "ST. ")
	#<Legion>	Current conditions for Detroit, MI: Sunny, 85°F (29°C) Humidity: 72% Wind: SW at 10 mph
	#<Legion>	Thu: Sunny, 99°F/74°F - Fri: Partly Cloudy, 91°F/75°F - Sat: Scattered Thunderstorms, 91°F/73°F - Sun: Scattered Thunderstorms, 87°F/73°F

	#<Spiffy> !weather detroit, mi
	#<Legion> Current conditions for Detroit, Michigan: Heavy Snow, 23°F (-5°C) Humidity: 24% Wind: ENE at 20 mph
	#<Legion> Sat: Partly Cloudy, 23°F/1°F (-5°C/-17°C) - Sun: Snow, 21°F/9°F (-6°C/-12°C) - Mon: Mostly Cloudy, 10°F/-6°F (-12°C/-21°C) - Tue: Partly Cloudy, 5°F/-4°F (-15°C/-20°C) - Wed: Partly Cloudy, 9°F/4°F (-12°C/-15°C)
	#<Spiffy> !weather hell, mi
	#<Legion> Current conditions for Hell, Michigan: Light Snow, 22°F (-5°C) Humidity: 23% Wind: NW at 18 mph
	#<Legion> Sat: Mostly Cloudy, 27°F/-7°F (-2°C/-21°C) - Sun: Snow, 20°F/6°F (-6°C/-14°C) - Mon: Mostly Cloudy, 8°F/-10°F (-13°C/-23°C) - Tue: Mostly Cloudy, 9°F/-7°F (-12°C/-21°C) - Wed: Partly Cloudy, 13°F/2°F (-10°C/-16°C)

#<Legion> Current conditions for Detroit, Michigan: Snow, 23°F/1°F (-5°C/-17°C) Humidity: 77% Wind: WNW at 19 mph/30 kph
#<Legion> Sat: Snow, 23°F/1°F (-5°C/-17°C) - Sun: Chance of Snow, 19°F/9°F (-7°C/-13°C) - Mon: Mostly Cloudy, 14°F/-9°F (-10°C/-23°C) - Tue: Fog, 3°F/-9°F (-16°C/-23°C)

#<Misaka> Current conditions for Detroit, MI: Overcast (24.7°F/-4.1°C). Feels like 14°F/-10°C. Humidity: 81%. Wind: From the WNW at 12.0 MPH Gusting to 13.0 MPH (19.3kph).
#<Misaka> Saturday: Snow. High of 23°F/-5°C. Low of 1°F/-17°C. Sunday: Chance of Snow. High of 19°F/-7°C. Low of 9°F/-13°C. 

	whatisthisplace=""
	url="http://autocomplete.wunderground.com/aq?query="+urllib.parse.quote(searchforme)
	auto=opener.open(url).read().decode("utf-8")
	if "\"name\"" in auto:
		whatisthisplace=auto.split("\"name\"")[1].split("\"")[1]
	if whatisthisplace:
		try:
			rightnow="Current conditions for "+str(whatisthisplace)+": "
			later=""
			if "/q/locid:" in auto:
				autocompleteresult=auto.split("\"l\": \"")[1].split("\",")[0]
				theactualpage="http://api.wunderground.com/api/b49b003cc2b0496f/forecast"+autocompleteresult+".json"
			else:
				autocompleteresult=auto.split("\"zmw\": \"")[1].split("\",")[0]
				theactualpage="http://api.wunderground.com/api/b49b003cc2b0496f/forecast/q/zmw:"+autocompleteresult+".json"
			#theactualpage="http://api.wunderground.com/api/b49b003cc2b0496f/forecast/q/zmw:"+autocompleteresult+".json"
			noreallythepage=opener.open(theactualpage).read().decode("utf-8").split("\"simpleforecast\"")[1].split("\"date\"")[1:]
			for i in range(0, len(noreallythepage)):
				dayoftheweek=noreallythepage[i].split("weekday_short\":\"")[1].split("\"")[0]
				condition=noreallythepage[i].split("conditions\":\"")[1].split("\"")[0]
				highinf=noreallythepage[i].split("fahrenheit\":\"")[1].split("\"")[0]
				lowinf=noreallythepage[i].split("fahrenheit\":\"")[2].split("\"")[0]
				highinc=noreallythepage[i].split("celsius\":\"")[1].split("\"")[0]
				lowinc=noreallythepage[i].split("celsius\":\"")[2].split("\"")[0]
				if i==0:
					averagehumidity=noreallythepage[i].split("avehumidity\": ")[1].split(",")[0]
					winddir=noreallythepage[i].split("avewind\": {")[1].split("dir\": \"")[1].split("\"")[0]
					windspeedenglish=noreallythepage[i].split("avewind\": {")[1].split("mph\": ")[1].split(",")[0]
					windspeedmetric=noreallythepage[i].split("avewind\": {")[1].split("kph\": ")[1].split(",")[0]
					
					#currenturl="http://www.wolframalpha.com/input/?i=weather+"+urllib.parse.quote(whatisthisplace)
					if "/q/locid" in autocompleteresult:
						currenturl="http://www.wunderground.com"+autocompleteresult
					else:
						currenturl="http://www.wunderground.com/cgi-bin/findweather/getForecast?query="+autocompleteresult
					wund=opener.open(currenturl).read().decode("utf-8")
					#print(wund)
					wund=wund.split("curCond")[1]


					#.split("small-3 columns")[0]
#					#</dd><dt>wind:</dt><dd>WSW<span> at </span>3mph</dd><dt>humidity:</dt><dd>59%</dd></span></td><td><h3>T
#					conditions=wolf.split("conditions")[1].split(">")[1].split("</")[0]
#					humidity=wolf.split("</dd><dt>humidity:</dt><dd>")[1].split("</dd></span></td><td>")[0]
#					wind=wolf.split("</dd><dt>wind:</dt><dd>")[1].split("</dd><dt>")[0]

#-4&deg;F
					condition=wund.split("wx-value")[1].split(">")[1].split("</span")[0]
					degrees=wund.split("wx-value")[2].split(">")[1].split("</span")[0]+wund.split("wx-unit")[1].split(">")[1].split("</span")[0].replace("&deg;", "°")
					if "°F" in degrees:
						fdegrees=degrees
						degrees=degrees.split("°F")[0]
						try:
							degrees=float(degrees)
						except:
							degrees=int(degrees)
						cdegrees=((degrees-32)*5)/9.0
						if cdegrees==int(cdegrees):
							cdegrees=int(cdegrees)
						else:
							cdegrees=round(cdegrees, 1)
						cdegrees=str(cdegrees)+"°C"

					elif "°C" in degrees:
						cdegrees=degrees
						degrees=degrees.split("°C")[0]
					
						try:
							degrees=float(degrees)
						except:
							degrees=int(degrees)
						fdegrees=((foundnumber*9)/5.0)+32
						if fdegrees==int(fdegrees):
							fdegrees=int(fdegrees)
						else:
							fdegrees=round(fdegrees, 1)
						fdegrees=str(fdegrees)+"°F"
					#more
					currenthumidity=wund.split("<dfn>Humidity</dfn>")[1].split("wx-value")[1].split(">")[1].split("<")[0]
					thedegrees=fdegrees+" ("+cdegrees+")"
					newbert=thedegrees+", "+condition+", Highs/Lows: "+highinf+"°F/"+lowinf+"°F ("+highinc+"°C/"+lowinc+"°C) Humidity: "+currenthumidity+"% Wind: "+winddir+" at "+windspeedenglish+" mph/"+windspeedmetric+" kph"
					#newbert=thedegrees+", "+condition+", Highs/Lows: "+highinf+"°F/"+lowinf+"°F ("+highinc+"°C/"+lowinc+"°C) Humidity: "+averagehumidity+"% Wind: "+winddir+" at "+windspeedenglish+" mph/"+windspeedmetric+" kph"
					rightnow+=newbert
				if later:
					later+=" - "
				later+=dayoftheweek+": "+condition+", "+highinf+"°F/"+lowinf+"°F ("+highinc+"°C/"+lowinc+"°C)"
			sendastringtowho(rightnow, data, network)
			return later
		except:# AttributeError:
			print_exc()

#def pickasinglenick(userlist, nickstoremove=[]):
