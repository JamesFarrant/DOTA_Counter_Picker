from operator import itemgetter
import json

super_list = ["abbadon", "alchemist", "ancient_apparition", "anti_mage", "axe",
              "bane_elemental", "batrider", "beastmaster", "bloodseeker", "bounty_hunter",
              "brewmaster", "bristleback", "broodmother", "centaur_warrunner", "chaos_knight",
              "chen", "clinkz", "clockwerk", "crystal_maiden", "dark_seer", "dazzle", "death_prophet", "disruptor",
              "doom", "dragon_knight", "drow_ranger", "earth_spirit", "earthshaker", "elder_titan", "ember_spirit",
              "enchantress", "enigma", "faceless_void", "gyrocopter", "huskar",
              "invoker", "io", "jakiro", "juggernaut", "keeper_of_the_light", "kunkka", "legion_commander", "leshrac",
              "lich", "lifestealer", "lina", "lion", "lone_druid", "luna", "lycanthrope", "magnus", "medusa", "meepo",
              "mirana", "morphling", "naga_siren", "natures_prophet", "necrolyte", "night_stalker", "nyx_assassin",
              "ogre_magi", "omniknight", "outworld_devourer", "phantom_assassin", "phantom_lancer", "phoenix", "puck",
              "pudge", "pugna", "queen_of_pain", "razor", "riki", "rubick", "sand_king", "shadow_demon",
              "shadow_fiend", "shadow_shaman", "silencer", "skywrath_mage", "slardar", "slark", "sniper", "spectre",
              "spirit_breaker", "storm_spirit", "sven", "templar_assassin", "terrorblade", "tidehunter", "tinker",
              "tiny", "treant_protector", "troll_warlord", "tusk", "undying", "ursa", "vengeful_spirit",
              "venomancer", "viper", "visage", "warlock", "weaver", "windranger", "witch_doctor", "wraith_king", "zeus"]


f = open('Counter_dictionary.txt', 'r')
counters_file = f.read()

all_counters = json.loads(counters_file)

enemy_team = []
for i in range(1):
    enemy_team.append(input('Add hero > '))

counter_scores = {}

for enemy_hero in enemy_team:
    hero_counters = all_counters[enemy_hero]

    for i in range(1, len(hero_counters)):
        hero = hero_counters[i]
        if hero in enemy_team:
            continue
        if not hero in counter_scores:
            counter_scores[hero] = 0
        counter_scores[hero] += 20 - i


sorted_heroes = sorted(counter_scores.items(), key=itemgetter(1), reverse=True)


for counter in sorted_heroes:
    if counter in enemy_team:
        pass
    else:
        print(counter[0] + ' has a counter score of ' + str(counter[1]))
