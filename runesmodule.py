#!/usr/bin/env python
# -*- coding: utf-8 -*-
#make a version as a module, a Cast class, the base for different spreads
from random import randint, shuffle, seed
seed()

#eventually, add reverse as an option?
#tarotspreads

class Cast:
	def __init__(self, caststructure):
		self.caststructure=caststructure
		self.runes = ["fehu (cattle)", "uruz (aurochs)", "þurisaz (giant)", "ansuz (Odin)", "raiðo (journey)", "kenaz (torch)", "gebo (gift)", "wunjo (glory)", "hagalaz (hail)", "nauþiz (need, necessity)", "isa (ice)", "jera (year, harvest)", "eihwaz (yew)", "perþ (dice-cup? vulva?)", "algiz (protection)", "sowulo (sun)", "teiwaz (Tyr)", "berkana (birch)", "ehwaz (horse)", "mannaz (man, humankind)", "laguz (water)", "inguz (Ing)", "ðagaz (day)", "OþILA (property)"]
		shuffle(self.runes)
		self.runemeanings={"fehu (cattle)" : "Prosperity, money, wealth, concern with physical and financial needs, goals, promotion, self-esteem, centredness, karma.",
		"uruz (aurochs)" : "Passion, vitality, instinct, wildness, sexuality, fertility, the unconscious, primitive mind, irrationality, shamanic experience, rite of passage.",
		"þurisaz (giant)" : "Hardship, painful event, discipline, knowledge, introspection, focus.",
		"ansuz (Odin)" : "Authority figure, leader, mind & body balance, justice, shaman, clairvoyant.",
		"raiðo (journey)" : "Journey, pilgrimage, change, destiny, quest, progress, life lessons.",
		"kenaz (torch)" : "Wisdom, insight, solution to a problem, creativity, inspiration, enlightenment.",
		"gebo (gift)" : "Gift, offering, relationship, love, marriage, partnership, generosity, unexpected good fortune.",
		"wunjo (glory)" : "Success, recognition of achievements, reward, joy, bliss, achievement of goals, contentment.",
		"hagalaz (hail)" : "Sudden loss, ordeal, destruction, disaster, clearance, testing, karmic lesson, drastic change.",
		"nauþiz (need, necessity)" : "Poverty, hardship, responsibility, discontent, obstacle, frustration.",
		"isa (ice)" : "Inactivity, blockage, stagnation, potential, patience, reflection, withdrawl, rest.",
		"jera (year, harvest)" : "Change, cycle turning, reward, motion, productivity, inevitable development.",
		"eihwaz (yew)" : "Change, initiation, confrontation of fears, turning point, death, transformation.",
		"perþ (dice-cup? vulva?)" : "Rebirth, mystery, magic, divination, fertility, sexuality, new beginning, prophecy.",
		"algiz (protection)" : "Protection, assistance, defence, warning, support, a mentor, an ethical dilemma.",
		"sowulo (sun)" : "Success, positive energy, increase, power, activity, fertility, health.",
		"teiwaz (Tyr)" : "Duty, discipline, responsibility, self-sacrifice, conflict, strength, a wound, physicality, the warrior path.",
		"berkana (birch)" : "Fertility, health, new beginnings, growth, conception, plenty, clearance.",
		"ehwaz (horse)" : "Transportation, motion, assistance, energy, power, communication, will, recklessness.",
		"mannaz (man, humankind)" : "Significator, self, family, community, relationships, social concerns.",
		"laguz (water)" : "Emotions, fears, unconscious mind, things hidden, revelation, intuition, counselling.",
		"inguz (Ing)" : "Work, productivity, bounty, groundedness, balance, connection with the land.",
		"ðagaz (day)" : "Happiness, success, activity, a fulfilling lifestyle, satisfaction.",
		"OþILA (property)" : "Property, land, inheritance, home, permenance, legacy, synthesis, sense of belonging."}
		self.actualcast=[]
		for castpart in caststructure:
				
			index=randint(0, len(self.runes)-1)
			rune=str(self.runes[index])
			self.runes.pop(index)
			#Who says I can't tie the rune and the meaning together, because of the lack of reverse meanings?
			theline=castpart+" "+rune+": "+self.runemeanings[rune]
			self.actualcast.append(theline)
	
class OneRune(Cast):
	def __init__(self):
		Cast.__init__(self, ["The rune:"])

class TheNorns(Cast):
	def __init__(self):
		Cast.__init__(self, ["Past:", "Present:", "Future:"])

class TheRomanMethod(Cast):
	def __init__(self):
		Cast.__init__(self, ["Rune 1:", "Rune 2:", "Rune 3:"])

class FiveRune(Cast):
	def __init__(self):
		Cast.__init__(self, ["Present:", "Past:", "Help you can expect:", "Unchangable things:", "Future:"])

class SevenRune(Cast):
	def __init__(self):
		Cast.__init__(self, ["Problem 1:", "Problem 2:", "Past factors 1:", "Past factors 2:", "Advice 1:", "Advice 2:", "Result:"])

class NineRuneCast(Cast):
	def __init__(self):
		Cast.__init__(self, ["Rune 1:", "Rune 2:", "Rune 3:", "Rune 4:", "Rune 5:", "Rune 6:", "Rune 7:", "Rune 8:", "Rune 9:"])

#if __name__ == "__main__":
#	run()
