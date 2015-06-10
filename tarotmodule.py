#!/usr/bin/env python
# -*- coding: utf-8 -*-
#make a version as a module, a Spread class, the base for different spreads
from random import randint, shuffle, seed
seed()

#store all the "Card 1, wisdom" etc in lists, so the individual spreads don't look ugly

#eventually, add reverse as an option?
#tarotspreads

class Spread:
	def __init__(self, spreadstructure, personspread):
		self.spreadstructure=spreadstructure
		self.packofcards = ("00 - The Fool", "01 - The Magician", "02 - The High Priestess", "03 - The Empress", "04 - The Emperor", "05 - The Hierophant", "06 - The Lovers", "07 - The Chariot", "08 - Strength", "09 - The Hermit", "10 - Wheel of Fortune", "11 - Justice", "12 - The Hanged Man", "13 - Death", "14 - Temperence", "15 - The Devil", "16 - The Tower", "17 - The Star", "18 - The Moon", "19 - The Sun", "20 - Judgement", "21 - The World")
		self.packofnumbercards = ("Cups - Ace", "Cups - 02", "Cups - 03", "Cups - 04", "Cups - 05", "Cups - 06", "Cups - 07", "Cups - 08", "Cups - 09", "Cups - 10", "Pentacles - Ace", "Pentacles - 02", "Pentacles - 03", "Pentacles - 04", "Pentacles - 05", "Pentacles - 06", "Pentacles - 07", "Pentacles - 08", "Pentacles - 09", "Pentacles - 10", "Swords - Ace", "Swords - 02", "Swords - 03", "Swords - 04", "Swords - 05", "Swords - 06", "Swords - 07", "Swords - 08", "Swords - 09", "Swords - 10", "Wands - Ace", "Wands - 02", "Wands - 03", "Wands - 04", "Wands - 05", "Wands - 06", "Wands - 07", "Wands - 08", "Wands - 09", "Wands - 10")
		self.packofpeoplecards = ("Cups - King", "Cups - Queen", "Cups - Knight", "Cups - Page", "Pentacles - King", "Pentacles - Queen", "Pentacles - Knight", "Pentacles - Page", "Swords - King", "Swords - Queen", "Swords - Knight", "Swords - Page", "Wands - King", "Wands - Queen", "Wands - Knight", "Wands - Page")
		self.cards=list(self.packofcards)+list(self.packofnumbercards)+list(self.packofpeoplecards)
		shuffle(self.cards)
		self.tarotmeanings={"00 - The Fool" : "Folly, mania, extravagance, intoxication, delirium, frenzy, bewrayment.",
		"01 - The Magician" : "Skill, diplomacy, address, subtlety; sickness, pain, loss, disaster, snares of enemies; self-confidence, will; the Querent, if male.",
		"02 - The High Priestess" : "Secrets, mystery, the future as yet unrevealed; the woman who interests the Querent, if male; the Querent herself, if female; silence, tenacity; mystery, wisdom, science.",
		"03 - The Empress" : "Fruitfulness, action, initiative, length of days; the unknown, clandestine; also difficulty, doubt, ignorance.",
		"04 - The Emperor" : "Stability, power, protection, realization; a great person; aid, reason, conviction; also authority and will.",
		"05 - The Hierophant" : "Marriage, alliance, captivity, servitude; by another account, mercy and goodness; inspiration; the man to whom the Querent has recourse.",
		"06 - The Lovers" : "Attraction, love, beauty, trials overcome.",
		"07 - The Chariot" : "Succour, providence; also war, triumph, presumption, vengeance, trouble.",
		"08 - Strength" : "Power, energy, action, courage, magnanimity; also complete success and honours.",
		"09 - The Hermit" : "Prudence, circumspection; also and especially treason, dissimulation, roguery, corruption.",
		"10 - Wheel of Fortune" : "Destiny, fortune, success, elevation, luck, felicity.",
		"11 - Justice" : "Equity, rightness, probity, executive; triumph of the observing side in law.",
		"12 - The Hanged Man" : "Wisdom, circumspection, discernment, trials, sacrifice, intuition, divination, prophecy.",
		"13 - Death" : "End, mortality, destruction, corruption; also for a man, the loss of a benefactor; for a woman, many contrarieties; for a maid, failure of marriage projects.",
		"14 - Temperence" : "Economy, moderation, frugality, management, accommodation.",
		"15 - The Devil" : "Ravage, violence, vehemence, extraordinary efforts, force, fatality; that which is predestined but is not for this reason evil.",
		"16 - The Tower" : "Misery, distress, indigence, adversity, calamity, disgrace, deception, ruin. It is a card in particular of unforeseen catastrophe.",
		"17 - The Star" : "Loss, theft, privation, abandonment; another reading says--hope and bright prospects.",
		"18 - The Moon" : "Hidden enemies, danger, calumny, darkness, terror, deception, occult forces, error.",
		"19 - The Sun" : "Material happiness, fortunate marriage, contentment.",
		"20 - Judgement" : "Change of position, renewal, outcome. Another account specifies total loss through lawsuit.",
		"21 - The World" : "Assured success, recompense, voyage, route, emigration, flight, change of place.",
		"Cups - 02" : "Love, passion, friendship, affinity, union, concord, sympathy, the interrelation of the sexes, and--as a suggestion apart from all offices of divination--that desire which is not in Nature, but by which Nature is sanctified. Additional Meanings: Favourable in things of pleasure and business, as well as love; also wealth and honour.",
		"Cups - 03" : "The conclusion of any matter in plenty, perfection and merriment; happy issue, victory, fulfillment, solace, healing. Additional Meanings: Unexpected advancement for a military man.",
		"Cups - 04" : "Weariness, disgust, aversion, imaginary vexations, as if the wine of this world had caused satiety only; another wine, as if a fairy gift, is now offered the wastrel, but he sees no consolation therein. This is also a card of blended pleasure. Additional Meanings: Contrarieties.",
		"Cups - 05" : "It is a card of loss, but something remains over; three have been taken, but two are left; it is a card of inheritance, patrimony, transmission, but not corresponding to expectations; with some interpreters it is a card of marriage, but not without bitterness or frustration. Additional Meanings: Generally favourable; a happy marriage; also patrimony, legacies, gifts, success in enterprise. ",
		"Cups - 06" : "A card of the past and memories, looking back, as--for example--on childhood; happiness, enjoyment, but coming rather from the past; things that have vanished. Another reading reverses this, giving new relations, new knowledge, new environment, and then the children are disporting in an unfamiliar precinct. Additional Meanings: Pleasant memories.",
		"Cups - 07" : "Fairy favours, images of reflection, sentiment, imagination, things seen in the glass of contemplation; some attainment in these degrees, but nothing permanent or substantial is suggested. Additional Meanings: Fair child; idea, design, resolve, movement.",
		"Cups - 08" : "The card speaks for itself on the surface, but other readings are entirely antithetical--giving joy, mildness, timidity, honour, modesty. In practice, it is usually found that the card shews the decline of a matter, or that a matter which has been thought to be important is really of slight consequence--either for good or evil. Additional Meanings: Marriage with a fair woman.",
		"Cups - 09" : "Concord, contentment, physical bien-être [well-being]; also victory, success, advantage; satisfaction for the Querent or person for whom the consultation is made. Additional Meanings: Of good augury for military men.",
		"Cups - 10" : "Contentment, repose of the entire heart; the perfection of that state; also perfection of human love and friendship; if with several picture-cards, a person who is taking charge of the Querent's interests; also the town, village or country inhabited by the Querent. Additional meanings: For a male Querent, a good marriage and one beyond his expectations.",
		"Cups - Ace" : "House of the true heart, joy, content, abode, nourishment, abundance, fertility; Holy Table, felicity hereof. Additional Meanings: Inflexible will, unalterable law.",
		"Cups - King" : "Fair man, man of business, law, or divinity; responsible, disposed to oblige the Querent; also equity, art and science, including those who profess science, law and art; creative intelligence. Additional meanings: Beware of ill-will on the part of a man of position, and of hypocrisy pretending to help.",
		"Cups - Knight" : "Arrival, approach--sometimes that of a messenger; advances, proposition, demeanor, invitation, incitement. Additional meanings: A visit from a friend, who will bring unexpected money to the Querent.",
		"Cups - Page" : "Fair young man, one impelled to render service and with whom the Querent will be connected; a studious youth; news, message; application, reflection, meditation; also those things directed to business. Additional meanings: Good augury; also a young man who is unfortunate in love.",
		"Cups - Queen" : "Good, fair woman; honest, devoted woman, who will do service to the Querent; loving intelligence, and hence the gift of vision; success, happiness, pleasure; also wisdom, virtue; a perfect spouse and a good mother. Additional meanings: Sometimes denotes a woman of equivocal character.",
		"Pentacles - 02" : "On the one hand it is represented as a card of gaiety, recreation and its connexions, which is the subject of the design; but it is read also as news and messages in writing, as obstacles, agitation, trouble, embroilment. Additional Meanings: Troubles are more imaginary than real.",
		"Pentacles - 03" : "Métier, trade, skilled labour; usually, however, regarded as a card of nobility, aristocracy, renown, glory. Additional Meanings: If for a man, celebrity for his eldest son.",
		"Pentacles - 04" : "The surety of possessions, cleaving to that which one has, gift, legacy, inheritance. Additional Meanings: For a bachelor, pleasant news from a lady.",
		"Pentacles - 05" : "The card foretells material trouble above all, whether in the form illustrated--that is, destitution--or otherwise. For some cartomancists, it is a card of love and lovers--wife, husband, friend, mistress; also concordance, affinities. These alternatives cannot be harmonized. Additional Meanings: Conquest of Fortune by Reason.",
		"Pentacles - 06" : "Presents, gifts, gratification; another account says attention, vigilance; now is the accepted time, present prosperity, etc. Additional Meanings: The present must not be relied on.",
		"Pentacles - 07" : "These are exceedingly contradictory; in the main; it is a card of money, business, barter; but one reading gives altercation, quarrel--and another innocence, ingenuity, purgation. Additional Meanings: Improved position for a lady's future husband.",
		"Pentacles - 08" : "Work, employment, commission, craftsmanship, skill in craft and business, perhaps in the preparatory stage. Additional Meanings: A young man in business who has relations with the Querent; a dark girl.",
		"Pentacles - 09" : "Prudence, safety, success, accomplishment, certitude, discernment. Additional Meanings: Prompt fulfillment of what is presaged by neighbouring cards.",
		"Pentacles - 10" : "Gain, riches; family matters, archives, extraction, the abode of a family. Additional Meanings: Represents house or dwelling, and derives its value from other cards.",
		"Pentacles - Ace" : "Perfect contentment, felicity, ecstasy; also speedy intelligence; gold. Additional Meanings: The most favourable of all cards.",
		"Pentacles - King" : "Valour, realizing intelligence, business and normal intellectual aptitude, sometimes mathematical gifts and attainments of this kind; success in these paths. Additional Meanings: A rather dark man, a merchant, master, professor.",
		"Pentacles - Knight" : "Utility, serviceableness, interest, responsibility, rectitude--all on the normal and external plane. Additional Meanings: An useful man; useful discoveries.",
		"Pentacles - Page" : "Application, study, scholarship, reflection; another reading says news, messages and the bringer thereof; also rule, management. Additional Meanings: A dark youth; a young officer or soldier; a child.",
		"Pentacles - Queen" : "Opulence, generosity, magnificence, security, liberty. Additional Meanings: Dark woman; presents from a rich relative; rich and happy marriage for a young man.",
		"Swords - 02" : "Conformity, and the equipoise which it suggests, courage, friendship, concord in a state of arms; another reading gives tenderness, affection, intimacy. The suggestion of harmony and other favourable readings must be considered in a qualified manner, as Swords generally are not symbolical of beneficent force in human affairs. Additional Meanings: Gifts for a lady, influential protection for a man in search of help.",
		"Swords - 03" : "Removal, absence, delay, division, rupture, dispersion, and all that the design signifies naturally, being too simple and obvious to call for specific enumeration. Additional Meanings: For a woman, the flight of her lover.",
		"Swords - 04" : "Vigilance, retreat, solitude, hermit's repose, exile, tomb and coffin. It is these last that have suggested the design. Additional Meanings: A bad card, but if reversed a qualified success may be expected by wise administration of affairs.",
		"Swords - 05" : "Degradation, destruction, revocation, infamy, dishonour, loss, with the variants and analogues of these. Additional Meanings: An attack on the fortune of the Querent.",
		"Swords - 06" : "Journey by water, route, way, enjoy, commissionary, expedient. Additional Meanings: The voyage will be pleasant.",
		"Swords - 07" : "Design, attempt, wish, hope, confidence; also quarrelling, a plan that may fail, annoyance. The design is uncertain in its import, because the significations are widely at variance with each other. Additional meanings: Dark girl; a good card; it promises a country life after a competence has been secured.",
		"Swords - 08" : "Bad news, violent chagrin, crisis, censure, power in trammels, conflict, calumny, also sickness. Additional Meanings: For a woman, scandal spread in her respect.",
		"Swords - 09" : "Death, failure, miscarriage, delay, deception, disappointment, despair. Additional meanings: An ecclesiastic, a priest; generally, a card of bad omen.",
		"Swords - 10" : "Whatsoever is intimated by the design; also pain, affliction, tears, sadness, desolation. It is not especially a card of violent death. Additional Meanings: Followed by Ace and King, imprisonment; for girl or wife, treason on the part of friends.",
		"Swords - Ace" : "Triumph, the excessive degree in everything, conquest, triumph of force. It is a card of great force, in love as well as in hatred. The crown may carry a much higher significance than comes usually within the sphere of fortune-telling. Additional Meanings: Great prosperity or great misery.",
		"Swords - King" : "Whatsoever arises out of the idea of judgment and all its connexions--power, command, authority, militant intelligence, law offices of the crown, and so forth. Additional Meanings: A lawyer, senator, doctor.",
		"Swords - Knight" : "Skill, bravery, capacity, defence, address, enmity, wrath, war, destruction, opposition, resistance, ruin. There is therefore a sense in which the card signifies death, but it carries this meaning only in its proximity to other cards of fatality. Additional Meanings: A soldier, man of arms, satellite, stipendiary; heroic action predicted for soldier.",
		"Swords - Page" : "Authority, overseeing, secret service, vigilance, spying, examination, and the qualities thereto belonging. Additional Meanings: An indiscreet person will pry into the Querent's secrets.",
		"Swords - Queen" : "Widowhood, female sadness and embarrassment, absence, sterility, mourning, privation, separation. Additional Meanings: A widow.",
		"Wands - 02" : "Between the alternative readings there is no marriage possible; on the one hand, riches, fortune, magnificence; on the other, physical suffering, disease, chagrin, sadness, mortification. The design gives one suggestion; here is a lord overlooking his dominion and alternately contemplating a globe; it looks like the malady, the mortification, the sadness of Alexander amidst the grandeur of this world's wealth. Additional Meanings: A young lady may expect trivial disappointments.",
		"Wands - 03" : "He symbolizes established strength, enterprise, effort, trade, commerce, discovery; those are his ships, bearing his merchandise, which are sailing over the sea. The card also signifies able co-operation in business, as if the successful merchant prince were looking from his side towards yours with the view to help you. Additional Meanings: A very good card; collaboration will favour enterprise.",
		"Wands - 04" : "The divinatory meanings are for once almost on the surface--country life, haven of refuge, a species of domestic harvest-home, repose, concord, harmony, prosperity, peace, and the perfected work of these. Additional Meanings: Unexpected good fortune. ",
		"Wands - 05" : "Imitation, as, for example, sham fight, but also the strenuous competition and struggle of the search after riches and fortune. In this sense it connects with the battle of life. Hence some attributions say that it is a card of gold, gain, opulence. Additional Meanings: Success in financial speculation.",
		"Wands - 06" : "The card has been so designed that it can cover several significations; on the surface, it is a victor triumphing, but it is also great news, such as might be carried in state by the King's courier; it is expectation crowned with its own desire, the crown of hope, and so forth. Additional meanings: Servants may lose the confidence of their masters; a young lady may be betrayed by a friend.",
		"Wands - 07" : "It is a card of valour, for, on the surface, six are attacking one, who has however, the vantage of position. On the intellectual plane, it signifies discussion, wordy strife; in business--negotiations, war of trade, barter, competition. It is further a card of success, for the combatant is on the top and his enemies may be unable to reach him. Additional Meanings: A dark child.",
		"Wands - 08" : "Activity in undertakings, the path of such activity, swiftness as that of an express messenger; great haste, great hope, speed towards an end which promises assured felicity; generally, that which is on the move; also the arrows of love. Additional meanings: Domestic disputes for a married person.",
		"Wands - 09" : "The card signifies strength in opposition. If attacked, the person will meet an onslaught boldly; and his build shews that he may prove a formidable antagonist. With this main significance there are all its possible adjuncts--delay, suspension, adjournment. Additional meanings: Generally speaking, a bad card.",
		"Wands - 10" : "The chief meaning is oppression simply, but it is also fortune, gain, any kind of success, and then it is the oppression of these things. It is also a card of false-seeming, disguise, perfidy. The place which the figure is approaching may suffer from the rods that he carries. Success is stultified if the Nine of Swords follows, and if it is a question of a lawsuit, there will be certain loss. Additional meanings: Difficulties and contradictions, if near a good card.",
		"Wands - Ace" : "Creation, invention, enterprise, the powers which result in these; principle, beginning, source; birth, family, origin, and in a sense the virility which is behind them; the starting point of enterprises; according to another account, money, fortune, inheritance. Additional Meanings: Calamities of all kinds.",
		"Wands - King" : "Dark man, friendly, countryman, generally married, honest and conscientious. The card always signifies honesty, and may mean news concerning an unexpected heritage to fall in before very long. Additional meanings: Generally favourable; may signify a good marriage.",
		"Wands - Knight" : "Departure, absence, flight, emigration. A dark young man, friendly. Change of residence. Additional meaning: A bad card; according to some readings, alienation.",
		"Wands - Page" : "Dark young man, faithful as a lover, an envoy, a postman. Beside a man, he will bear favourable testimony concerning him. Additional meanings: Young man of family in search of young lady.",
		"Wands - Queen" : "Dark woman, countrywoman, friendly, chaste, loving, honourable. If the card beside her signifies a man, she is well disposed towards him; if a woman, she is interested in the Querent. Also, love of money, or a certain success in business. Additional meaning: A good harvest, which may be taken in several senses.",
		"00 - The Fool (Reverse)" : "Negligence, absence, distribution, carelessness, apathy, nullity, vanity.",
		"01 - The Magician (Reverse)" : "Physician, Magus, mental disease, disgrace, disquiet.",
		"02 - The High Priestess (Reverse)" : "Passion, moral or physical ardour, conceit, surface knowledge.",
		"03 - The Empress (Reverse)" : "Light, truth, the unravelling of involved maters, public rejoicings; according to another reading, vacillation.",
		"04 - The Emperor (Reverse)" : "Benevolence, compassion, credit; also confusion to enemies, obstruction, immaturity.",
		"05 - The Hierophant (Reverse)" : "Society, good understanding, concord, over-kindness, weakness.",
		"06 - The Lovers (Reverse)" : "Failure, foolish designs. Another account speaks of marriage frustrated and contrarities of all kinds.",
		"07 - The Chariot (Reverse)" : "Riot, quarrel, dispute, litigation, defeat.",
		"08 - Strength (Reverse)" : "Despotism, abuse of power, weakness, discord, sometimes even disgrace.",
		"09 - The Hermit (Reverse)" : "Concealment, disguise, policy, fear, unreasoned caution.",
		"10 - Wheel of Fortune (Reverse)" : "Increase, abundance, superfluity.",
		"11 - Justice (Reverse)" : "Law in all departments, legal complications, bigotry, bias, excessive severity.",
		"12 - The Hanged Man (Reverse)" : "Selfishness, the crowd, body politic.",
		"13 - Death (Reverse)" : "Intertia, sleep, lethargy, petrifaction, somnambulism; hope destroyed.",
		"14 - Temperence (Reverse)" : "Things connected with churches, religions, sects, the priesthood, sometimes even the priest who will marry the Querent; also disunion, unfortunate combinations, competing interests.",
		"15 - The Devil (Reverse)" : "Evil fatality, weakness, blindness.",
		"16 - The Tower (Reverse)" : "According to one account, the same in a lesser degree; also oppression, imprisonment, tyranny.",
		"17 - The Star (Reverse)" : "Arrogance, haughtiness, impotence.",
		"18 - The Moon (Reverse)" : "Instability, inconstancy, silence, lesser degrees of deception and error.",
		"19 - The Sun (Reverse)" : "Material happiness, fortunate marriage, contentment, in a lesser sense.",
		"20 - Judgement (Reverse)" : "Weakness, pusillanimity, simplicity; also deliberation, decision, sentence.",
		"21 - The World (Reverse)" : "Inertia, fixity, stagnation, permanence.",
		"Cups - 02 (Reverse)" : "Passion",
		"Cups - 03 (Reverse)" : "Expedition, dispatch, achievement, end. It signifies also the side of excess in physical enjoyment, and the pleasures of the senses. Additional Meanings: Consolation, cure, end of the business.",
		"Cups - 04 (Reverse)" : "Novelty, presage, new instruction, new relations. Additional Meanings: Presentiment.",
		"Cups - 05 (Reverse)" : "News, alliances, affinity, consanguinity, ancestry, return, false projects. Additional Meanings: Return of some relative who has not been seen for long.",
		"Cups - 06 (Reverse)" : "The future, renewal, that which will come to pass presently. Additional Meanings: Inheritance to fall in quickly.",
		"Cups - 07 (Reverse)" : "Desire, will, determination, project. Additional Meanings: Success, if accompanied by the Three of Cups.",
		"Cups - 08 (Reverse)" : "Great joy, happiness, feasting. Additional Meanings: Perfect satisfaction.",
		"Cups - 09 (Reverse)" : "Truth, loyalty, liberty; but the readings vary and include mistakes, imperfections, etc. Additional Meanings: Good business.",
		"Cups - 10 (Reverse)" : "Repose of the false heart, indignation, violence. Additional Meanings: Sorrow; also a serious quarrel.",
		"Cups - Ace (Reverse)" : "House of the false heart, mutation, instability, revolution. Additional Meanings: Unexpected change of position.",
		"Cups - King (Reverse)" : "Dishonest, double-dealing man; roguery, exaction, vice, scandal, pillage, considerable loss. Additional meanings: Loss.",
		"Cups - Knight (Reverse)" : "Trickery, artifice, subtlety, swindling, duplicity, fraud. Additional meanings: Irregularity.",
		"Cups - Page (Reverse)" : "Taste, inclination, attachment, seduction, deception, artifice. Additional meanings: Obstacles of all kinds.",
		"Cups - Queen (Reverse)" : "The accounts vary; good woman; otherwise distinguished woman but one not to be trusted; perverse woman; vice, dishonor, depravity. Additional Meanings: A rich marriage for a man and a distinguished one for a woman.",
		"Pentacles - 02 (Reverse)" : "Enforced gaiety, simulated enjoyment, literal sense, handwriting, composition, letters of exchange. Additional Meanings: Bad omen, ignorance, injustice.",
		"Pentacles - 03 (Reverse)" : "Mediocrity, in work and otherwise, puerility, pettiness, weakness. Additional Meanings: Depends on neighbouring cards.",
		"Pentacles - 04 (Reverse)" : "Suspense, delay, opposition. Additional Meanings: Observation, hindrances.",
		"Pentacles - 05 (Reverse)" : "Disorder, chaos, ruin, discord, profligacy. Additional meanings: Troubles in love.",
		"Pentacles - 06 (Reverse)" : "Desire, cupidity, envy, jealousy, illusion. Additional Meanings: A check on the Querent's ambition.",
		"Pentacles - 07 (Reverse)" : "Cause for anxiety regarding money which it may be proposed to lend. Additional Meanings: Impatience, apprehension, suspicion.",
		"Pentacles - 08 (Reverse)" : "Voided ambition, vanity, cupidity, exaction, usury. It may also signify the possession of skill, in the sense of the ingenious mind turned to cunning and intrigue. Additional Meanings: The Querent will be compromised in a matter of money-lending.",
		"Pentacles - 09 (Reverse)" : "Roguery, deception, voided project, bad faith. Additional Meanings: Vain hopes.",
		"Pentacles - 10 (Reverse)" : "Chance, fatality, loss, robbery, games of hazard; sometimes gift, dowry, pension.",
		"Pentacles - Ace (Reverse)" : "The evil side of wealth, bad intelligence; also great riches. In any case it shews prosperity, comfortable material conditions, but whether these are of advantage to the possessor will depend on whether the card is reversed or not. Additional Meanings: A share in the finding of treasure.",
		"Pentacles - King (Reverse)" : "Vice, weakness, ugliness, perversity, corruption, peril. Additional Meanings: An old and vicious man.",
		"Pentacles - Knight (Reverse)" : "Inertia, idleness, repose of that kind, stagnation; also placidity, discouragement, carelessness. Additional Meanings: A brave man out of employment.",
		"Pentacles - Page (Reverse)" : "Prodigality, dissipation, liberality, luxury; unfavourable news. Additional Meanings: Sometimes degradation and sometimes pillage.",
		"Pentacles - Queen (Reverse)" : "Evil, suspicion, suspense, fear, mistrust. Additional Meanings: An illness.",
		"Swords - 02 (Reverse)" : "Imposture, falsehood, duplicity, disloyalty. Additional Meanings: Dealings with rogues.",
		"Swords - 03 (Reverse)" : "Mental alienation, error, loss, distraction, disorder, confusion. Additional Meanings: A meeting with one whom the Querent has compromised; also a nun.",
		"Swords - 04 (Reverse)" : "Wise administration, circumspection, economy, avarice, precaution, testament. Additional Meanings: A certain success following wise administration.",
		"Swords - 05 (Reverse)" : "Degradation, destruction, revocation, infamy, dishonour, loss, with the variants and analogues of these; burial and obsequies. A sign of sorrow and mourning.",
		"Swords - 06 (Reverse)" : "Declaration, confession, publicity; one account says that it is a proposal of love. Additional Meanings: Unfavourable issue of lawsuit.",
		"Swords - 07 (Reverse)" : "Good advice, counsel, instruction, slander, babbling. Additional Meanings: Good advice, probably neglected.",
		"Swords - 08 (Reverse)" : "Disquiet, difficulty, opposition, accident, treachery; what is unforeseen; fatality. Additional Meanings: Departure of a relative.",
		"Swords - 09 (Reverse)" : "Imprisonment, suspicion, doubt, reasonable fear, shame. Additional Meanings: Good ground for suspicion against a doubtful person.",
		"Swords - 10 (Reverse)" : "Advantage, profit, success, favour, but none of these are permanent; also power and authority. Additional Meanings: Victory and consequent fortune for a soldier in war.",
		"Swords - Ace (Reverse)" : "Triumph, the excessive degree in everything, conquest, triumph of force, but the results are disastrous; another account says--conception, childbirth, augmentation, multiplicity. Additional Meanings: Marriage broken off, for a woman, through her own imprudence.",
		"Swords - King (Reverse)" : "Cruelty, perversity, barbarity, perfidy, evil intention. Additional Meanings: A bad man; also a caution to put an end to a ruinous lawsuit.",
		"Swords - Knight (Reverse)" : "Imprudence, incapacity, extravagance. Additional Meanings: Dispute with an imbecile person; for a woman, struggle with a rival, who will be conquered.",
		"Swords - Page (Reverse)" : "Authority, overseeing, secret service, vigilance, spying, examination, and the qualities thereto belonging. More evil side of these qualities; what is unforeseen, unprepared state; sickness is also intimated. Additional Meanings: Astonishing news.",
		"Swords - Queen (Reverse)" : "Malice, bigotry, artifice, prudery, bale, deceit. Additional Meanings: A bad woman, with ill-will towards the Querent.",
		"Wands - 02 (Reverse)" : "Surprise, wonder, enchantment, emotion, trouble, fear.",
		"Wands - 03 (Reverse)" : "The end of troubles, suspension or cessation of adversity, toil and disappointment.",
		"Wands - 04 (Reverse)" : "The meaning remains unaltered; it is prosperity, increase, felicity, beauty, embellishment. Additional Meanings: A married woman will have beautiful children.",
		"Wands - 05 (Reverse)" : "Litigation, disputes, trickery, contradiction. Additional Meanings: Quarrels may be turned to advantage.",
		"Wands - 06 (Reverse)" : "Apprehension, fear, as of a victorious enemy at the gate; treachery, disloyalty, as of gates being opened to the enemy; also indefinite delay. Additional meanings: Fulfillment of deferred hope.",
		"Wands - 07 (Reverse)" : "Perplexity, embarrassments, anxiety. It is also a caution against indecision.",
		"Wands - 08 (Reverse)" : "Arrows of jealousy, internal dispute, stingings of conscience, quarrels; and domestic disputes for persons who are married.",
		"Wands - 09 (Reverse)" : "Obstacles, adversity, calamity.",
		"Wands - 10 (Reverse)" : "Contrarieties, difficulties, intrigues, and the analogies.",
		"Wands - Ace (Reverse)" : "Fall, decadence, ruin, perdition, to perish; also a certain clouded joy. Additional Meanings: A sign of birth.",
		"Wands - King (Reverse)" : "Good, but severe; austere, yet tolerant. Additional meanings: Advice that should be followed.",
		"Wands - Knight (Reverse)" : "Rupture, division, interruption, discord. Additional Meanings: For a woman, marriage, but probably frustrated.",
		"Wands - Page (Reverse)" : "Anecdotes, announcements, evil news. Also indecision and the instability which accompanies it. Additional meanings: Bad news.",
		"Wands - Queen (Reverse)" : "Good, economical, obliging, serviceable. Signifies also--but in certain positions and the neighbourhood of other cards tending in such directions--opposition, jealousy, even deceit and infidelity. Additional meaning: Good will toward the Querent, but without the opportunity to exercise it."}
		self.actualspread=[]
		for spreadpart in spreadstructure:	
			if personspread==1 and len(self.actualspread)==0:
				index=randint(0, len(self.packofpeoplecards)-1)
				card=str(self.packofpeoplecards[index])
				self.cards.remove(card)
			else:
				
				index=randint(0, len(self.cards)-1)
				card=str(self.cards[index])
				self.cards.pop(index)
				#pop or remove?
				isreverse=randint(1,8)
				if isreverse==1:
					card+=" (Reverse)"
			theline=spreadpart+" "+card+": "+self.tarotmeanings[card]
			self.actualspread.append(theline)
	
class ThreeCard(Spread):
	def __init__(self):
		Spread.__init__(self, ["Past:", "Present:", "Future:"], personspread=0)

class FiveCard(Spread):
	def __init__(self):
		Spread.__init__(self, ["Present/General theme:", "Past influences:", "Future:", "Reason behind question:", "Potential:"], personspread=0)

class SevenCardDraw(Spread):
	def __init__(self):
		Spread.__init__(self, ["Essence of the question:", "Inner influences:", "Outer influences:", "Path of action:", "Path of passivity:", "The way of the heart:", "Possible outcome:"], personspread=0)

class Horseshoe(Spread):
	def __init__(self):
		Spread.__init__(self, ["Past:", "Immediate present:", "Immediate future:", "Something occupying querent's mind:", "The attitudes of others:", "An obstacle:", "The final outcome:"], personspread=0)

class General(Spread):
	def __init__(self):
		Spread.__init__(self, ["Past 1:", "Past 2:", "Past 3:", "Present 4:", "Present 5:", "Present 6:", "Future 1:", "Future 2:", "Future 3:"], personspread=0)

class CelticCross(Spread):
	def __init__(self):
		Spread.__init__(self, ["Present:", "Immediate challenge:", "Distant past:", "Recent past:", "Best outcome:", "Immediate future:", "Factors affecting situation:", "External influences:", "Hopes and fears:", "The final outcome:"], personspread=0)

class TreeOfLife(Spread):
	def __init__(self):
		Spread.__init__(self, ["Significator:", "Aims or ideals:", "Influences:", "General nature:", "The key:", "Influences of the present:", "Influences of the future:", "Effect of the significator:", "Effect of the environment:", "Hopes and fears:", "The final outcome:"], personspread=1)

class Horoscope(Spread):
	def __init__(self):
		Spread.__init__(self, ["Aries - Self:", "Taurus - Material things:", "Gemini - Communication:", "Cancer - Home life:", "Leo - Love, creativity, and pleasure:", "Virgo - Health and work:", "Libra - Partnerships:", "Scorpio - Death, money, and sex:", "Sagittarius - Travel and future:", "Capricorn - Career:", "Aquarius - Friends and social groups:", "Pisces - Secrets:"], personspread=1)

#if __name__ == "__main__":
#	run()
