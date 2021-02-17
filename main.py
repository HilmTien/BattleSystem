
# Programmeringsvurdering våren 2021

# Enkelt battle system utviklet av Tien og Vincent (2021)

import console, scene, random, sys, time

#
# PLAYABLE CHARACTERS
#

playablecharacters = [{
	'name': 'Lumine',
	'sprite': 'emj:Dancer',
	'HP': 1000,
	'MHP': 1000,
	'ATK': 70,
	'ELEATK': 100,
	'DEF': 45,
	'ELERES': 30,
	'SPE': 100,
	'CRITrate': 15,
	'status': '',
	'statustimer': 0,
	'reaction' : '',
	'attacks': {
		'attack1': (80, 90, 'Normal Attack', 'physical'), # (atk, accuracy), senere implement element!
		'attack2': (90, 80, 'Primary Skill', 'electro'),
		'attack3': (60, 100, 'Secondary Skill', 'hydro'),
		'attack4': (50, 95, 'Utility', 'utility', 'atkup', 'Swords Dance')
	}
}, {
	'name': 'Aether',
	'sprite': 'emj:Pedestrian',
	'HP': 1750,
	'MHP': 1750,
	'ATK': 30,
	'ELEATK': 20,
	'DEF': 60,
	'ELERES': 60,
	'SPE': 80,
	'CRITrate': 0,
	'status': '',
	'statustimer': 3,
	'reaction' : '',
	'attacks': {
		'attack1': (100, 90, 'Normal Attack', 'physical'),
		'attack2': (90, 80, 'Primary Skill', 'geo'),
		'attack3': (60, 90, 'Secondary Skill', 'anemo'),
		'attack4': (50, 95, 'Utility', 'utility', 'defup', 'Defense Curl')
	}
}] # Mulighet til å legge til flere karakterer rett før ]

#
# Init
#

# Viser antallet spillbare karakterer
antallCharacters = len(playablecharacters)
# Velger en tilfeldig karakter for hver spiller
player1 = dict(playablecharacters[random.randint(0,antallCharacters-1)])
player2 = dict(playablecharacters[random.randint(0,antallCharacters-1)])

while player1 == player2:
	player1 = dict(playablecharacters[random.randint(0,antallCharacters-1)])
	player2 = dict(playablecharacters[random.randint(0,antallCharacters-1)])

#player1 = dict(playablecharacters[0])
#player2 = dict(playablecharacters[1])

attackboxsizex, attackboxsizey = (200, 100) # Universal størrelse på attackbox
attack1x, attack1y = (56, 56) # Koordinater på bottomleft corner av boxene
attack2x, attack2y = (312, 56)
attack3x, attack3y = (568, 56)
attack4x, attack4y = (824, 56)

info1bl = (100, 550)#(150, 800, 600)
info1tr = ()

info2bl = (750, 550)
info2tr = ()

#
# FUNKSJONER (F.EKS. BATTLE MECHANICS)
#

# Kalkulerer hvem som starter utifra fart
def SPEcalc(player, opponent):
	if player['SPE'] > opponent['SPE']:
		PlayerMove = 1
	
	elif player['SPE'] < opponent['SPE']:
		PlayerMove = 2
	
	else:
		PlayerMove = random.randint(1,2)
	
	return PlayerMove

# Sjekker hvilken reaction som blir inflicted	
def ELMreactionCheck(player, opponent, attack):
	
	if opponent['status'] == 'geo':
		elementalReaction = 'crystallize'
		if player['attacks'][attack][3] != 'geo':
			opponent['reaction'] = 'Crystallize'
		
		
	
	if opponent['status'] == 'anemo':
		elementalReaction = 'swirl'
		if player['attacks'][attack][3] != 'anemo':
			opponent['reaction'] = 'Swirl'
		
		
		
	if opponent['status'] == 'dendro':
		if player['attacks'][attack][3] == 'pyro':
			elementalReaction = 'burning'
			opponent['reaction'] = 'Burning'
		
		if player['attacks'][attack][3] == 'anemo':
			elementalReaction = 'swirl'
			opponent['reaction'] = 'Swirl'
		
		if player['attacks'][attack][3] == 'geo':
			elementalReaction = 'crystallize'
			opponent['reaction'] = 'Crystallize'
	
	if opponent['status'] == 'hydro':
		if player['attacks'][attack][3] == 'pyro':
			elementalReaction = 'vaporizeweak'
			opponent['reaction'] = 'Vaporize'
			
		if player['attacks'][attack][3] == 'cryo':
			elementalReaction = 'freeze'
			opponent['reaction'] = 'Freeze'
			
		if player['attacks'][attack][3] == 'electro':
			elementalReaction = 'electrocharged'
			opponent['reaction'] = 'Electro Charged'
		
		if player['attacks'][attack][3] == 'anemo':
			elementalReaction = 'swirl'
			opponent['reaction'] = 'Swirl'
		
		if player['attacks'][attack][3] == 'geo':
			elementalReaction = 'crystallize'
			opponent['reaction'] = 'Crystallize'
	
	elif opponent['status'] == 'pyro':
		if player['attacks'][attack][3] == 'hydro':
			elementalReaction = 'vaporizestrong'
			opponent['reaction'] = 'Vaporize'
			
		if player['attacks'][attack][3] == 'cryo':
			elementalReaction = 'meltweak'
			opponent['reaction'] = 'Melt'
			
		if player['attacks'][attack][3] == 'electro':
			elementalReaction = 'overload'
			opponent['reaction'] = 'Overload'
		
		if player['attacks'][attack][3] == 'dendro':
			elementalReaction = 'burning'
			opponent['reaction'] = 'Burning'
		
		if player['attacks'][attack][3] == 'anemo':
			elementalReaction = 'swirl'
			opponent['reaction'] = 'Swirl'
		
		if player['attacks'][attack][3] == 'geo':
			elementalReaction = 'crystallize'
			opponent['reaction'] = 'Crystallize'
	
	elif opponent['status'] == 'electro':
		if player['attacks'][attack][3] == 'hydro':
			elementalReaction = 'electrocharged'
			opponent['reaction'] = 'Electro Charged'
			
		if player['attacks'][attack][3] == 'cryo':
			elementalReaction = 'superconduct'
			opponent['reaction'] = 'Superconduct'
			
		if player['attacks'][attack][3] == 'pyro':
			elementalReaction = 'overload'
			opponent['reaction'] = 'Overload'
		
		if player['attacks'][attack][3] == 'anemo':
			elementalReaction = 'swirl'
			opponent['reaction'] = 'Swirl'
		
		if player['attacks'][attack][3] == 'geo':
			elementalReaction = 'crystallize'
			opponent['reaction'] = 'Crystallize'
	
	elif opponent['status'] == 'cryo':
		if player['attacks'][attack][3] == 'hydro':
			elementalReaction = 'freeze'
			opponent['reaction'] = 'Freeze'
			
		if player['attacks'][attack][3] == 'electro':
			elementalReaction = 'superconduct'
			opponent['reaction'] = 'Superconduct'
			
		if player['attacks'][attack][3] == 'pyro':
			elementalReaction = 'meltstrong'
			opponent['reaction'] = 'Melt'
		
		if player['attacks'][attack][3] == 'anemo':
			elementalReaction = 'swirl'
			opponent['reaction'] = 'Swirl'
		
		if player['attacks'][attack][3] == 'geo':
			elementalReaction = 'crystallize'
			opponent['reaction'] = 'Crystallize'
	
	if opponent['status'] == player['attacks'][attack][3]:
		elementalReaction = 'neutral'
	
	return elementalReaction 

# Utfører elemental reactions
def ELMreactions(player, opponent, attack, ElementalReaction):
	
	if ElementalReaction == 'neutral':
		DMGdealt = (player['ELEATK']/opponent['ELERES']) * player['attacks'][attack][0] * (random.randint(8, 12)/10)
		opponent['statustimer'] = 4
	else:
		if ElementalReaction == 'vaporizeweak':
			DMGdealt = (player['ELEATK']/opponent['ELERES']) * player['attacks'][attack][0] * (random.randint(8, 12)/10)*1.5
		elif ElementalReaction == 'vaporizestrong':
			DMGdealt = (player['ELEATK']/opponent['ELERES']) * player['attacks'][attack][0] * (random.randint(8, 12)/10)*2
		elif ElementalReaction == 'meltweak':
			DMGdealt = (player['ELEATK']/opponent['ELERES']) * player['attacks'][attack][0] * (random.randint(8, 12)/10)*1.5
		elif ElementalReaction == 'meltstrong':
			DMGdealt = (player['ELEATK']/opponent['ELERES']) * player['attacks'][attack][0] * (random.randint(8, 12)/10)*2
		elif ElementalReaction == 'superconduct':
			opponent['DEF'] /= 2
			DMGdealt = (player['ELEATK']/opponent['ELERES']) * player['attacks'][attack][0] * (random.randint(8, 12)/10)
		elif ElementalReaction == 'swirl':
			opponent['ELERES'] = (opponent['ELERES']/3) * 2
			DMGdealt = (player['ELEATK']/opponent['ELERES']) * player['attacks'][attack][0] * (random.randint(8, 12)/10)
		elif ElementalReaction == 'overload':
			DMGdealt = player['ELEATK'] * player['attacks'][attack][0] * (random.randint(8, 12)/10)
		elif ElementalReaction == 'freeze':
			opponent['isFrozenRounds'] = 4
			DMGdealt = (player['ELEATK']/opponent['ELERES']) * player['attacks'][attack][0] * (random.randint(8, 12)/10)
		elif ElementalReaction == 'burning':
			opponent['isBurningRounds'] = 6
			DMGdealt = (player['ELEATK']/opponent['ELERES']) * player['attacks'][attack][0] * (random.randint(8, 12)/10)
		elif ElementalReaction == 'electrocharged':
			opponent['isElectroChargedRounds'] = 6
			DMGdealt = (player['ELEATK']/opponent['ELERES']) * player['attacks'][attack][0] * (random.randint(8, 12)/10)
		elif ElementalReaction == 'crystallize':
			player['DEF'] += 15
			player['ELERES'] += 15
			player['HP'] += player['DEF'] + player['ELERES'] + (player['MHP']/20)
			DMGdealt = (player['ELEATK']/opponent['ELERES']) * player['attacks'][attack][0] * (random.randint(8, 12)/10)
			
		# Fjerner element etter reaction
		opponent['status'] = ''
	
	return DMGdealt
	

def DMGcalc(player, opponent, attack): # player og opponent er i dictionary formatet importert fra playablecharacters


	# Elemetal check
	
	if player['attacks'][attack][3] != 'physical':
		if player['attacks'][attack][3] != 'utility':
			if opponent['status'] == '':
				opponent['status'] = player['attacks'][attack][3] # Applyer element til enemy
				opponent['statustimer'] = 4
				DMGdealt = (player['ELEATK']/opponent['ELERES']) * player['attacks'][attack][0] * (random.randint(8, 12)/10)
			
			else:
				ElementalReaction = ELMreactionCheck(player,opponent,attack)
				DMGdealt = ELMreactions(player, opponent, attack, ElementalReaction)
		else:
			DMGdealt = 0
			if player['attacks'][attack][4] == 'atkup':
				player['ATK'] += player['attacks'][attack][0]
			elif player['attacks'][attack][4] == 'defup':
				player['DEF'] += player['attacks'][attack][0]
		
	else:
		DMGdealt = (player['ATK']/opponent['DEF']) * player['attacks'][attack][0] * (random.randint(8, 12)/10)
		
	# Electro Charged damage check
	try:
		if player['isElectroChargedRounds'] != 0:
			player['HP'] -= ((player['MHP'] - player['HP']) / 10)
			player['isElectroChargedRounds'] -= 1
	except:
		pass
	
	try:
		if opponent['isElectroChargedRounds'] != 0:
			opponent['HP'] -= ((opponent['MHP'] - opponent['HP']) / 10)
			opponent['isElectroChargedRounds'] -= 1
	except:
		pass		
	
	# Burning check
	
	try:
		if player['isBurningRounds'] != 0:
			player['HP'] -= player['HP'] / 10
			player['isElectroChargedRounds'] -= 1
	except:
		pass
	
	try:
		if opponent['isBurningRounds'] != 0:
			opponent['HP'] -= opponent['HP'] / 10
			opponent['isBurningRounds'] -= 1
	except:
		pass
		
	# Freeze check
	
	try:
		if player['isFrozenRounds'] != 0:
			DMGdealt = 0
			player['isFrozenRounds'] -= 1
		thawrng = random.randint(1, player['isFrozenRounds'])
		if thawrng == 1:
			player['isFrozenRounds'] = 0
	except:
		pass
	
	try:
		if opponent['isFrozenRounds'] != 0:
			opponent['isFrozenRounds'] -= 1
		thawrng = random.randint(1, opponent['isFrozenRounds'])
		if thawrng == 1:
			opponent['isFrozenRounds'] = 0
	except:
		pass
	
	return DMGdealt

def hppercentage(player):
	res = (player['HP']/player['MHP']) * 100 * 1.8
	if res <= 0:
		res = 0
	return res # finn prosent hp og gjøre det til riktig format til hpbarrektangel

#
# USER INTERFACE
#

class mainScene(scene.Scene):
	# Setter opp variabler som funksjonene skal arve
	currentMover = SPEcalc(player1, player2)
	Game_Over = False
	def setup(self):
		self.background_color = '#ffffff'
		scene.SpriteNode(player1['sprite'], position=(150, 600), parent=self, scale=2)
		scene.SpriteNode(player2['sprite'], position=(800, 600), parent=self, scale=2)
		
		# Topleft text (player #'s turn)
		
		self.playerturn = scene.LabelNode("(Player {}) {}'s turn".format(self.currentMover, [player1, player2][self.currentMover-1]['name']), font=('Avenir', 25), color='#000', position=(25, self.size.h-25), parent=self, anchor_point=(0, 1))
		
		# Attack text (1 - 4)
		
		self.attack1label = scene.LabelNode('', font=('Avenir', 20), color='#fff', position=(attack1x+(attackboxsizex/2), attack1y+(attackboxsizey/2)), parent=self)
		self.attack1label2 = scene.LabelNode('', font=('Avenir', 20), color='#fff', position=(attack2x+(attackboxsizex/2), attack2y+(attackboxsizey/2)), parent=self)
		self.attack1label3 = scene.LabelNode('', font=('Avenir', 20), color='#fff', position=(attack3x+(attackboxsizex/2), attack3y+(attackboxsizey/2)), parent=self)
		self.attack1label4 = scene.LabelNode('', font=('Avenir', 20), color='#fff', position=(attack4x+(attackboxsizex/2), attack4y+(attackboxsizey/2)), parent=self)
		
		# Text if attack is missed
		
		self.attackmissedtext = scene.LabelNode('', font=('Avenir', 50), color='#000', position=(self.size.w/2, self.size.h/2), parent=self)
		
		self.critHit = scene.LabelNode('', font=('Avenir', 50), color='#000', position=(self.size.w/2, self.size.h/2), parent=self)
		
		# Reaction texts
		
		self.player1reaction = scene.LabelNode('', font=('Avenir', 25), color='#000', position= (200, 500), parent = self, anchor_point=(0.5,1))
		self.player2reaction = scene.LabelNode('', font=('Avenir', 25), color='#000', position= (850, 500), parent = self, anchor_point =(0.5,1))
		
		# Elements sprites
		
		self.pyro1 = scene.SpriteNode('emj:Fire', position=(100, 500), anchor_point=(0.5, 1), parent=self, alpha=0)
		self.pyro2 = scene.SpriteNode('emj:Fire', position=(750, 500), anchor_point=(0.5, 1), parent=self, alpha=0) 
		
		self.hydro1 = scene.SpriteNode('emj:Droplet', position=(100, 500), anchor_point=(0.5, 1), parent=self, alpha=0)
		self.hydro2 = scene.SpriteNode('emj:Droplet', position=(750, 500), anchor_point=(0.5, 1), parent=self, alpha=0) 
		
		self.cryo1 = scene.SpriteNode('emj:Snowflake', position=(100, 500), anchor_point=(0.5, 1), parent=self, alpha=0)
		self.cryo2 = scene.SpriteNode('emj:Snowflake', position=(750, 500), anchor_point=(0.5, 1), parent=self, alpha=0) 
		
		self.electro1 = scene.SpriteNode('emj:High_Voltage_Sign', position=(100, 500), anchor_point=(0.5, 1), parent=self, alpha=0)
		self.electro2 = scene.SpriteNode('emj:High_Voltage_Sign', position=(750, 500), anchor_point=(0.5, 1), parent=self, alpha=0) 
		
		self.anemo1 = scene.SpriteNode('emj:Cyclone', position=(100, 500), anchor_point=(0.5, 1), parent=self, alpha=0)
		self.anemo2 = scene.SpriteNode('emj:Cyclone', position=(750, 500), anchor_point=(0.5, 1), parent=self, alpha=0) 
		
		self.geo1 = scene.SpriteNode('emj:Moyai', position=(100, 500), anchor_point=(0.5, 1), parent=self, alpha=0)
		self.geo2 = scene.SpriteNode('emj:Moyai', position=(750, 500), anchor_point=(0.5, 1), parent=self, alpha=0) 
		
		self.dendro1 = scene.SpriteNode('emj:Seedling', position=(100, 500), anchor_point=(0.5, 1), parent=self, alpha=0)
		self.dendro2 = scene.SpriteNode('emj:Seedling', position=(750, 500), anchor_point=(0.5, 1), parent=self, alpha=0) 
		
		# Elemental reaction Labels
		self.Player1DOT = scene.LabelNode('', font=('Avenir', 25), color='#000', position=(225, 600), parent=self, anchor_point=(0, 0))
		self.Player2DOT = scene.LabelNode('', font=('Avenir', 25), color='#000', position=(875, 600), parent=self, anchor_point=(0, 0))
	
	def draw(self):
		
		# HP bar player 1
		
		scene.fill("#000")
		scene.rect(100, 500, 200, 50)
		scene.fill("#4cd658")
		scene.rect(110, 510, hppercentage(player1), 30)
		
		# HP bar player 2
		
		scene.fill("#000")
		scene.rect(750, 500, 200, 50)
		scene.fill("#4cd658")
		scene.rect(760, 510, hppercentage(player2), 30)
		
		# Elemental sprites
		
		if player1['status'] != '':
			#self.pyro.alpha = 1
			setattr(getattr(self, '{}{}'.format(player1['status'], '1')), 'alpha', 1) # en bedre måte å skrive det over
		else:
			setattr(getattr(self, 'pyro1'), 'alpha', 0)
			setattr(getattr(self, 'hydro1'), 'alpha', 0)
			setattr(getattr(self, 'cryo1'), 'alpha', 0)
			setattr(getattr(self, 'electro1'), 'alpha', 0)
			setattr(getattr(self, 'geo1'), 'alpha', 0)
			setattr(getattr(self, 'anemo1'), 'alpha', 0)
			setattr(getattr(self, 'dendro1'), 'alpha', 0)
		if player2['status'] != '':
			#self.pyro.alpha = 1
			setattr(getattr(self, '{}{}'.format(player2['status'], '2')), 'alpha', 1)
		else:
			setattr(getattr(self, 'pyro2'), 'alpha', 0)
			setattr(getattr(self, 'hydro2'), 'alpha', 0)
			setattr(getattr(self, 'cryo2'), 'alpha', 0)
			setattr(getattr(self, 'electro2'), 'alpha', 0)
			setattr(getattr(self, 'geo2'), 'alpha', 0)
			setattr(getattr(self, 'anemo2'), 'alpha', 0)
			setattr(getattr(self, 'dendro2'), 'alpha', 0)
			
		# DOTs
		
		try:
			if player1['isBurningRounds'] != 0:
				self.Player1DOT.text = 'Burning'
			else:
				self.Player1DOT.text = ''
		except:
			pass
			
		try:
			if player1['isElectroChargedRounds'] != 0:
				self.Player1DOT.text = 'Electro Charged'
			else:
				self.Player1DOT.text = ''
		except:
			pass
		
		try:
			if player1['isFrozenRounds'] != 0:
				self.Player1DOT.text = 'Frozen'
			else:
				self.Player1DOT.text = ''
		except:
			pass
		
		try:
			if player2['isBurningRounds'] != 0:
				self.Player2DOT.text = 'Burning'
			else:
				self.Player2DOT.text = ''
		except:
			pass
			
		try:
			if player2['isElectroChargedRounds'] != 0:
				self.Player2DOT.text = 'Electro Charged'
			else:
				self.Player2DOT.text = ''
		except:
			pass
		
		try:
			if player2['isFrozenRounds'] != 0:
				self.Player2DOT.text = 'Frozen'
			else:
				self.Player2DOT.text = ''
		except:
			pass
					
		# Attack #1-4 button
		scene.fill("#000")
		scene.rect(attack1x, attack1y, attackboxsizex, attackboxsizey)
		scene.rect(attack2x, attack2y, attackboxsizex, attackboxsizey)
		scene.rect(attack3x, attack3y, attackboxsizex, attackboxsizey)
		scene.rect(attack4x, attack4y, attackboxsizex, attackboxsizey)
		
		# Attack text
		
		if self.currentMover == 1:
			self.attack1label.text = player1['attacks']['attack1'][2]
			self.attack1label2.text = player1['attacks']['attack2'][2]
			self.attack1label3.text = player1['attacks']['attack3'][2]
			self.attack1label4.text = player1['attacks']['attack4'][2]
		else:
			self.attack1label.text = player2['attacks']['attack1'][2]
			self.attack1label2.text = player2['attacks']['attack2'][2]
			self.attack1label3.text = player2['attacks']['attack3'][2]
			self.attack1label4.text = player2['attacks']['attack4'][2]
	
	
	
	
	
	def touch_began(self, touch):				
		self.attackmissedtext.text = ''
		self.critHit.text = ''
		# Deaktiverer Normal Attack hvis en av spillerene er døde
		if self.Game_Over == False:
			
			#
			# Attack 1 (Normal Attack)
			#
			
			if attack1x < touch.location.x < attack1x+attackboxsizex and attack1y < touch.location.y < attack1y+attackboxsizey: # Første black box eller attack
				
				accrng = random.randint(1, 100)
				critrng = random.randint(1, 100)
				
				# Sjekker om det er P2 sin tur
				if self.currentMover == 2:
					if accrng < player2['attacks']['attack1'][1]: #Sjekker accuracy
						if critrng <= player2['CRITrate']:						
							player1['HP'] -= DMGcalc(player2, player1, 'attack1')*2 #Dealer damage til P1
							self.critHit.text = '(Player {}) {} CRIT!'.format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
						else:
							player1['HP'] -= DMGcalc(player2, player1, 'attack1')
					else:
						self.attackmissedtext.text = '(Player {}) {} missed!'.format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
					#Bytter tur tilbake til P1
					self.currentMover = 1
					self.playerturn.text = "(Player {}) {}'s turn".format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
					# Ticker ned elemental status timer
					if player1['statustimer'] != 0:
						player1['statustimer'] -= 1
					# Fjerner element etter en tid
					if player1['statustimer'] <= 0:
						player1['status'] = ''
					
					if player1['reaction'] != '':
						self.player1reaction.text = '{}'.format(player1['reaction'])
					if player2['reaction'] != '':
						self.player2reaction.text = ''
						player2['reaction'] = ''
						
						
						
				
				# Spiller om det er P1 sin tur
				else:				
					if accrng < player1['attacks']['attack1'][1]:
						if critrng <= player1['CRITrate']:
							player2['HP'] -= DMGcalc(player1, player2, 'attack1')*2
							self.critHit.text = '(Player {}) {} CRIT!'.format(self.currentMover, [player1, player2][self.currentMover-1]['name'])						
						else:	
							player2['HP'] -= DMGcalc(player1, player2, 'attack1')
						#Dealer damage til P2
					else:
						self.attackmissedtext.text = '(Player {}) {} missed!'.format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
						
					#Bytter tur tilbake til P2
					self.currentMover = 2
					self.playerturn.text = "(Player {}) {}'s turn".format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
					# Ticker ned elemental status timer
					if player2['statustimer'] != 0:
						player2['statustimer'] -= 1
					# Fjerner element etter en tid
					if player2['statustimer'] <= 0:
						player2['status'] = ''
					
					if player2['reaction'] != '':
						self.player2reaction.text = '{}'.format(player2['reaction'])
					if player1['reaction'] != '':
						self.player1reaction.text = ''
						player1['reaction'] = ''
						
		
			#
			# Attack 2 (Primary skill)
			#
		
			elif attack2x < touch.location.x < attack2x+attackboxsizex and attack2y < touch.location.y < attack2y+attackboxsizey: 
				
				accrng = random.randint(1, 100)
				critrng = random.randint(1, 100)
				
				# Sjekker om det er P2 sin tur
				if self.currentMover == 2:
					if accrng < player2['attacks']['attack2'][1]: #Sjekker accuracy
						if critrng <= player2['CRITrate']:						
							player1['HP'] -= DMGcalc(player2, player1, 'attack2')*2 #Dealer damage til P1
							self.critHit.text = '(Player {}) {} CRIT!'.format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
						else:
							player1['HP'] -= DMGcalc(player2, player1, 'attack2')
					else:
						self.attackmissedtext.text = '(Player {}) {} missed!'.format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
					#Bytter tur tilbake til P1
					self.currentMover = 1
					self.playerturn.text = "(Player {}) {}'s turn".format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
					# Ticker ned elemental status timer
					if player1['statustimer'] != 0:
						player1['statustimer'] -= 1
					# Fjerner element etter en tid
					if player1['statustimer'] <= 0:
						player1['status'] = ''
					
					if player1['reaction'] != '':
						self.player1reaction.text = '{}'.format(player1['reaction'])
					if player2['reaction'] != '':
						self.player2reaction.text = ''
						player2['reaction'] = ''
				
				# Spiller om det er P1 sin tur
				else:				
					if accrng < player1['attacks']['attack2'][1]:
						if critrng <= player1['CRITrate']:
							player2['HP'] -= DMGcalc(player1, player2, 'attack2')*2
							self.critHit.text = '(Player {}) {} CRIT!'.format(self.currentMover, [player1, player2][self.currentMover-1]['name'])						
						else:	
							player2['HP'] -= DMGcalc(player1, player2, 'attack2')
						#Dealer damage til P2
					else:
						self.attackmissedtext.text = '(Player {}) {} missed!'.format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
						
					#Bytter tur tilbake til P2
					self.currentMover = 2
					self.playerturn.text = "(Player {}) {}'s turn".format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
					# Ticker ned elemental status timer
					if player2['statustimer'] != 0:
						player2['statustimer'] -= 1
					# Fjerner element etter en tid
					if player2['statustimer'] <= 0:
						player2['status'] = ''
					
					if player2['reaction'] != '':
						self.player2reaction.text = '{}'.format(player2['reaction'])
					if player1['reaction'] != '':
						self.player1reaction.text = ''
						player1['reaction'] = ''
			
			#
			# Attack 3 (Secondary Skill)
			#
		
			elif attack3x < touch.location.x < attack3x+attackboxsizex and attack3y < touch.location.y < attack3y+attackboxsizey: 
				
				accrng = random.randint(1, 100)
				critrng = random.randint(1, 100)
				
				# Sjekker om det er P2 sin tur
				if self.currentMover == 2:
					if accrng < player2['attacks']['attack3'][1]: #Sjekker accuracy
						if critrng <= player2['CRITrate']:						
							player1['HP'] -= DMGcalc(player2, player1, 'attack3')*2 #Dealer damage til P1
							self.critHit.text = '(Player {}) {} CRIT!'.format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
						else:
							player1['HP'] -= DMGcalc(player2, player1, 'attack3')
					else:
						self.attackmissedtext.text = '(Player {}) {} missed!'.format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
					#Bytter tur tilbake til P1
					self.currentMover = 1
					self.playerturn.text = "(Player {}) {}'s turn".format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
					# Ticker ned elemental status timer
					if player1['statustimer'] != 0:
						player1['statustimer'] -= 1
					# Fjerner element etter en tid
					if player1['statustimer'] <= 0:
						player1['status'] = ''
					
					if player1['reaction'] != '':
						self.player1reaction.text = '{}'.format(player1['reaction'])
					if player2['reaction'] != '':
						self.player2reaction.text = ''
						player2['reaction'] = ''
						
				
				# Spiller om det er P1 sin tur
				else:				
					if accrng < player1['attacks']['attack3'][1]:
						if critrng <= player1['CRITrate']:
							player2['HP'] -= DMGcalc(player1, player2, 'attack3')*2
							self.critHit.text = '(Player {}) {} CRIT!'.format(self.currentMover, [player1, player2][self.currentMover-1]['name'])						
						else:	
							player2['HP'] -= DMGcalc(player1, player2, 'attack3')
						#Dealer damage til P2
					else:
						self.attackmissedtext.text = '(Player {}) {} missed!'.format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
						
					#Bytter tur tilbake til P2
					self.currentMover = 2
					self.playerturn.text = "(Player {}) {}'s turn".format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
					# Ticker ned elemental status timer
					if player2['statustimer'] != 0:
						player2['statustimer'] -= 1
					# Fjerner element etter en tid
					if player2['statustimer'] <= 0:
						player2['status'] = ''
					
					if player2['reaction'] != '':
						self.player2reaction.text = '{}'.format(player2['reaction'])
					if player1['reaction'] != '':
						self.player1reaction.text = ''
						player1['reaction'] = ''
			
			#
			# Attack 4 (Utility)
			#
		
			elif attack4x < touch.location.x < attack4x+attackboxsizex and attack4y < touch.location.y < attack4y+attackboxsizey:
				
				accrng = random.randint(1, 100)
				
				# Sjekker om det er P2 sin tur
				if self.currentMover == 2:
					if accrng < player2['attacks']['attack4'][1]: #Sjekker accuracy
						player1['HP'] -= DMGcalc(player2, player1, 'attack4') #Dealer damage til P1/status effect
						self.player2reaction.text = '{}'.format(player2['attacks']['attack4'][5])
					else:
						self.attackmissedtext.text = '(Player {}) {} failed!'.format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
					#Bytter tur tilbake til P1
					self.currentMover = 1
					self.playerturn.text = "(Player {}) {}'s turn".format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
					# Ticker ned elemental status timer
					if player1['statustimer'] != 0:
						player1['statustimer'] -= 1
					# Fjerner element etter en tid
					if player1['statustimer'] <= 0:
						player1['status'] = ''
					
					if player1['reaction'] != '':
						self.player1reaction.text = '{}'.format(player1['reaction'])
					if player2['reaction'] != '':
						player2['reaction'] = ''
						
				
				# Spiller om det er P1 sin tur
				else:				
					if accrng < player1['attacks']['attack4'][1]:
						player2['HP'] -= DMGcalc(player1, player2, 'attack4')
						#Dealer damage til P2/status effect
						self.player1reaction.text = '{}'.format(player1['attacks']['attack4'][5])
					else:
						self.attackmissedtext.text = '(Player {}) {} failed!'.format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
						
					#Bytter tur tilbake til P2
					self.currentMover = 2
					self.playerturn.text = "(Player {}) {}'s turn".format(self.currentMover, [player1, player2][self.currentMover-1]['name'])
					# Ticker ned elemental status timer
					if player2['statustimer'] != 0:
						player2['statustimer'] -= 1
					# Fjerner element etter en tid
					if player2['statustimer'] <= 0:
						player2['status'] = ''
					
					if player2['reaction'] != '':
						self.player2reaction.text = '{}'.format(player2['reaction'])
					if player1['reaction'] != '':
						player1['reaction'] = ''
		
			#elif infox
		
		# Dead check
		
		if player1['HP'] <= 0:
			# Signaliserer at et av spillerene er døde
			self.critHit.text = ''
			self.Game_Over = True
			self.wintext = scene.LabelNode('{} (Player 2) wins'.format(player2['name']), font=('Avenir', 100), color='#000', position=(self.size.w/2, (self.size.h/2)-25), parent=self)
			sys.exit()
		if player2['HP'] <= 0:
			self.critHit.text = ''
			self.Game_Over = True
			self.wintext = scene.LabelNode('{} (Player 1) wins'.format(player1['name']), font=('Avenir', 100), color='#000', position=(self.size.w/2, (self.size.h/2)-25), parent=self)
			sys.exit()
	

#print(DMGcalc(playablecharacters[0], playablecharacters[0], 'Normal Attack'))

#print(scene.get_screen_size()) #1080 810

scene.run(mainScene())

