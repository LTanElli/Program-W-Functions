from datetime import datetime
import random



def main():

    name()
    print()

    print(f"Race: {race()}")
    print()

    print(f"Class: {cclass()}")
    print()

    print(f"Alignment: {alignment()}")
    print()

    skills()
    print()

    ability()
    print()

    print(f"Extra Language: {language()}")
    print()

    print(f"Background: {background()}")
    print()

    personality_traits()
    print()

    flaws()
    print()

    date_and_time()


    pass


def race():
    # Aarakocra, Dragonborn, Hill Dwarf, Mountain Dwarf, High Elf, Wood Elf, Eladrin Elf, Air Genasi, Fire Genasi, Earth Genasi, Water Genasi, Rock Gnome, Deep Gnome, Goliath, Half-Elf, Half-Orc, Lightfoot Halfling, Stout Halfling, Human, Variant Human, Tiefling, Variant Aasimar, Bugbear, Centaur, Changeling, Deurgar, Fairy, Giant, Firbolg, Githyanki, Githzerai, Goblin, Harengon, Hobgoblin, Kenku, Kobold, Lizardfolk, Minotaur, Orc, Satyr, Sea Elf, Shadar-kai, Shifter, Tabaxi, Tortle, Triton, Yuan-ti, Kender, Astral Elf, Autognome, Giff, Hadozee, Plasmoid, Thri-kreen, Owlin, Leonin, Kalashtar, Warforged, Verdan, Loxodon, Simic Hybrid, Vedalken, Locathah, Grung,
    races = ["Aarakocra", "Dragonborn", "Hill Dwarf", "Mountain Dwarf", "High Elf", "Wood Elf", "Eladrin Elf", "Air Genasi", "Fire Genasi", "Earth Genasi", "Water Genasi", "Rock Gnome", "Deep Gnome", "Goliath", "Half-Elf", "Half-Orc", "Lightfoot Halfling", "Stout Halfling", "Human", "Variant Human", "Tiefling", "Variant Aasimar", "Bugbear", "Centaur", "Changeling", "Deurgar", "Fairy", "Giant", "Firbolg", "Githyanki", "Githzerai", "Goblin", "Harengon", "Hobgoblin", "Kenku", "Kobold", "Lizardfolk", "Minotaur", "Orc", "Satyr", "Sea Elf", "Shadar-kai", "Shifter", "Tabaxi", "Tortle", "Triton", "Yuan-ti", "Kender", "Astral Elf", "Autognome", "Giff", "Hadozee", "Plasmoid", "Thri-kreen", "Owlin", "Leonin", "Kalashtar", "Warforged", "Verdan", "Loxodon", "Simic Hybrid", "Vedalken", "Locathah", "Grung"]

    random_race = random.choice(races)

    return random_race


def name():
    #User creates their own name. 
    print("As of right now, you get to choose your own name.")
    print("Please enter your name:")

    user_name = input(">>> ")

    print()

    print(f"<{user_name}>")
    

def cclass():
    #Barbarian, Bard, Blood Hunter, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard, Articifer, 
    cclasses = ["Barbarian", "Bard", "Blood" "Hunter", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "Articifer"]

    user_class = random.choice(cclasses)

    return user_class


def alignment():
    #Lawful Good, Lawful Neutral, Lawful Evil, Neutral Good, True Neutral, Neutral Evil, Chaotic Good, Chaotic Neutral, Chaotic Evil
    alignments = ["Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "True Neutral", "Neutral Evil", "Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]

    user_alignment = random.choice(alignments)

    return user_alignment


def skills():
    #get two skills to be proficient in.
    #Acrobatics, Animal Handling, Arcana, Athletics, Deception, History, Insight, Intimidation, Investigation, Medicine, Nature, Perception, Performance, Persuasion, Religion, Sleight of Hand, Stealth, Survival
    user_skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]

    random_skills = random.sample(user_skills, 2)

    print("You get two skills to become proficient in aside from what your class/race gives you.")
    print("Any overlaps from your class/race, then choose another skill in place of that overlap.")
    print()
    print(f"Your skills: {random_skills}")


def ability():
    # random number between 8 and 18 for each ability. 
    # get two abiilties to be increased from base role. 
    #Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma
    items = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    random_items = random.choices(items, k=6)

    print()
    print("These are your ability numbers:")
    print(random_items)

    user_abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    random_abilities = random.sample(user_abilities, 2)

    print()
    print(f"You get to increase these two abilities by 1, or choose one of these abilities to increase by 2.")
    print(f"Your Abilities: {random_abilities}")


def language():
    # Abanasinian, Abyssal, Celestial, Daelkyr, Deep Speech, Draconic, Dwarvish, Ergot, Giant, Gith, Gnomish, Goblin, Hadozee, Halfing, Infernal, Istarian, Kenderspeak, Khalorian, Khur, Kothian, Kraul, Leonin, Loxodon, Marquesian, Minotaur, Naush, Nerakese, Nordmaarian, Ogre, Orc, Primordial, Quori, Riedran, Solamnic, Sylvan, Thri-kreen, Undercommon, Vedalken, Zemnian
    user_languages = ["Abanasinian", "Abyssal", "Celestial", "Daelkyr", "Deep Speech", "Draconic", "Dwarvish", "Ergot", "Giant", "Gith", "Gnomish", "Goblin", "Hadozee", "Halfing", "Infernal", "Istarian", "Kenderspeak", "Khalorian", "Khur", "Kothian", "Kraul", "Leonin", "Loxodon", "Marquesian", "Minotaur", "Naush", "Nerakese", "Nordmaarian", "Ogre", "Orc", "Primordial", "Quori", "Riedran", "Solamnic", "Sylvan", "Thri-kreen", "Undercommon", "Vedalken", "Zemnian"]

    random_language = random.choice(user_languages)

    return random_language


def flaws():
    # get 2 or 3 of these

    # Anxious all the time
    # Arrogant
    # Sticky fingers, even when they dont want to
    # No sense of direction
    # Says things bluntly without trying
    # Sex addict
    # Dyslexic
    # Color Blind
    # Flatulence disorder, but, always happens at the worst time
    # Extremely flirty, even when you are not attracted to them
    # Extremely gullible, despite intelligence 
    # Illiterate
    # Extremely klutzy
    # Subconsious stripper, takes clothes off without thinking
    # Alcoholic
    # Cannot tolerate the presence of cheese
    # Small bladder
    # Paranoid that everyone is out to get them all the time
    # You have a terrible stuttering problem
    # You have a crippling addiction to milk
    # Passes out at the sight of bugs
    # Easily distracted by anything shiny or any weapon lying around
    # Can't turn left
    # Extremely superstitious
    # A really bad smoking habit
    # Smells bad all the time, no matter what you do
    # Loves starting fights between other people
    # obsessed with food and will relate almost everything that is happening to some kind of food
    # Hiccups at the worst times. Even if you didn't eat recently
    # Never learned to swim
    user_flaws = ["Anxious all the time", "Arrogant", "Sticky fingers even when they dont want to", "No sense of direction", "Says things bluntly without trying", "Sex addict", "Dyslexic", "Color Blind", "Flatulence disorder, but, always happens at the worst time", "Extremely flirty, even when you are not attracted to them", "Extremely gullible, despite intelligence" , "Illiterate", "Extremely klutzy", "Subconsious stripper, takes clothes off without thinking", "Alcoholic", "Cannot tolerate the presence of cheese", "Small bladder", "Paranoid that everyone is out to get them all the time", "You have a terrible stuttering problem", "You have a crippling addiction to milk", "Passes out at the sight of bugs", "Easily distracted by anything shiny or any weapon lying around", "Can't turn left", "Extremely superstitious", "A really bad smoking habit", "Smells bad all the time, no matter what you do", "Loves starting fights between other people", "obsessed with food and will relate almost everything that is happening to some kind of food", "Hiccups at the worst times. Even if you didn't eat recently", "Never learned to swim"]

    random_flaws = random.sample(user_flaws, 2)

    print(f"Your Flaws: {random_flaws}")


def background():
    # Acolyte, Criminal, Spy, Folk Hero, Haunted One, Noble, Sage, Soldier, Librarian, Sailor, Pirate, Merchant, Adopted, Archeoligist, City Watch, Scholar, Miner, Entertainer, Gladiator, Hermit, Smuggler, Investigator, Bandit, Bounty Hunter, Alchemist, Alcoholic, Amnesiac, Arranged Marriage Escapee, Farmer, Stripper, Slave, Monster Hunter, Gambler, Debtor, Cultist, Puppeteer, Sex Worker, War Criminal, Blacksmith, Train Conductor, 
    user_backgrounds = ["Acolyte", "Criminal", "Spy", "Folk Hero", "Haunted One", "Noble", "Sage", "Soldier", "Librarian", "Sailor", "Pirate", "Merchant", "Adopted", "Archeoligist", "City Watch", "Scholar", "Miner", "Entertainer", "Gladiator", "Hermit", "Smuggler", "Investigator", "Bandit", "Bounty Hunter", "Alchemist", "Alcoholic", "Amnesiac", "Arranged Marriage Escapee", "Farmer", "Stripper", "Slave", "Monster Hunter", "Gambler", "Debtor", "Cultist", "Puppeteer", "Sex Worker", "War Criminal", "Blacksmith", "Train Conductor"]
    random_background = random.choice(user_backgrounds)
    return random_background


def personality_traits():
    # get three of these?

    # I'm always polite and respectful
    # I have a very crude sense of humor
    # I face problems head on
    # I am very generous and caring
    # I am very Humble
    # I am very optimistic
    # I have lost a lot of friends and family, so I don't get attached easily
    # I spent my early youth in a kitchen and became good at cooking
    # I do not like kids, but kids like me
    # I change my voice and accent as often and easily as changing hats or clothes
    # I am incredibly unlucky
    # My favorite weapon has a name and I talk to it like it is a living being
    # I have an anecdote for EVERYTHING
    # I suspect everyone i meet of being the villain who killed my father until proven otherwise
    # I lack any sense of shame and will grovel and beg and plead my way out of anything
    # I have a good sense of smell, that can sometimes tell me if someone is genuine or not, when I meet new people I sometimes smell them
    # I am a masochist
    # Whether or not it is true, I firmly believe that I speak cat
    # I never stop smiling, some find this creepy
    # I am compulsive liar
    # I am really nervous around any animals
    # Believes he is safe no matter what as long as someone ties a rope to them
    # I hit poses after saying something epic or doing something epic. Although what is epic to me may not be epic to others.
    # I am self centered
    # I love to try different kinds of food.
    # I am quiet and reserved
    # I get turned on by new or cool or sharp weapons
    # I love animal like people (heteromorphs)
    # I have a hard time expressing feelings to other people
    # I have no sense of fashion
    # I never smile or get excited about anything
    # It is physically and mentally impossible for me to tell a lie
    # I am very adventurous, which can lead to some dumb decisions
    user_traits = ["I'm always polite and respectful", "I have a very crude sense of humor", "I face problems head on", "I am very generous and caring", "I am very Humble", "I am very optimistic", "I have lost a lot of friends and family, so I don't get attached easily", "I spent my early youth in a kitchen and became good at cooking", "I do not like kids, but kids like me", "I change my voice and accent as often and easily as changing hats or clothes", "I am incredibly unlucky", "My favorite weapon has a name and I talk to it like it is a living being", "I have an anecdote for EVERYTHING", "I suspect everyone i meet of being the villain who killed my father until proven otherwise", "I lack any sense of shame and will grovel and beg and plead my way out of anything", "I have a good sense of smell, that can sometimes tell me if someone is genuine or not, when I meet new people I sometimes smell them", "I am a masochist", "Whether or not it is true, I firmly believe that I speak cat", "I never stop smiling, some find this creepy", "I am compulsive liar", "I am really nervous around any animals", "Believes he is safe no matter what as long as someone ties a rope to them", "I hit poses after saying something epic or doing something epic. Although what is epic to me may not be epic to others.", "I am self centered", "I love to try different kinds of food", "I am quiet and reserved", "I get turned on by new or cool or sharp weapons", "I love animal like people (heteromorphs)", "I have a hard time expressing feelings to other people", "I have no sense of fashion", "I never smile or get excited about anything", "It is physically and mentally impossible for me to tell a lie", "I am very adventurous, which can lead to some dumb decisions"]

    random_traits = random.sample(user_traits, 3)

    print(f"Your Traits: {random_traits}")


def date_and_time():
    current_time = datetime.now()
    print(f"{current_time:%c}")


# if "__name__" == "__main__":
main()