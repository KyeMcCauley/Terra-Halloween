import random
import time

CANDY_TYPES = {
  "common": ["Candy Corn", "Fun Size Snickers", "Lolli-pop", "Tootsie Roll"]
  "rare": ["Full Size Hershey Bar", "King Sized Reese's", "Glow-in-the-dark Ring"]
  "cursed": ["Mystery Bean", "Black Licorice", "Toothbrush"]
}

TRICKS = [
  "A jump scare from a hidden speaker!",
  "The homeowner wears a terrifying clown mask!",
  "A fake spider drops on your head!",
  "You got sprayed with silly string!"
]

player = {
  "name": "",
  "candy_bag": [],
  "fear_level": 0,     #Game ends when fear hits 100
  "stamina": 100,
  "inventory": []
}

def clear_console():
  print("\n" * 3)

def show_status():
  print("=" * 40)
  print(f"👻 PLAYER: {player['name']} | 🎚️ FEAR: {player['fear_level']}/100 | ⚡ STAMINA: {player['stamina']}/100")
  print(f"🎒 CANDY BAG ({len(player['candy_bag'])} items): {', '.join(player['candy_bag']) if player['candy_bag'] else 'Empty'}")
  if player['inventory"]:
    print(f"💼 ITEMS: {', '.join(player['inventory'])}")
  print("=" * 40)

  def knock_on_door():
    if player["stamina"] <= 10:
      print("❌ You are too tired to trick-or-treat! Rest up or find a safe house.")
      return

    player["stamina"] -= 10
    print("\n✊ Knock, knock, knock...")
    time.sleep(1)

    outcome = random.random()

    if outcome < 0.70:
      rarity_roll = random.random()
      if rarity_roll < 0.15:
        candy = random.choice(CANDY_TYPES["rare"])
        print(f"✨ JACKPOT! You received a RARE treat: {candy}!")
      elif rarity_roll < 0.80:
        candy = random.choice(CANDY_TYPES["common"])
        print(f"🍬 Sweet! You received: {candy}.")
      else:
        candy = random.choice(CANDY_TYPES["cursed"])
        print(f"🤢 Oh no... They handed you a cursed item: {candy}.")
        player["fear_level"] +=5

      player["candy_bag"].append(candy)
    else:
      trick = random.choice(TRICKS)
      print(f"🎃 TRICKED! {trick}")
      fear_gain = random.randint(15, 30)
      player["fear_level"] += fear_gain
      print(f"📈 Your fear level rose by {fear_gain}!")

def main():      ## main game loop
  clear_console()
  print("🎃 WELCOME TO THE HALLOWEEN ADVENTURE 🎃")
  print("Can you fill your bag before your stamina runs out or fear takes over?")

  player["name"] = input "\nEnter your trick-or-treater's name: ").strip()
  if not player["name"]:
    player["name"] = "Spooky Coder"
