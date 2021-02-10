
# Programmeringsvurdering våren 2021

# Enkelt battle system utviklet av Tien og Vincent (2021)

import console, scene, random

#
# PLAYABLE CHARACTERS
#

playablecharacters = [{
	'name': 'Lumine',
	'HP': 500,
	'ATK': 50,
	'DEF': 50,
	'SPE': 100,
	'attacks': {
		'Normal Attack': (20, 95) # (atk, accuracy), senere implement element!
	}
}] # Mulighet til å legge til flere karakterer rett før ]

#
# FUNKSJONER (F.EKS. BATTLE MECHANICS)
#

def damageCalc(player, opponent): # player og opponent er i dictionary formatet importert fra playablecharacters
	pass

#
# USER INTERFACE
#

class mainScene(scene.Scene):
	def setup(self):
		self.background_color = '#ffffff'

scene.run(mainScene())
