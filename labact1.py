POUNDS_TO_KILOGRAMS = 0.453592
MILES_TO_KILOMETERS = 1.60934
FAHRENHEIT_TO_CELSIUS_OFFSET = 32
FAHRENHEIT_TO_CELSIUS_SCALE = 5/9

pounds = 132
miles = 75
fahrenheit = 59

kilograms = pounds * POUNDS_TO_KILOGRAMS
kilometers = miles * MILES_TO_KILOMETERS
celsius = (fahrenheit - FAHRENHEIT_TO_CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_SCALE

student_ages = [17, 21, 22, 18, 21, 23, 20, 17, 24, 19]
average_age = sum(student_ages) / len(student_ages)

character_names = ["Aldric", "Elara", "Thorne", "Lyria", "Draven"]
equipment_names = ["Serpent's Fang", "Phoenix Shield", "Starfall Bow", "Dragonfire Sword", "Mystic Robes"]
item_names = ["Elixir of Wisdom", "Amulet of Eternal Fire", "Crystal of Truth", "Shadow Cloak", "Sorcerer's Staff"]
ability_names = ["Frost Nova", "Inferno Burst", "Lightning Strike", "Teleportation", "Mind Control"]

print("Weight Conversion:")
print(f"{pounds} pounds is equal to {kilograms:.2f} kilograms")

print("\nDistance Conversion:")
print(f"{miles} miles is equal to {kilometers:.2f} kilometers")

print("\nTemperature Conversion:")
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius")

print("\nStudent Ages:")
for i, age in enumerate(student_ages, start=1):
    print(f"Student {i}: {age} years old")
print(f"Average Age: {average_age:.2f} years")

print("\nFantasy Story:")
story = f"""
Once upon a time in the mystical land of Eldoria, there lived five brave adventurers:
- {character_names[0]}, wielding the {equipment_names[0]}, known for their {ability_names[0]} ability.
- {character_names[1]}, the guardian of the {equipment_names[1]}, master of {ability_names[1]}.
- {character_names[2]}, the archer with the legendary {equipment_names[2]} and the deadly {ability_names[2]}.
- {character_names[3]}, a sorceress draped in the {equipment_names[3]}, who could cast {ability_names[3]} at will.
- {character_names[4]}, the enigmatic rogue, cloaked in the {equipment_names[4]} and a master of {ability_names[4]}.

Their journey began with the discovery of the {item_names[0]}, a relic said to grant boundless wisdom.
With the {item_names[1]} and the {item_names[2]} in hand, they set out to face the shadows, protected by the {equipment_names[4]}.
But it was {character_names[2]}, the archer, who held the power of the {item_names[3]}, an ability to traverse realms with {ability_names[3]}.

Their destinies intertwined as they ventured deeper into the unknown, their tale forever etched in the annals of Eldoria.
"""
print(story)