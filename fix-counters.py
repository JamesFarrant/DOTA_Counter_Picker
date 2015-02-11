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

import json

def fix_name(name):
    name = str(name)
    name = name.lower()
    name = name.replace('  ','_')
    name = name.replace(' ','_')
    name = name.replace('-','_')
    if name=='abbadon': return 'abaddon'
    if name=='nature\'s_prophet': return 'natures_prophet'
    if name=='necrolyte': return 'necrophos'
    if name=='bane_elemental': return 'bane'
    if name=='ember_spirit_': return 'ember_spirit'
    if not name in super_list: print('Unrecognised hero: '+name)
    return name

f = open('hero_counters_old.txt', 'r')
counters_file = f.read()
all_counters = json.loads(counters_file)

all_counters_fixed = {}

for name in all_counters:
    all_counters_fixed[fix_name(name)] = [fix_name(i) for i in all_counters[name]]

#all_names = []
#
#for i in all_counters:
#    all_names += [j for j in all_counters[i]]
#
#all_names += [i for i in all_names]
#all_names = set([fix_name(str(i)) for i in all_names])
#all_names = [i for i in all_names if i in super_list]
#print(all_names)
#


hero_data_file = open('hero_counters.txt', 'wt')
hero_data_file.write(json.dumps(all_counters_fixed,indent=4, separators=(',', ': ')))