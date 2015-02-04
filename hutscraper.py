from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

f = urlopen('http://www.dotahut.com/heroes/pudge')
soup = BeautifulSoup(f)
heroName = soup.find('div', attrs={'class': 'name'})
heroList = soup.findAll('div', attrs={'class': 'weak-block'})
weak_hero = heroList[0].findAll('div', attrs={'class': 'name'})
#print('\n' + 'Counters for ' + heroName.text + '\n')

weak_hero_names = [i.text for i in weak_hero]

#print(json.dumps(weak_hero_names))

o = urlopen('http://www.dotahut.com/heroes')
all_heroes = BeautifulSoup(o)
all_heroes_list = all_heroes.find_all('div', attrs={'class': 'champions'})
list_of_names = all_heroes_list[0].findAll('a')
#print(list_of_names)
''' turn into array then turn it into a string using json and save as a string file '''
super_list = ["abbadon", "alchemist", "ancient_apparition", "anti_mage", "axe",
     "bane_elemental", "batrider", "beastmaster", "bloodseeker", "bounty_hunter",
     "brewmaster", "bristleback", "broodmother", "centaur_warrunner", "chaos_knight",
     "chen", "clinkz", "clockwerk", "crystal_maiden", "dark_seer", "dazzle", "death_prophet", "disruptor", "doom",
     "dragon_knight",
     "drow_ranger", "earth_spirit", "earthshaker", "elder_titan", "ember_spirit",
     "enchantress", "enigma", "faceless_void", "gyrocopter", "huskar",
     "invoker", "io", "jakiro", "juggernaut", "keeper_of_the_light", "kunkka", "legion_commander", "leshrac", "lich",
     "lifestealer", "lina", "lion", "lone_druid", "luna", "lycanthrope", "magnus", "medusa", "meepo", "mirana",
     "morphling", "naga_siren", "natures_prophet", "necrolyte", "night_stalker", "nyx_assassin", "ogre_magi",
     "omniknight", "outworld_devourer", "phantom_assassin", "phantom_lancer", "phoenix", "puck", "pudge", "pugna",
     "queen_of_pain", "razor", "riki", "rubick", "sand_king", "shadow_demon", "shadow_fiend", "shadow_shaman",
     "silencer", "skywrath_mage", "slardar", "slark", "sniper", "spectre", "spirit_breaker", "storm_spirit", "sven",
     "templar_assassin", "terrorblade", "tidehunter", "tinker", "tiny", "treant_protector", "troll_warlord",
     "tusk", "undying", "ursa", "vengeful_spirit", "venomancer", "viper", "visage", "warlock", "weaver", "windranger",
     "witch_doctor", "wraith_king", "zeus"
]

x = (json.dumps(super_list))
bytes(x, 'utf-8')

banana = open('the_hero_list.txt', 'wt')
banana.write(json.dumps(x))
