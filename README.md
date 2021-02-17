# battleSystem
## Skoleoppgave
### Background
Our final project in our programming classes was to create a program freely of choice, and this is my (Tien) and my friend's (Vincent) work!

It is a relatively simple battle system composed of characters and various attacks, heavily inspired by Pokemon Showdown.
Other core elements such as elements and reactions are inspired by Genshin Impact.
### Documentation
#### Prerequisites
This program is made in Pythonista on iOS, and the scene module will only work on that application. Tested and developed with Python 3.7.
It's designed to only work on iPad (7th Generation) on landscape mode (Pythonista doesn't allow forced orientation) and with no split screen. However it may work on other devices with the same resolution.
#### UI and Layout
There are 4 buttons presented to you upon starting the program.
On all buttons will there say a short description of what it'll do. The four main (but changeable) labels are 'Normal Attack', 'Primary Skill', 'Secondary Skill' and 'Utility'. Upon pressing one of the buttons, the current active character will perform that attack on the opponent.
If you press on the area of your character's sprite, then the stats of that character will show up. Pressing anywhere else will remove this text.
On the topleft corner of the screen it will display whose turn it is.
Note that when a character name is used, brackets with the players # will also be there in parenthesis to clarify further.
#### Core Game Mechanics
All characters have 3 offensive attacks and 1 non damaging move.
Critical hits deal 2x damage.
Primary and Secondary Skill will always apply an element to the opponent.
The applied element lasts for 3 entire rounds.
If another element is applied to a coexisting element, then an elemental reaction will occour.
These reactions are described in this image: https://i.imgur.com/VjlcUdM.png
The reactions can be decribed as following:
##### Elemental Reactions
- Pyro + Hydro = Vaporize 
  - The attack triggering the reaction has a multiplier of 2 or 1.5
  - The multiplier will be 2 if Hydro was the triggering element
  - The multiplier will be 1.5 if Pyro was the triggering element
- Pyro + Cryo = Melt
  - The attack triggering the reaction has a multiplier of 2 or 1.5
  - The multiplier will be 2 if Pyro was the triggering element
  - The multiplier will be 1.5 if Cryo was the triggering element
- Pyro + Electro = Overload
  - Always does a flat damage amount / Ignores defense
- Pyro + Dendro = Burning
  - Applies a Damage Over Time, which deals damage every halfturn based on the character's current health
  - This means that the DOT will do more damage the healthier the opponent is
- Hydro + Electro = Electro Charged
  - Applies a Damage Over Time, which deals damage every halfturn based on the character's missing health
  - This means that the DOT will do more damage the weaker the opponent is
- Hydro + Cryo = Freeze
  - Applies a status effect where the character cannot do any action, with increasing probability to thaw out every halfturn
  - This chance starts at 1/4 initially, and the denominator decreases by 1 every halfturn.
- Cryo + Electro = Superconduct
  - Divides defense in half
- Anemo + Any element = Swirl
  - Divides elemental resistance in half
- Geo + Any element = Crystallize
  - Increases own defense and elemental resistance by 15 and heals the player
  - The healing bypasses max hp, allowing for an overheal

The order of element infliction does matter. This is for instance described in the Melt and Vaporize reactions. If Anemo is the initial element, then the reaction will always be Swirl, and the same counts for Geo. Anemo + Geo = Swirl / Geo + Anemo = Crystallize.

#### Characters

##### Lumine
- HP: 1000
- ATK: 70
- ELEATK: 100
- DEF: 45
- ELERES: 30
- SPE: 100
- Crit Rate: 15
- Attacks:
  - Normal Attack: 80 base power, 90% accuracy, Physical
  - Primary Skill: 90 base power, 80% accuracy, Anemo
  - Secondary Skill: 60 base power, 100% accuracy, Geo
  - Utility: (Swords Dance) Grants Lumine +50 Attack and has a 5% chance of failing

##### Aether
- HP: 1750
- ATK: 30
- ELEATK: 20
- DEF: 60
- ELERES: 60
- SPE: 80
- Crit Rate: 0
- Attacks:
  - Normal Attack: 100 base power, 90% accuracy, Physical
  - Primary Skill: 90 base power, 80% accuracy, Geo
  - Secondary Skill: 60 base power, 90% accuracy, Anemo
  - Utility: (Defense Curl) Grants Aether +50 Defense and has a 5% chance of failing

##### Childe
- HP: 1250
- ATK: 50
- ELEATK: 25
- DEF: 50
- ELERES: 50
- SPE: 95
- Crit Rate: 10
- Attacks:
  - Normal Attack: 70 base power, 90% accuracy, Physical
  - Primary Skill: 80 base power, 80% accuracy, Hydro
  - Secondary Skill: 100 base power, 90% accuracy, Electro
  - Utility: (Delusion) Grants Childe +50 Attack and +50 Elemental Attack

##### Madame Ping
- HP: 1000
- ATK: 25
- ELEATK: 75
- DEF: 50
- ELERES: 50
- SPE: 50
- Crit Rate: 0
- Attacks:
  - Normal Attack: 50 base power, 90% accuracy, Physical
  - Primary Skill: 90 base power, 95% accuracy, Dendro
  - Secondary Skill: 120 base power, 90% accuracy, Pyro
  - Utility: (Tea Drink) Grants Madame Ping +250 HP

##### Razor
- HP: 1500
- ATK: 50
- ELEATK: 50
- DEF: 50
- ELERES: 50
- SPE: 80
- Crit Rate: 10
- Attacks:
  - Normal Attack: 60 base power, 90% accuracy, Physical
  - Primary Skill: 100 base power, 95% accuracy, Electro
  - Secondary Skill: 80 base power, 85% accuracy, Cryo
  - Utility: (Elemental Burst) Grants Razor +50 of Defense, Attack, Elemental Resistance and Elemental Attack

##### Klee & Co
- HP: 1250
- ATK: 25
- ELEATK: 75
- DEF: 50
- ELERES: 50
- SPE: 110
- Crit Rate: 25
- Attacks:
  - Normal Attack: 80 base power, 90% accuracy, Pyro
  - Primary Skill: 80 base power, 90% accuracy, Electro
  - Secondary Skill: 80 base power, 90% accuracy, Cryo
  - Utility: (Elemental Spores) Decreases opponent's Elemental Resistance
