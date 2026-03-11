# Challenge One: The Mining Engine


"""
PROCEDURE mining(inventoryPick, gem_inventory, gemstones, rarity) {
    DISPLAY "You head down to the mines..."
    
    IF (inventoryPick = "basic"){
        start_percent ← 30
    } ELSE IF (inventoryPick = "good"){
        start_percent ← 50
    } ELSE IF (inventoryPick = "better"){
        start_percent ← 70
    } ELSE {
        start_percent ← 90
    }
    
    DISPLAY "You swing your pick at the rock..."
    
    chance ← start_percent
    keepSwinging ← "y"
    
    REPEAT UNTIL (keepSwinging ≠ "y" AND keepSwinging ≠ "Y") {
        DISPLAY "Swing? Y/N"
        keepSwinging ← INPUT()
        
        IF (keepSwinging = "y" OR keepSwinging = "Y") {
            DISPLAY "You reveal a little more gemstone..."
            chance ← chance + 5
        }
        ELSE {
            roll ← RANDOM(1, 100)
            
            IF (roll ≤ chance) {
                // Pick a random gem and rarity using 1-based indexing
                gem_name ← gemstones[RANDOM(1, LENGTH(gemstones))]
                gem_rarity ← rarity[RANDOM(1, LENGTH(rarity))]
                
                DISPLAY "You carefully uncover a " + gem_name + "!"
                
                // Append as a list: [Name, Value, Rarity]
                newGem ← [gem_name, 0, gem_rarity] 
                APPEND(gem_inventory, newGem)
            }
            ELSE {
                DISPLAY "Unlucky! Your wild swings crack the gem. You'll have to return and try again."
            }
        }
    }
}
"""



def mining(inventory, gem_inventory):
    gemstones = ["diamond", "ruby", "emerald", "topaz", "onyx", "opal", "turquoise", "lapis lazuli"]
    rarity = ["common", "uncommon", "rare", "unique", "fake"]
    
    # Write your translated Python code below this line!
    pass
# --------------------------------------
start_percent = 0

def mining(inventoryPick,gem_inventory,gemstones,rarity)
    print("You head down to the mines...")

    if (inventoryPick = "basic")
        start_percent = 30
    elif (inventoryPick = "good")
        start_percent = 50
    elif (inventoryPick = "better")
        start_percent = 70
    else:
        start_percent = 90
    
    print("You swing your pick at the rock...")

    chance = start_percent
    keepSwinging = "y"

    while keepSwinging = "y" and keepSwinging = "Y"
        print("Swing? Y/N")
        keepSwinging = input()

        if keepSwinging = "y" or keepSwinging = "Y"
            print("You reveal a little more gemstone...")
            chance = chance + 5
        else:
            roll = random(1,100)
            
            if (roll <= chance)
            