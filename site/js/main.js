var HERO_LIST = ["abaddon", "alchemist", "ancient_apparition", "anti_mage", "axe",
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

var EXTRA_NAMES     = ["oh joy", "GUESS WHO","kotl","tide","am","beast","bh","brew","cm","seer"]
var EXTRA_NAME_REAL = ["sniper", "juggernaut","keeper_of_the_light","tidehunter","anti_mage","beastmaster","bloodseeker","brewmaster","crystal_maiden","dark_seer"]
var FUZZY_HEROES = FuzzySet(HERO_LIST.concat(EXTRA_NAMES))

var picked_team = []
var picked_formation = "212"

function pretty_name(name) {
  return name.replace(/_/g," ").toUpperCase()
}

function fix_name(name) {
    if(EXTRA_NAMES.indexOf(name) != -1) {
        return EXTRA_NAME_REAL[EXTRA_NAMES.indexOf(name)]
    }
    return name
}

function setForm(form) {
  picked_formation = form
  chooseTeam()
}

function updateBox() {
    var hero_entry = document.getElementById('hero_entry')
    var hero_guess = document.getElementById('hero_guess')

    matches = FUZZY_HEROES.get(hero_entry.value)
    if(matches == null || matches.length == 0) { return; }
    hero_guess.innerHTML = getHeroCode(fix_name(matches[0][1]),matches[0][1])
}

function chooseHero() {
    if(picked_team.length > 4) { return; }
    var hero_entry = document.getElementById('hero_entry')
    matches = FUZZY_HEROES.get(hero_entry.value)
    if(matches == null || matches.length == 0) { return; }
    hero_entry.value = ""
    hero = fix_name(matches[0][1])
    if(picked_team.indexOf(hero) == -1) {

      picked_team.push(hero)

      updateEnemyPicks()

      chooseTeam()
    }
}

function removePick(name) {
  if(picked_team.indexOf(name) != -1) {
    picked_team.splice(picked_team.indexOf(name),1)
  }
  updateEnemyPicks()
  chooseTeam()
}

function updateEnemyPicks() {
  var enemy_picks = document.getElementById('enemy_picks')
  enemy_picks.innerHTML = '<div class="role_name">Picks</div>'
  for(var i in picked_team) {
    enemy_picks.innerHTML += 
              "<div class='role_pick' onclick='removePick(\""+picked_team[i]+"\")'>" +
                getHeroCode(picked_team[i]) +
              "</div>";
  }
}

function checkSubmit(e) {
   if(e && e.keyCode == 13)
   {
      chooseHero();
   }
}

function getHeroCode(name,displayName) {
  if(displayName==null) { displayName = name}
  return '<div class="hero_card"><i class="d2mh '+name+'"></i><p>'+pretty_name(displayName)+'</p></div>'
}
var result

function chooseTeam() {
    picks = [document.getElementById('role_1_picks'),
             document.getElementById('role_2_picks'),
             document.getElementById('role_3_picks'),
             document.getElementById('role_4_picks'),
             document.getElementById('role_5_picks')]

    $.ajax({
      url: "get_counters",
      data: {"form":picked_formation,"enemies":JSON.stringify(picked_team)},
      context: document.body,
      success: function(data){
        result = JSON.parse(data);
        var i = 0;
        for(var role in result) {
          picks[i].innerHTML = "<div class='role_name'>"+role+"</div>"
          for(var j in result[role]) {
            picks[i].innerHTML += 
              "<div class='role_pick'>" +
                getHeroCode(result[role][j][0]) +
              "</div>";
          }
          i++;
        }
      }
  });
}