from random_character import race, alignment, background
import pytest 


def test_race():
    races = ["Aarakocra", "Dragonborn", "Hill Dwarf", "Mountain Dwarf", "High Elf", "Wood Elf", "Eladrin Elf", "Air Genasi", "Fire Genasi", "Earth Genasi", "Water Genasi", "Rock Gnome", "Deep Gnome", "Goliath", "Half-Elf", "Half-Orc", "Lightfoot Halfling", "Stout Halfling", "Human", "Variant Human", "Tiefling", "Variant Aasimar", "Bugbear", "Centaur", "Changeling", "Deurgar", "Fairy", "Giant", "Firbolg", "Githyanki", "Githzerai", "Goblin", "Harengon", "Hobgoblin", "Kenku", "Kobold", "Lizardfolk", "Minotaur", "Orc", "Satyr", "Sea Elf", "Shadar-kai", "Shifter", "Tabaxi", "Tortle", "Triton", "Yuan-ti", "Kender", "Astral Elf", "Autognome", "Giff", "Hadozee", "Plasmoid", "Thri-kreen", "Owlin", "Leonin", "Kalashtar", "Warforged", "Verdan", "Loxodon", "Simic Hybrid", "Vedalken", "Locathah", "Grung"]

    for _ in range(12):
        test_races = race()
        assert test_races in races
    

def test_alignment():
    alignments = ["Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "True Neutral", "Neutral Evil", "Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]

    for _ in range(12):
        test_alignments = alignment()
        assert test_alignments in alignments 


def test_background():
    backgrounds = ["Acolyte", "Criminal", "Spy", "Folk Hero", "Haunted One", "Noble", "Sage", "Soldier", "Librarian", "Sailor", "Pirate", "Merchant", "Adopted", "Archeoligist", "City Watch", "Scholar", "Miner", "Entertainer", "Gladiator", "Hermit", "Smuggler", "Investigator", "Bandit", "Bounty Hunter", "Alchemist", "Alcoholic", "Amnesiac", "Arranged Marriage Escapee", "Farmer", "Stripper", "Slave", "Monster Hunter", "Gambler", "Debtor", "Cultist", "Puppeteer", "Sex Worker", "War Criminal", "Blacksmith", "Train Conductor"]
    
    for _ in range(12):
        test_backgrounds = background()
        assert test_backgrounds in backgrounds