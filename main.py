
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
	'DEF': 45,
	'SPE': 100,
	'CRITrate': 15,
	'attacks': {
		'attack1': (80, 90, 'Normal Attack'), # (atk, accuracy), senere implement element!
		'attack2': (90, 80, 'Elemental Skill')
	}
}, {
	'name': 'Aether',
	'sprite': 'emj:Pedestrian',
	'HP': 1750,
	'MHP': 1750,
	'ATK': 30,
	'DEF': 60,
	'SPE': 80,
	'CRITrate': 0,
	'attacks': {
		'attack1': (80, 90, 'Normal Attack'),
		'attack2': (90, 80, 'Elemental Skill')
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

attackboxsizex, attackboxsizey = (200, 100) # Universal størrelse på attackbox
attack1x, attack1y = (56, 56) # Koordinater på bottomleft corner av boxene
attack2x, attack2y = (312, 56)
attack3x, attack3y = (568, 56)
attack4x, attack4y = (824, 56)

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
	


def DMGcalc(player, opponent, attack): # player og opponent er i dictionary formatet importert fra playablecharacters
	return (player['ATK']/opponent['DEF']) * player['attacks'][attack][0] * (random.randint(8, 12)/10)

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
		self.attack1labe2 = scene.LabelNode('', font=('Avenir', 20), color='#fff', position=(attack2x+(attackboxsizex/2), attack2y+(attackboxsizey/2)), parent=self)
		self.attack1labe3 = scene.LabelNode('', font=('Avenir', 20), color='#fff', position=(attack3x+(attackboxsizex/2), attack3y+(attackboxsizey/2)), parent=self)
		self.attack1labe4 = scene.LabelNode('', font=('Avenir', 20), color='#fff', position=(attack4x+(attackboxsizex/2), attack4y+(attackboxsizey/2)), parent=self)
		
		# Text if attack is missed
		
		self.attackmissedtext = scene.LabelNode('', font=('Avenir', 50), color='transparent', position=(self.size.w/2, self.size.h/2), parent=self)
		
		self.critHit = scene.LabelNode('', font=('Avenir', 50), color='transparent', position=(self.size.w/2, self.size.h/2), parent=self)
	
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
		
		# Attack #1-4 button
		scene.fill("#000")
		scene.rect(attack1x, attack1y, attackboxsizex, attackboxsizey)
		scene.rect(attack2x, attack2y, attackboxsizex, attackboxsizey)
		scene.rect(attack3x, attack3y, attackboxsizex, attackboxsizey)
		scene.rect(attack4x, attack4y, attackboxsizex, attackboxsizey)
		
		# Attack text
		
		if self.currentMover == 1:
			self.attack1label.text = player1['attacks']['attack1'][2]
			self.attack1labe2.text = player1['attacks']['attack2'][2]
			#self.attack1labe3.text = player1['attacks']['attack3'][2]
			#self.attack1labe4.text = player1['attacks']['attack4'][2]
		else:
			self.attack1label.text = player2['attacks']['attack1'][2]
			self.attack1labe2.text = player2['attacks']['attack2'][2]
			#self.attack1labe3.text = playe2['attacks']['attack3'][2]
			#self.attack1labe4.text = player2['attacks']['attack4'][2]
	
	def touch_began(self, touch):				
		self.attackmissedtext.text = ''
		self.critHit.text = ''
		# Deaktiverer Normal Attack hvis en av spillerene er døde
		if self.Game_Over == False:
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
		
		# Dead check
		
		if player1['HP'] <= 0:
			scene.fill("#fff")
			scene.rect(0, 0, 2000, 2000)
			# Signaliserer at et av spillerene er døde
			self.Game_Over = True
			self.wintext = scene.LabelNode('{} (Player 2) wins'.format(player2['name']), font=('Avenir', 110), color='#000', position=(self.size.w/2, self.size.h/2), parent=self)
			sys.exit()
		if player2['HP'] <= 0:
			scene.fill("#fff")
			scene.rect(0, 0, 2000, 2000)
			self.Game_Over = True
			self.wintext = scene.LabelNode('{} (Player 1) wins'.format(player1['name']), font=('Avenir', 110), color='#000', position=(self.size.w/2, self.size.h/2), parent=self)
			sys.exit()
	

#print(DMGcalc(playablecharacters[0], playablecharacters[0], 'Normal Attack'))

#print(scene.get_screen_size()) #1080 810

scene.run(mainScene())

