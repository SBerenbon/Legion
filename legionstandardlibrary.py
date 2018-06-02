#from legion import legionconfig
scriptfinder = re.compile(r'<script[\s\S]+?/script>')

def splitOnJustFirstInstance(theString, theToken):
	return theString.split(theString.split(theToken)[0]+theToken)[1]

def splitOnJustLastInstance(theString, theToken):
	return theString.split(theToken+theString.split(theToken)[-1])[0]

def dictprint(thedict):
	finalstring="{"
	for i in sorted(thedict.keys()):
		finalstring+="'"+i+"':{"
		for j in sorted(thedict[i].keys()):
			finalstring+="'"+j+"':"+repr(thedict[i][j])+",\n"
		finalstring+="},\n"
	finalstring+="}"
	return finalstring

def opentoread(nameoffile):
	f=open(nameoffile, "r")
	ff=f.read().replace("\r\n", "\n").replace("\r", "\n")
	f.close()
	return ff

def writethistothis(contents, nameoffile):
	fil=open(nameoffile, "w")
	fil.write(contents)
	fil.close()

def getdata(network):
	data=""
	data = legionconfig[network][5].recv ( 4096 )
	try:
		data=data.decode("utf-8")
	except:
		try:
			data=data.decode("latin-1")
		except:
			try:
				data=str(data)
			except:
				print_exc()
	data=data.strip("\r\n")
	data=data.strip("\n")
	data=data.strip()
	return data

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
		

<<<<<<< HEAD
def nickachan(string):
	if " #" in string and " :" in string:
		try:
			return "#"+string.split(" PRIVMSG")[1].split( " #")[1].split(" :")[0].strip()
<<<<<<< HEAD
=======
=======
	if " #" in string and " :" in string:
		try:
			return "#"+string.split(":")[1].split( " #")[1].split(" :")[0].strip()
>>>>>>> 5edf3822feeb55996b6022058d90c8b58ca58781
>>>>>>> 0df60148fa541a25d832bb4e9d26f0446c445007
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

def sendastringtotheop(network, string):
	legionconfig[network][5].send(bytesgoutf8("PRIVMSG "+legionconfig[network][1]+" :"+string+"\r\n"))

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
		title=htmlette.split("</title>")[0].split(">")[-1].split(" - TV Tropes")[0]
		htmlette=htmlette.split("<div id=\"proper-ad-tvtropes_content_2\">")[1].split("<div id=\"proper-ad-tvtropes_content_1\">")[0]
		if "<div class=\"alt-titles section section-fact\">" in htmlette:
			htmlette=htmlette.split("<div class=\"alt-titles section section-fact\">")[0]
		for i in re.findall(scriptfinder,htmlette):
			htmlette=htmlette.replace(i, "")
		try:
			for i in newihtmlette:
				newhtmlette+=(i)
			
			htmler = lxml.html.fromstring(htmlette).text_content().strip()
			examples=[]
			examples=htmler.split("\n")[:-1]
			try:
				examples.remove("")
			except:
				pass
			
			for i in range(0,len(examples)):
				try:
					if examples[i][0]==" ":
						examples[i]=examples[i].strip()
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
	whatisthisplace=""
	url="http://autocomplete.wunderground.com/aq?query="+urllib.parse.quote(searchforme)
	auto=opener.open(url).read().decode("utf-8")
	if "\"name\"" in auto:
		whatisthisplace=auto.split("\"name\"")[1].split("\"")[1]
	if whatisthisplace:
		try:
			rightnow="Current conditions for "+str(whatisthisplace)+": "
			later=""
			if "/q/zmw:" in auto:
				autocompleteresult=auto.split("\"l\": \"")[1].split("\",")[0]
				theactualpage="http://api.wunderground.com/api/b49b003cc2b0496f/forecast"+autocompleteresult+".json"
			else:
				autocompleteresult=auto.split("\"zmw\": \"")[1].split("\",")[0]
				theactualpage="http://api.wunderground.com/api/b49b003cc2b0496f/forecast/q/zmw:"+autocompleteresult+".json"
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
					
					try:
						autocompleteresult=autocompleteresult.split("/q/zmw:")[1]
						currenturl="https://www.wunderground.com/q/locid/"+autocompleteresult
						print(currenturl)
						wund=opener.open(currenturl).read().decode("utf-8")
						wund=wund.split("curCond")[1]
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
							fdegrees=((degrees*9)/5.0)+32
							if fdegrees==int(fdegrees):
								fdegrees=int(fdegrees)
							else:
								fdegrees=round(fdegrees, 1)
							fdegrees=str(fdegrees)+"°F"
						#more
						currenthumidity=wund.split("<dfn>Humidity</dfn>")[1].split("wx-value")[1].split(">")[1].split("<")[0]
						thedegrees=fdegrees+" ("+cdegrees+")"
						newbert=thedegrees+", "+condition+", Highs/Lows: "+highinf+"°F/"+lowinf+"°F ("+highinc+"°C/"+lowinc+"°C) Humidity: "+currenthumidity+"% Wind: "+winddir+" at "+windspeedenglish+" mph/"+windspeedmetric+" kph"
						rightnow+=newbert
					except urllib.error.HTTPError:
						currenturl="http://www.wunderground.com/cgi-bin/findweather/getForecast?query="+urllib.parse.quote(searchforme)+"?hdf=1"

						wund=opener.open(currenturl).read().decode("utf-8")
						if "</display-unit>" not in wund and "td><a href=\"/weather/" in wund:
							currenturl="https://www.wunderground.com/weather/"+wund.split("td><a href=\"/weather/")[1].split("\"")[0]
							print(currenturl)
							wund=opener.open(currenturl).read().decode("utf-8")
						condition=wund.split("</display-unit>")[2].split("condition-icon ")[1].split("p _ngcontent")[1].split(">")[1].split("<")[0]
						degreeunit="°"+wund.split("units_nosymbol\":\"")[1].split("\"")[0]
						degrees=wund.split("class=\"current-temp\"")[1].split("wu-value wu-value-to")[1].split(">")[1].split("<")[0]+degreeunit
						#print(degrees)
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
							fdegrees=((degrees*9)/5.0)+32
							if fdegrees==int(fdegrees):
								fdegrees=int(fdegrees)
							else:
								fdegrees=round(fdegrees, 1)
							fdegrees=str(fdegrees)+"°F"
						#more
						currenthumidity=wund.split("\"humidity\":")[1].split(",")[0]
						thedegrees=fdegrees+" ("+cdegrees+")"
						newbert=thedegrees+", "+condition+", Highs/Lows: "+highinf+"°F/"+lowinf+"°F ("+highinc+"°C/"+lowinc+"°C) Humidity: "+currenthumidity+"% Wind: "+winddir+" at "+windspeedenglish+" mph/"+windspeedmetric+" kph"
						rightnow+=newbert

				if later:
					later+=" - "
				later+=dayoftheweek+": "+condition+", "+highinf+"°F/"+lowinf+"°F ("+highinc+"°C/"+lowinc+"°C)"
			sendastringtowho(rightnow, data, network)
			return later
		except:# AttributeError:
			print_exc()

#def pickasinglenick(userlist, nickstoremove=[]):
