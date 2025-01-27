import random

# Setup
diceOptions = list(range(1, 7))
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

# Display available weapons
print("Available Weapons:")
for index, weapon in enumerate(weapons, 1):
    print(f"{index}. {weapon}")

# Player inputs and validation
while True:
    try:
        combatStrength = int(input("Enter your combat strength (1-6): "))
        if combatStrength < 1 or combatStrength > 6:
            print("Please enter a value between 1 and 6.")
            continue
        mCombatStrength = int(input("Enter monster's combat strength (1-6): "))
        if mCombatStrength < 1 or mCombatStrength > 6:
            print("Please enter a value between 1 and 6.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")

# Battle sequence
for j in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll

    # Determine selected weapons based on dice rolls
    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    print(f"Round {j}: Hero rolled {heroRoll}, Monster rolled {monsterRoll}.")
    print(f"Hero selected: {heroWeapon}, Monster selected: {monsterWeapon}.")
    print(f"Hero Total Strength: {heroTotal}, Monster Total Strength: {monsterTotal}.")
    
    # Determine winner
    if heroTotal > monsterTotal:
        print("Hero wins the round!")
    elif heroTotal < monsterTotal:
        print("Monster wins the round!")
    else:
        print("It's a tie!")
    
    # Battle truce condition
    if j == 11:
        print("Battle Truce declared in Round 11. Game Over!")
        break
    print()
