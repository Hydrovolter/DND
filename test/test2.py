races = ["human", "elf", "dwarf", "half-orc", "tiefling", "half-elf", "dragonborn", "gnome", "halfling"] # added from dwarf [3]
racePrint = "\nRaces:\n"
for race in races:
    racePrint = racePrint + "\n" + race.capitalize()
print(racePrint)
