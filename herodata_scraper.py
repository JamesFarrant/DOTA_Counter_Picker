super_list = ["abaddon", "alchemist", "ancient_apparition", "anti_mage", "axe",
              "bane", "batrider", "beastmaster", "bloodseeker", "bounty_hunter",
              "brewmaster", "bristleback", "broodmother", "centaur_warrunner", "chaos_knight",
              "chen", "clinkz", "clockwerk", "crystal_maiden", "dark_seer", "dazzle", "death_prophet", "disruptor",
              "doom", "dragon_knight", "drow_ranger", "earth_spirit", "earthshaker", "elder_titan", "ember_spirit",
              "enchantress", "enigma", "faceless_void", "gyrocopter", "huskar",
              "invoker", "io", "jakiro", "juggernaut", "keeper_of_the_light", "kunkka", "legion_commander", "leshrac",
              "lich", "lifestealer", "lina", "lion", "lone_druid", "luna", "lycanthrope", "magnus", "medusa", "meepo",
              "mirana", "morphling", "naga_siren", "natures_prophet", "necrophos", "night_stalker", "nyx_assassin",
              "ogre_magi", "omniknight", "oracle", "outworld_devourer", "phantom_assassin", "phantom_lancer", "phoenix", "puck",
              "pudge", "pugna", "queen_of_pain", "razor", "riki", "rubick", "sand_king", "shadow_demon",
              "shadow_fiend", "shadow_shaman", "silencer", "skywrath_mage", "slardar", "slark", "sniper", "spectre",
              "spirit_breaker", "storm_spirit", "sven", "techies", "templar_assassin", "terrorblade", "tidehunter", "tinker",
              "tiny", "timbersaw", "treant_protector", "troll_warlord", "tusk", "undying", "ursa", "vengeful_spirit",
              "venomancer", "viper", "visage", "warlock", "weaver", "windranger", "witch_doctor", "wraith_king", "zeus"]

from urllib import urlopen
import lxml.html
import json
import re

def hero_name(element):
  h = element.get('href')
  return h[h.rfind('/')+1:h.rfind('-')]

def fix_name(name):
  name = name.replace('-','_')
  if name=="centaur_warchief": return "centaur_warrunner"
  if name=="doom_bringer": return "centaur_warrunner"
  if name=="wisp": return "centaur_warrunner"
  if name=="soul_keeper": return "terrorblade"
  if name=="tuskarr": return "tusk"
  return name

#class HeroData:
#    def __init__(self,element):
#        self.element = element
#        self.name = fix_name(hero_name(i))
#    name = ""
#    is_lane_support = False
#    is_carry = False
#    is_disabler = False
#    is_ganker = False
#    is_initiator = False
#    is_jungler = False
#    is_pusher = False
#    is_roamer = False
#    is_durable = False
#    is_escape = False
#    is_semi_carry = False
#    is_support = False

html = lxml.html.parse('http://www.dotafire.com/dota-2/heroes')
hero_elements = html.xpath('//a[contains(@class,"hero-box")]')

#name_list = [fix_name(hero_name(i)) for i in hero_elements]

heroes = {fix_name(hero_name(i)):i for i in hero_elements}

for h in heroes:
  c = heroes[h].get('class')
  data = {}

  data['is_lane_support'] = 'lane-support' in c
  data['is_carry'] = 'carry' in c
  data['is_disabler'] = 'disabler' in c
  data['is_ganker'] = 'ganker' in c
  data['is_initiator'] = 'initiator' in c
  data['is_jungler'] = 'jungler' in c
  data['is_pusher'] = 'pusher' in c
  data['is_roamer'] = 'roamer' in c
  data['is_durable'] = 'durable' in c
  data['is_escape'] = 'escape' in c
  data['is_semi_carry'] = 'semi-carry' in c
  data['is_support'] = 'support' in c
  data.pop("element",None)

  heroes[h] = data


hero_data_file = open('hero_data.txt', 'wt')
hero_data_file.write(json.dumps(heroes,indent=4, separators=(',', ': ')))