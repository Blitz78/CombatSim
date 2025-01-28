import random, os, time 

victorious_phrases = [
  " beats ",
  " utterly defeats ",
  " triumphantly bests ",
]
def get_random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return f"\033[38;2;{r};{g};{b}m"

def roll_dice(sides):
  result = random.randint(1, sides)
  return result

def roll_health_stats():
  health = ((roll_dice(6) * roll_dice(12)) / 2) + 10
  return health

def roll_strength_stats():
  strength = ((roll_dice(6) * roll_dice(8)) / 2) + 12
  return strength

def start_battle(player1, player2):
  print("\nBattle started!\n")
  while player1['health'] > 0 and player2['health'] > 0:
    player1_attack = roll_dice(6)
    player2_attack = roll_dice(6)
    player2['health'] -= player1_attack

    print(f"\033[0m{player1['name'].title()} hits {player2['name'].title()} for {player1_attack} points of damage! {player2['name'].title()} has {player2['health']:.2f} health remaining!")
    time.sleep(1)

    if player2['health'] <= 0:
      break
    
    player1['health'] -= player2_attack
    print(f"\033[0m{player2['name'].title()} hits {player1['name'].title()} for {player2_attack} points of damage! {player1['name'].title()} has {player1['health']:.2f} health remaining!")
    time.sleep(1)

    os.system('clear')

  if player1['health'] > player2['health']:
    victorious_phrase = random.choice(victorious_phrases)
    print(f"\033[0m{player1['name'].title()}{victorious_phrase}{player2['name'].title()}!")
  elif player2['health'] > player1['health']:
    victorious_phrase = random.choice(victorious_phrases)
    print(f"\033[0m{player2['name'].title()}{victorious_phrase}{player1['name'].title()}!") 

  time.sleep(2)

  os.system('clear')

  return

while True:
  player1_name = input("Enter your character name: ").strip().lower()
  while True:
    selected_race = input("Enter your selected race (Human, Dwarf, Goliath, Elf, Tiefling, Gnome, Orc, Drow, or Other): ").strip().title()
    
    if selected_race in ["Human", "Dwarf", "Goliath", "Elf", "Tiefling", "Gnome", "Orc", "Drow", "Other"]:
      break
    else:
      print("Invalid race.")

  if selected_race.lower() == 'other':
    selected_race = input('Enter your selected race: ').strip().title().lower()

  player1_health = roll_health_stats()
  player1_strength = roll_strength_stats()

  text_color = get_random_color()
  print(f"{text_color}{player1_name.title()}'s stats:")
  print("\033[0m" + selected_race.title())
  print("\033[0m" + f"{player1_health} (Health)")
  print("\033[0m" + f"{player1_strength} (Strength)")
  
  player2_name = input("Enter opponent's Name: ").strip().lower()
  while True:
    selected_race = input("Enter opponent's selected race (Human, Dwarf, Goliath, Elf, Tiefling, Gnome, Orc, Drow, or Other): ").strip().title()
    
    if selected_race in ["Human", "Dwarf", "Goliath", "Elf", "Tiefling", "Gnome", "Orc", "Drow", "Other"]:
      break
    else:
      print("Invalid race.")

  if selected_race.lower() == 'other':
    selected_race = input('Enter opponent\'s selected race: ').strip().title().lower()
  
  player2_health = roll_health_stats()
  player2_strength = roll_strength_stats()

  print(f"{text_color}{player2_name.title()}'s stats:")
  print("\033[0m" + selected_race.title())
  print("\033[0m" + f"{player2_health} (Health)")
  print("\033[0m" + f"{player2_strength} (Strength)")

  start_battle({'name': player1_name, 'health': player1_health}, {'name': player2_name, 'health': player2_health})

  another_round = input("\nDo you want to roll stats for another character? (y/n) ").strip().lower()
  
  if another_round.lower() == "n" or another_round.lower() == "no":
    os.system("clear") 
    break
  elif another_round.lower() == "y" or another_round.lower() == "yes":
    os.system("clear")
    continue
  else:
    print("Invalid input. Please enter 'y' or 'n'")

print("\nThank you for playing!")
time.sleep(1)
os.system("clear")