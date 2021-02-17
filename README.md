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
  - Utility: Grants Lumine +50 Attack and has a 5% chance of failing
