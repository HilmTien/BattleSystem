
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
	'ATK': 60,
	'DEF': 45,
	'SPE': 100,
	'attacks': {
		'attack1': (80, 90, 'Normal Attack'), # (atk, accuracy), senere implement element!
		'attack2': (90, 80)
	}
}, {
	'name': 'Aether',
	'sprite': 'emj:Pedestrian',
	'HP': 1750,
	'MHP': 1750,
	'ATK': 30,
	'DEF': 60,
	'SPE': 80,
	'attacks': {
		'attack1': (80, 90, 'Normal Attack'),
		'attack2': (90, 80)
	}
}] # Mulighet til å legge til flere karakterer rett før ]

#
# Init
#

player1 = playablecharacters[0]
player2 = playablecharacters[1]



#
# FUNKSJONER (F.EKS. BATTLE MECHANICS)
#

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
	def setup(self):
		self.background_color = '#ffffff'
		scene.SpriteNode(player1['sprite'], position=(150, 600), parent=self, scale=2)
		scene.SpriteNode(player2['sprite'], position=(800, 600), parent=self, scale=2)
	
	def draw(self):
		
		#self.missed = scene.LabelNode('Missed!', font=('Avenir', 50), color='transparent', position=)
		
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
		
		# Attack #1 button
		scene.fill("#000")
		scene.rect(100, 100, 150, 100)
	
	def touch_began(self, touch):
		
		if 100 < touch.location.x < 250 and 100 < touch.location.y < 200: #Første black box eller attack
			accrng = random.randint(1, 100)
			if accrng < player1['attacks']['attack1'][1]:
				player1['HP'] -= DMGcalc(player1, player2, 'attack1')
			else:
				pass
		
		# Dead check
		
		if player1['HP'] <= 0:
			scene.fill("#fff")
			scene.rect(0, 0, 2000, 2000)
			self.wintext = scene.LabelNode('Player 2 wins', font=('Avenir', 150), color='#000', position=(self.size.w/2, self.size.h/2), parent=self)
			sys.exit()
		if player2['HP'] <= 0:
			scene.fill("#fff")
			scene.rect(0, 0, 2000, 2000)
			self.wintext = scene.LabelNode('Player 1 wins', font=('Avenir', 150), color='#000', position=(self.size.w/2, self.size.h/2), parent=self)
			sys.exit()
	

#print(DMGcalc(playablecharacters[0], playablecharacters[0], 'Normal Attack'))

#print(scene.get_screen_size()) #1080 810

scene.run(mainScene())
