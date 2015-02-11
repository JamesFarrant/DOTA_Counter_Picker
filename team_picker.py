from operator import itemgetter
import json

def get_counter_score(hero, enemy_team):
    score = 0
    my_counters = counters[hero]

    for enemy_hero in enemy_team:
        # do i counter them?
        hero_counters = counters[enemy_hero]

        for i in range(1, len(hero_counters)):
            if hero == hero_counters[i]:
                score += 20 - i 

        # do they counter me?        
        for i in range(1, len(my_counters)):
            if enemy_hero == my_counters[i]:
                score -= 20 - i 

    return score

def has_role(hero, role):
    if not "is_"+role in roles[hero]: return False
    return roles[hero]["is_"+role]

def get_by_role(role):
    return [hero for hero in roles if has_role(hero,role)]

def role_match_score(hero, roles):
    if len(roles) == 0: return 1
    score = 0.0
    for i in roles:
        if has_role(hero,i):
            score += 1
    return score / len(roles)

def fill_formation(formation): 
    t = {}
    for r in formation:
        hero_scores = {
            hero: role_match_score(hero, formation[r])
            for hero in roles
        }
        t[r] = [hero for hero in hero_scores if hero_scores[hero] > 0] # this is a bit bad
    return t

def team_counters(team, enemy_team):
    for r in team:
        team[r] = sort_by_counter(team[r],enemy_team)
    return team

def sort_by_counter(hero_list, enemy_team):
    scored_heroes = [[hero,get_counter_score(hero,enemy_team)] for hero in hero_list]
    sorted_heroes = sorted(scored_heroes, key=itemgetter(1), reverse=True)
    return sorted_heroes

# load in the data

f = open('hero_counters.txt', 'r')
counters_file = f.read()
f.close()

f = open('hero_data.txt', 'r')
data_file = f.read()
f.close()

f = open('formations.txt', 'r')
formations_file = f.read()
f.close()

counters = json.loads(counters_file)
roles = json.loads(data_file)
formations = json.loads(formations_file)

# do things

enemy_heroes = ['silencer','juggernaut','necrophos','phantom_assassin','lion']

team = team_counters(fill_formation(formations["212"]),enemy_heroes)

team = {role_candidates:team[role_candidates][:3] for role_candidates in team}

print("Countering: "+str(enemy_heroes))
print("Formation 2-1-2")

print("Team:")
for role in team:
    print ("  "+role)
    for candidate in team[role]:
        print("    "+str(candidate[0])+ ", "+str(candidate[1]))