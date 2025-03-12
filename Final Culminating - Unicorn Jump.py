"""
Tanya
Final Culminating - Unicorn Jump
“Unicorn Jump” is based off of the Google Dinosaur Game, but with additional
unique features.
"""

from graphics import *
from random import randint
win = GraphWin("Unicorn Jump", 632, 400, autoflush = False)

# Game State Variable:
# Game State 0: Main Screen
# Game State 1: Rules Screen
# Game State 2: Credits Screen
# Game State 3: In Game State
# Game State 4: Bonus Life Screen
# Game State 5: Game Over Screen
# Game State 6: New Highscore Screen
gamestate = 0

# Background Image Importation:
p1 = Point(316, 200)
p3 = Point(948, 200)

# Game State 0
gs0 = Image(p1, "gs0.png")
gs1 = Image(p1, "gs1.png")
gs2 = Image(p1, "gs2.png")
gs3 = Image(p1, "gs3.png")
gs4 = Image(p1, "gs4.png")
gs5 = Image(p1, "gs5.png")
gs6 = Image(p1, "gs6.png")

# Sky Statistics:
sky = Image(p1, "sky.png")
cloud1 = Image(p1, "clouds.png")
cloud2 = Image(p3, "clouds.png")
cloud_speed = -5

# General Statistics:
frame_counter = 0
seconds = 0
heads = [Image(p1, "head1.png"),
         Image(p1, "head2.png"),
         Image(p1, "head3.png"),
         Image(p1, "head4.png"),
         Image(p1, "head5.png"),
         Image(p1, "head6.png")]
# If headIndex == 0, heads[0] is drawn
# If headIndex == 1, heads[1] is drawn
# If headIndex == 2, heads[2] is drawn
# If headIndex == 3, heads[3] is drawn
headIndex = 0
headFrameCounter = 1
mouths = [Image(p1, "mouth1.png"),
          Image(p1, "mouth2.png"),
          Image(p1, "mouth3.png"),
          Image(p1, "mouth4.png"),
          Image(p1, "mouth5.png"),
          Image(p1, "mouth6.png")]
# If mouthIndex == 0, mouths[0] is drawn
# If mouthIndex == 1, mouths[1] is drawn
# If mouthIndex == 2, mouths[2] is drawn
# If mouthIndex == 3, mouths[3] is drawn 
mouthIndex = 0
mouthFrameCounter = 1

# Highscore Statistics
p6 = Point(170, 22)
highscore = 0
highscoretxt = Text(p6, highscore)

# Score Statistics
p7 = Point(112, 54)
p10 = Point(154, 383)
score = 0
scoretxt = Text(p7, score)
scoretxt2 = Text(p10, score)
scoretxt2.setFill("white")


# If char_select = 0 no character is selected
# If char_select = 1, unicorn is selected
# If char_select = 2, dinocorn is selected
char_select = 0
moveSpeed = -5

# Main Sprite Statistics
characters = [] # Append the selected character's sprites
characterFrameCounter = 1
characterIndex = 0
characterSpeed = 6
character_is_jumping = False
character_is_ducking = False
character_jumping_speed = -63
character_gravity = 9
# If character_is_colliding = 0, the character is not colliding with the ice cream cone or pig
# If character_is_colliding = 1, the character is colliding with the ice cream cone or pig
# If character_is_colliding = 2, the character is colliding with the ice cream or pig but has a bonus life
character_is_colliding = 0

# Unicorn Statistics
p2 = Point(74, 280)
unicorns = [Image(p2, "Unicorn1.png"),
            Image(p2, "Unicorn2.png"),
            Image(p2, "Unicorn1.png"),
            Image(p2, "Unicorn3.png"),
            Image(p2, "Unicorn4.png"),
            Image(p2, "Unicorn5.png")]

# Dinocorn Statistics
p5 = Point(49, 260)
p11 = Point(76, 286)
dinocorns = [Image(p5, "Dinocorn1.png"),
             Image(p5, "Dinocorn2.png"),
             Image(p5, "Dinocorn1.png"),
             Image(p5, "Dinocorn3.png"),
             Image(p5, "Dinocorn4.png"),
             Image(p11, "Dinocorn5.png")]

# Ice Cream Cone Statistics
p4 = Point(806, 280) 
ice_creams = [Image(p4, "IceCream1.png"),
              Image(p4, "IceCream2.png"),
              Image(p4, "IceCream3.png"),
              Image(p4, "IceCream4.png")] # 1, 2, 3, or 4 cones
ice_creams_index = randint(0, 3)

# Coin Statistics
p8 = Point(806, 150)
p11 = Point(546, 383)
coin = Image(p8, "Coin.png")
numBonus = 0
numBonustxt = Text(p11, numBonus)
numBonustxt.setFill("white")

# Flying Pig Statistics
p9 = Point(806, 217)
pigs = [Image(p8, "FlyingPig.png"),
        Image(p8, "FlyingPig2.png"),
        Image(p9, "FlyingPig.png"),
        Image(p9, "FlyingPig2.png")]
pigsIndex = randint(0, 3)

# If obs_drawn = 1, 2, or 3 ice cream cones come in the screen
# If obs_drawn = 4, a coin comes into the screen
# If obs_drawn = 5, 6, or 7 a flying pig comes into the screen
obs_drawn = randint(1, 7)

obs_speed = -20

# Selection oval Statistics
selections = [Image(p1, "selection1.png"), Image(p1, "selection2.png")]
selectionIndex = 0

# First Frame:
gs0.draw(win)
heads[headIndex].draw(win)
mouths[mouthIndex].draw(win)

# Animation:
while True:
    update()
    time.sleep(0.02)
    k = win.getAllKeys()
    m = win.checkMouse()
    
    if gamestate == 0:
        characterIndex = 0
        # Animate the unicorn's head moving side to side and the dinocorn's
        # mouth opening and closing.
        headFrameCounter += 1
        mouthFrameCounter += 1
        if headFrameCounter == 10 and mouthFrameCounter == 10:
            heads[headIndex].undraw()
            mouths[mouthIndex].undraw()
            headIndex += 1
            mouthIndex += 1
            if headIndex == 2 and mouthIndex == 2:
                headIndex = 0
                mouthIndex = 0
            heads[headIndex].draw(win)
            mouths[mouthIndex].draw(win)
            headFrameCounter = 1
            mouthFrameCounter = 1
            
        # Allow the user to select a character
        # 1) The user selects the unicorn.
        if m != None and 112 <= m.getX() <= 290 and 70 <= m.getY() <= 286:
            characters = []      
            if char_select == 1:
                selections[0].undraw()
            if char_select == 2:
                selections[1].undraw()
            selectionIndex = 0
            selections[selectionIndex].draw(win)
            for i in range(len(unicorns)):
                characters.append(unicorns[i])
            char_select = 1
            
        # 2) The user selects the dinocorn.
        elif m != None and 368 <= m.getX() <= 486 and 70 <= m.getY() <= 330:
            characters = []
            if char_select == 1:
                selections[0].undraw()
            if char_select == 2:
                selections[1].undraw()
            selectionIndex = 1
            selections[selectionIndex].draw(win)
            for i in range(len(dinocorns)):
                characters.append(dinocorns[i])
            char_select = 2
            
        # If the user clicks the "Rules" button, direct them to the rules screen.
        if m != None and 418 <= m.getX() <= 564 and 310 <= m.getY() <= 388:
            gs0.undraw()
            heads[headIndex].undraw()
            mouths[mouthIndex].undraw()
            if char_select != 0:
                selections[selectionIndex].undraw()
            gs1.draw(win)
            gamestate = 1
            
        # If the user clicks the "Credits" button, direct them to the credits
        # screen.
        elif m != None and 60 <= m.getX() <= 210 and 310 <= m.getY() <= 388:
            gs0.undraw()
            heads[headIndex].undraw()
            mouths[mouthIndex].undraw()
            if char_select != 0:
                selections[selectionIndex].undraw()
            gs2.draw(win)
            gamestate = 2
            
        # If the user clicks the "Start" button, direct them to the in-game state.
        elif m != None and 238 <= m.getX() <= 388 and 310 <= m.getY() <= 388 and char_select != 0:
            gs0.undraw()
            heads[headIndex].undraw()
            mouths[mouthIndex].undraw()
            selections[selectionIndex].undraw()
            sky.draw(win)
            gs3.draw(win)
            cloud1.draw(win)
            cloud2.draw(win)
            characters[characterIndex].draw(win)
            obs_drawn = randint(1, 7)
            ice_creams_index = randint(0, 3)
            ice_creams[ice_creams_index].draw(win)
            coin.draw(win)
            pigsIndex = randint(0, 3)
            pigs[pigsIndex].draw(win)
            scoretxt2.draw(win)
            numBonustxt.draw(win)
            gamestate = 3
            
    elif gamestate == 1:
        # If the user clicks the "Back" button, direct them to the main screen
        if m != None and 520 <= m.getX() <= 620 and 330 <= m.getY() <= 390:
            gs1.undraw()
            gs0.draw(win)
            heads[headIndex].draw(win)
            mouths[mouthIndex].draw(win)
            if char_select != 0:
                selections[selectionIndex].draw(win)
            gamestate = 0
            
    elif gamestate == 2:
        # If the user clicks the "Back" button, direct them to the main screen
        if m != None and 520 <= m.getX() <= 620 and 330 <= m.getY() <= 390:
            gs2.undraw()
            gs0.draw(win)
            heads[headIndex].draw(win)
            mouths[mouthIndex].draw(win)
            if char_select != 0:
                selections[selectionIndex].draw(win)
            gamestate = 0
            
    elif gamestate == 3:
        # The foreground doesn't move horizontally, so to give the effect
        # that the character is moving, the background moves:
        cloud1.move(cloud_speed, 0)
        cloud2.move(cloud_speed, 0)
        if cloud1.getAnchor().getX() <= -316:
            cloud1.move(948 - cloud1.getAnchor().getX(), 0)
        if cloud2.getAnchor().getX() <= -316:
            cloud2.move(948 - cloud2.getAnchor().getX(), 0)

        # Every frame, the 1 is added to the score
        frame_counter += 1
        score += 1
        scoretxt2.undraw()
        scoretxt2.setText(score)
        scoretxt2.draw(win)
        if frame_counter == 100:
            frame_counter = 0
            obs_speed *= 1.05
            cloud_speed *= 1.05
            
        # When the user presses the "w" key, the character jumps
        if not character_is_jumping and "w" in k:
            characters[characterIndex].undraw()
            if character_is_ducking:
                characters[5].undraw()
                character_is_ducking = False
            characters[4].draw(win)
            character_is_jumping = True
            
        # Character when jumping
        if character_is_jumping:
            characters[4].move(0, character_jumping_speed)
            character_jumping_speed += character_gravity
            if character_jumping_speed == 72:
                characters[4].undraw()
                characters[characterIndex].draw(win)
                character_is_jumping = False
                character_jumping_speed = -63
                
        # The character walking
        if not character_is_jumping and not "s" in k:
            characterFrameCounter += 1
            if characterFrameCounter == characterSpeed:
                characters[characterIndex].undraw()
                characterIndex += 1
                if characterIndex == 4:
                    characterIndex = 0
                characters[characterIndex].draw(win)
                characterFrameCounter = 1
            
        # When the user presses "s", the character ducks
        if not character_is_jumping and not character_is_ducking and "s" in k:
            characters[characterIndex].undraw()
            characters[5].draw(win)
            character_is_ducking = True

        elif character_is_ducking and "s" in k:
            character_is_ducking = True     
            
        elif character_is_ducking and not "s" in k:
            characters[5].undraw()
            characters[characterIndex].undraw()
            characters[characterIndex].draw(win)
            character_is_ducking = False
        
                
        # Ice Creams Moving
        if obs_drawn == 1 or obs_drawn == 2 or obs_drawn == 3:
            ice_creams[ice_creams_index].move(obs_speed, 0)
            if ice_creams[ice_creams_index].getAnchor().getX() <= -174:
                ice_creams[ice_creams_index].move(806 - ice_creams[ice_creams_index].getAnchor().getX(), 0)
                ice_creams[ice_creams_index].undraw()
                ice_creams_index = randint(0, 3)
                ice_creams[ice_creams_index].draw(win)
                obs_drawn = randint(1, 7)
            
        # Coin Moving
        elif obs_drawn == 4:
            coin.move(obs_speed, 0)
            if coin.getAnchor().getX() <= -174:
                coin.move(806 - coin.getAnchor().getX(), 0)
                obs_drawn = randint(1, 7)

        # Flying Pig Moving
        elif obs_drawn == 5 or obs_drawn == 6 or obs_drawn == 7:
            pigs[pigsIndex].move(obs_speed, 0)
            if pigs[pigsIndex].getAnchor().getX() <= -174:
                pigs[pigsIndex].move(806 - pigs[pigsIndex].getAnchor().getX(), 0)
                pigs[pigsIndex].undraw()
                pigsIndex = randint(0, 3)
                pigs[pigsIndex].draw(win)
                obs_drawn = randint(1, 7)
        
                     
        # Developer Key: If the user presses "4", they are directed to the
        # bonus life screen
        if "4" in k:
            gs3.undraw()
            cloud1.undraw()
            cloud2.undraw()
            sky.undraw()
            characters[characterIndex].undraw() 
            ice_creams[ice_creams_index].undraw()
            pigs[pigsIndex].undraw()
            coin.undraw()
            gs4.draw(win)
            gamestate = 4

        # Collision Detection For unicorn
        if char_select == 1:
            if character_is_jumping:
                if not(characters[4].getAnchor().getX() + 50 < ice_creams[ice_creams_index].getAnchor().getX() - 20 or
                        characters[4].getAnchor().getX() - 50 > ice_creams[ice_creams_index].getAnchor().getX() + 20 or
                        characters[4].getAnchor().getY() + 38 < 228):
                    # Go to game over screen
                    if numBonus == 0:
                        character_is_colliding = 1
                    # Use a bonus life
                    elif numBonus > 0:
                        character_is_colliding = 2
                        numBonustxt.undraw()
                        numBonustxt.setText(numBonus - 1)
                        numBonustxt.draw(win)
                            
                # Collision with flying pig
                if not(characters[4].getAnchor().getX() + 50 < pigs[pigsIndex].getAnchor().getX() - 40 or
                        characters[4].getAnchor().getX() - 50 > pigs[pigsIndex].getAnchor().getX() + 40 or
                        characters[4].getAnchor().getY() + 38 < pigs[pigsIndex].getAnchor().getY() - 32 or
                        characters[4].getAnchor().getY() - 38 > pigs[pigsIndex].getAnchor().getY() + 32):
                    # Go to the game over screen
                    if numBonus == 0:
                        character_is_colliding = 1
                    # Use a bonus life
                    elif numBonus > 0:
                        character_is_colliding = 2
                        numBonustxt.undraw()
                        numBonustxt.setText(numBonus - 1)
                        numBonustxt.draw(win)
                    
                # Collision with coin: go to the bonus life screen            
                elif not(characters[4].getAnchor().getX() + 50 < coin.getAnchor().getX() - 15 or
                            characters[4].getAnchor().getX() - 50 > coin.getAnchor().getX() + 15 or
                            characters[4].getAnchor().getY() + 38 < coin.getAnchor().getY() - 15 or
                            characters[4].getAnchor().getY() - 38 > coin.getAnchor().getY() + 15):
                    character_is_jumping = False
                    gs3.undraw()
                    cloud1.undraw()
                    cloud2.undraw()
                    sky.undraw()
                    characters[4].move(0, 280 - characters[4].getAnchor().getY())
                    characters[4].undraw()
                    character_jumping_speed = -63
                    characters[characterIndex].undraw()
                    ice_creams[ice_creams_index].undraw()
                    pigs[pigsIndex].undraw()
                    numBonus += 1
                    numBonustxt.undraw()
                    numBonustxt.setText(numBonus)
                    coin.undraw()
                    frame_counter = 0
                    gs4.draw(win)
                    gamestate = 4

            elif character_is_ducking:
                if not(characters[5].getAnchor().getX() + 46 < ice_creams[ice_creams_index].getAnchor().getX() - 20 or
                       characters[5].getAnchor().getX() - 46 > ice_creams[ice_creams_index].getAnchor().getX() + 20 or
                       characters[5].getAnchor().getY() + 30 < 228):
                    # Go to game over screen
                    if numBonus == 0:
                        character_is_colliding = 1
                    # Use a bonus life
                    elif numBonus > 0:
                        character_is_colliding = 2
                        numBonustxt.undraw()
                        numBonustxt.setText(numBonus - 1)
                        numBonustxt.draw(win)
                            
                # Collision with flying pig
                if not(characters[5].getAnchor().getX() + 46 < pigs[pigsIndex].getAnchor().getX() - 40 or
                       characters[5].getAnchor().getX() - 46 > pigs[pigsIndex].getAnchor().getX() + 40 or
                       characters[5].getAnchor().getY() + 30 < pigs[pigsIndex].getAnchor().getY() - 32 or
                       characters[5].getAnchor().getY() - 30 > pigs[pigsIndex].getAnchor().getY() + 32):
                    # Go to the game over screen
                    if numBonus == 0:
                        character_is_colliding = 1
                    # Use a bonus life
                    elif numBonus > 0:
                        character_is_colliding = 2
                        numBonustxt.undraw()
                        numBonustxt.setText(numBonus - 1)
                        numBonustxt.draw(win)
                    
                # Collision with coin: go to the bonus life screen            
                elif not(characters[5].getAnchor().getX() + 46 < coin.getAnchor().getX() - 15 or
                         characters[5].getAnchor().getX() - 46 > coin.getAnchor().getX() + 15 or
                         characters[5].getAnchor().getY() + 30 < coin.getAnchor().getY() - 15 or
                         characters[5].getAnchor().getY() - 30 > coin.getAnchor().getY() + 15):
                    character_is_ducking = False
                    gs3.undraw()
                    cloud1.undraw()
                    cloud2.undraw()
                    sky.undraw()
                    characters[5].undraw()
                    characters[4].undraw()
                    characters[characterIndex].undraw()
                    ice_creams[ice_creams_index].undraw()
                    pigs[pigsIndex].undraw()
                    numBonus += 1
                    numBonustxt.undraw()
                    numBonustxt.setText(numBonus)
                    coin.undraw()
                    frame_counter = 0
                    gs4.draw(win)
                    gamestate = 4
                
            else:
                # Collision with Ice cream cones
                if not(characters[characterIndex].getAnchor().getX() + 50 < ice_creams[ice_creams_index].getAnchor().getX() - 20 or
                        characters[characterIndex].getAnchor().getX() - 50 > ice_creams[ice_creams_index].getAnchor().getX() + 20 or
                        characters[characterIndex].getAnchor().getY() + 38 < 228):
                    # Go to game over screen
                    if numBonus == 0:
                        character_is_colliding = 1
                    # Use a bonus life
                    elif numBonus > 0:
                        character_is_colliding = 2
                        numBonustxt.undraw()
                        numBonustxt.setText(numBonus - 1)
                        numBonustxt.draw(win)

                # Collision with flying pigs                                
                if not(characters[characterIndex].getAnchor().getX() + 50 < pigs[pigsIndex].getAnchor().getX() - 40 or
                        characters[characterIndex].getAnchor().getX() - 50 > pigs[pigsIndex].getAnchor().getX() + 40 or
                        characters[characterIndex].getAnchor().getY() + 38 < pigs[pigsIndex].getAnchor().getY() - 32 or
                        characters[characterIndex].getAnchor().getY() - 38 > pigs[pigsIndex].getAnchor().getY() + 32):
                    # Go to the game over screen
                    if numBonus == 0:
                        character_is_colliding = 1
                    # Use a bonus life
                    elif numBonus > 0:
                        character_is_colliding = 2
                        numBonustxt.undraw()
                        numBonustxt.setText(numBonus - 1)
                        numBonustxt.draw(win)
                    
                # Collision with coin: go to the bonus life screen            
                elif not(characters[characterIndex].getAnchor().getX() + 50 < coin.getAnchor().getX() - 15 or
                            characters[characterIndex].getAnchor().getX() - 50 > coin.getAnchor().getX() + 15 or
                            characters[characterIndex].getAnchor().getY() + 38 < coin.getAnchor().getY() - 15 or
                            characters[characterIndex].getAnchor().getY() - 38 > coin.getAnchor().getY() + 15):
                    character_is_jumping = False
                    gs3.undraw()
                    cloud1.undraw()
                    cloud2.undraw()
                    sky.undraw()
                    characters[characterIndex].undraw()
                    ice_creams[ice_creams_index].undraw()
                    pigs[pigsIndex].undraw()
                    numBonus += 1
                    numBonustxt.undraw()
                    numBonustxt.setText(numBonus)
                    coin.undraw()
                    frame_counter = 0
                    gs4.draw(win)
                    gamestate = 4                    
    
        elif char_select == 2:
            if character_is_jumping:
                if not(characters[4].getAnchor().getX() + 26 < ice_creams[ice_creams_index].getAnchor().getX() - 20 or
                       characters[4].getAnchor().getX() - 26 > ice_creams[ice_creams_index].getAnchor().getX() + 20 or
                       characters[4].getAnchor().getY() + 56 < 228):
                    # Go to game over screen
                    if numBonus == 0:
                        character_is_colliding = 1
        
                    # Use a bonus life
                    elif numBonus > 0:
                        character_is_colliding = 2
                        numBonustxt.undraw()
                        numBonustxt.setText(numBonus - 1)
                        numBonustxt.draw(win)
                            
                # Collision with flying pig
                if not(characters[4].getAnchor().getX() + 26 < pigs[pigsIndex].getAnchor().getX() - 40 or
                       characters[4].getAnchor().getX() - 26 > pigs[pigsIndex].getAnchor().getX() + 40 or
                       characters[4].getAnchor().getY() + 56 < pigs[pigsIndex].getAnchor().getY() - 32 or
                       characters[4].getAnchor().getY() - 56 > pigs[pigsIndex].getAnchor().getY() + 32):
                    # Go to the game over screen
                    if numBonus == 0:
                        character_is_colliding = 1
                            
                    # Use a bonus life
                    elif numBonus > 0:
                        character_is_colliding = 2
                        numBonustxt.undraw()
                        numBonustxt.setText(numBonus - 1)
                        numBonustxt.draw(win)
                    
                # Collision with coin: go to the bonus life screen            
                elif not(characters[4].getAnchor().getX() + 26 < coin.getAnchor().getX() - 15 or
                         characters[4].getAnchor().getX() - 26 > coin.getAnchor().getX() + 15 or
                         characters[4].getAnchor().getY() + 56 < coin.getAnchor().getY() - 15 or
                         characters[4].getAnchor().getY() - 56 > coin.getAnchor().getY() + 15):
                    character_is_jumping = False
                    gs3.undraw()
                    cloud1.undraw()
                    cloud2.undraw()
                    sky.undraw()
                    characters[4].move(0, 260 - characters[4].getAnchor().getY())
                    character_jumping_speed = -63
                    characters[4].undraw()
                    characters[characterIndex].undraw()
                    ice_creams[ice_creams_index].undraw()
                    pigs[pigsIndex].undraw()
                    numBonus += 1
                    numBonustxt.undraw()
                    numBonustxt.setText(numBonus)
                    coin.undraw()
                    frame_counter = 0
                    gs4.draw(win)
                    gamestate = 4

            elif character_is_ducking:
                if not(characters[5].getAnchor().getX() + 53 < ice_creams[ice_creams_index].getAnchor().getX() - 20 or
                       characters[5].getAnchor().getX() - 53 > ice_creams[ice_creams_index].getAnchor().getX() + 20 or
                       characters[5].getAnchor().getY() + 30 < 228):
                    # Go to game over screen
                    if numBonus == 0:
                        character_is_colliding = 1
                    # Use a bonus life
                    elif numBonus > 0:
                        character_is_colliding = 2
                        numBonustxt.undraw()
                        numBonustxt.setText(numBonus - 1)
                        numBonustxt.draw(win)
                            
                # Collision with flying pig
                if not(characters[5].getAnchor().getX() + 53 < pigs[pigsIndex].getAnchor().getX() - 40 or
                       characters[5].getAnchor().getX() - 53 > pigs[pigsIndex].getAnchor().getX() + 40 or
                       characters[5].getAnchor().getY() + 30 < pigs[pigsIndex].getAnchor().getY() - 32 or
                       characters[5].getAnchor().getY() - 30 > pigs[pigsIndex].getAnchor().getY() + 32):
                    # Go to the game over screen
                    if numBonus == 0:
                        character_is_colliding = 1
                    # Use a bonus life
                    elif numBonus > 0:
                        character_is_colliding = 2
                        numBonustxt.undraw()
                        numBonustxt.setText(numBonus - 1)
                        numBonustxt.draw(win)
                    
                # Collision with coin: go to the bonus life screen            
                elif not(characters[5].getAnchor().getX() + 53 < coin.getAnchor().getX() - 15 or
                         characters[5].getAnchor().getX() - 53 > coin.getAnchor().getX() + 15 or
                         characters[5].getAnchor().getY() + 30 < coin.getAnchor().getY() - 15 or
                         characters[5].getAnchor().getY() - 30 > coin.getAnchor().getY() + 15):
                    character_is_ducking = False
                    gs3.undraw()
                    cloud1.undraw()
                    cloud2.undraw()
                    sky.undraw()
                    characters[5].undraw()
                    characters[4].undraw()
                    characters[characterIndex].undraw()
                    ice_creams[ice_creams_index].undraw()
                    pigs[pigsIndex].undraw()
                    numBonus += 1
                    numBonustxt.undraw()
                    numBonustxt.setText(numBonus)
                    coin.undraw()
                    frame_counter = 0
                    gs4.draw(win)
                    gamestate = 4
                        
            else:
                # Collision with Ice cream cones
                if not(characters[characterIndex].getAnchor().getX() + 26 < ice_creams[ice_creams_index].getAnchor().getX() - 20 or
                       characters[characterIndex].getAnchor().getX() - 26 > ice_creams[ice_creams_index].getAnchor().getX() + 20 or
                       characters[characterIndex].getAnchor().getY() + 56 < 228):
                    # Go to game over screen
                    if numBonus == 0:
                        character_is_colliding = 1
                    # Use a bonus life
                    elif numBonus > 0:
                        character_is_colliding = 2
                        numBonustxt.undraw()
                        numBonustxt.setText(numBonus - 1)
                        numBonustxt.draw(win)

                # Collision with flying pigs                                
                if not(characters[characterIndex].getAnchor().getX() + 26 < pigs[pigsIndex].getAnchor().getX() - 40 or
                       characters[characterIndex].getAnchor().getX() - 26 > pigs[pigsIndex].getAnchor().getX() + 40 or
                       characters[characterIndex].getAnchor().getY() + 56 < pigs[pigsIndex].getAnchor().getY() - 32 or
                       characters[characterIndex].getAnchor().getY() - 56 > pigs[pigsIndex].getAnchor().getY() + 32):
                    # Go to the game over screen
                    if numBonus == 0:
                        character_is_colliding = 1
                    # Use a bonus life
                    elif numBonus > 0:
                        character_is_colliding = 2
                        numBonustxt.undraw()
                        numBonustxt.setText(numBonus - 1)
                        numBonustxt.draw(win)
                    
                # Collision with coin: go to the bonus life screen            
                elif not(characters[characterIndex].getAnchor().getX() + 26 < coin.getAnchor().getX() - 15 or
                         characters[characterIndex].getAnchor().getX() - 26 > coin.getAnchor().getX() + 15 or
                         characters[characterIndex].getAnchor().getY() + 56 < coin.getAnchor().getY() - 15 or
                         characters[characterIndex].getAnchor().getY() - 56 > coin.getAnchor().getY() + 15):
                    character_is_jumping = False
                    gs3.undraw()
                    cloud1.undraw()
                    cloud2.undraw()
                    sky.undraw()
                    characters[characterIndex].undraw()
                    ice_creams[ice_creams_index].undraw()
                    pigs[pigsIndex].undraw()
                    numBonus += 1
                    numBonustxt.undraw()
                    numBonustxt.setText(numBonus)
                    coin.undraw()
                    frame_counter = 0
                    gs4.draw(win)
                    gamestate = 4
    
        if character_is_colliding == 1:
            if character_is_jumping:
                if score < highscore:
                    gs3.undraw()
                    cloud1.undraw()
                    cloud2.undraw()
                    sky.undraw()
                    characters[characterIndex].undraw()
                    characters[4].move(0, 260 - characters[4].getAnchor().getY())
                    character_jumping_speed = -63
                    characters[4].undraw()
                    character_is_jumping = False
                    ice_creams[ice_creams_index].move(806 - ice_creams[ice_creams_index].getAnchor().getX(), 0)
                    ice_creams[ice_creams_index].undraw()
                    coin.move(806 - coin.getAnchor().getX(), 0)
                    coin.undraw()
                    pigs[pigsIndex].move(806 - pigs[pigsIndex].getAnchor().getX(), 0)
                    pigs[pigsIndex].undraw()
                    scoretxt2.undraw()
                    numBonustxt.undraw()
                    obs_speed = -20
                    cloud_speed = -5
                    frame_counter = 0
                    numBonus = 0
                    headIndex = 2
                    mouthIndex = 2
                    gs5.draw(win)
                    heads[headIndex].draw(win)
                    mouths[mouthIndex].draw(win)
                    scoretxt.setText(score)
                    scoretxt.draw(win)
                    highscoretxt.draw(win)
                    gamestate = 5
                    
                # Go to the highscore screen
                elif score > highscore:
                    gs3.undraw()
                    cloud1.undraw()
                    cloud2.undraw()
                    sky.undraw()
                    characters[characterIndex].undraw()
                    characters[4].move(0, 260 - characters[4].getAnchor().getY())
                    character_jumping_speed = -63
                    characters[4].undraw()
                    character_is_jumping = False
                    ice_creams[ice_creams_index].move(806 - ice_creams[ice_creams_index].getAnchor().getX(), 0)
                    ice_creams[ice_creams_index].undraw()
                    coin.move(806 - coin.getAnchor().getX(), 0)
                    coin.undraw()
                    pigs[pigsIndex].move(806 - pigs[pigsIndex].getAnchor().getX(), 0)
                    pigs[pigsIndex].undraw()
                    scoretxt2.undraw()
                    numBonustxt.undraw()
                    obs_speed = -20
                    cloud_speed = -5
                    frame_counter = 0
                    numBonus = 0
                    headIndex = 4
                    mouthIndex = 4
                    gs6.draw(win)
                    heads[headIndex].draw(win)
                    mouths[mouthIndex].draw(win)
                    highscore = score
                    highscoretxt.setText(highscore)
                    highscoretxt.draw(win)
                    gamestate = 6
                            
            elif character_is_ducking:
                if score < highscore:
                    characters[characterIndex].undraw()
                    characters[5].undraw()
                    gs3.undraw()
                    cloud1.undraw()
                    cloud2.undraw()
                    sky.undraw()
                    ice_creams[ice_creams_index].move(806 - ice_creams[ice_creams_index].getAnchor().getX(), 0)
                    ice_creams[ice_creams_index].undraw()
                    coin.move(806 - coin.getAnchor().getX(), 0)
                    coin.undraw()
                    pigs[pigsIndex].move(806 - pigs[pigsIndex].getAnchor().getX(), 0)
                    pigs[pigsIndex].undraw()
                    scoretxt2.undraw()
                    numBonustxt.undraw()
                    obs_speed = -20
                    cloud_speed = -5
                    frame_counter = 0
                    numBonus = 0
                    headIndex = 2
                    mouthIndex = 2
                    gs5.draw(win)
                    heads[headIndex].draw(win)
                    mouths[mouthIndex].draw(win)
                    scoretxt.setText(score)
                    scoretxt.draw(win)
                    highscoretxt.draw(win)
                    gamestate = 5
                        
                # Go to the highscore screen
                elif score > highscore:
                    characters[characterIndex].undraw()
                    characters[5].undraw()
                    gs3.undraw()
                    cloud1.undraw()
                    cloud2.undraw()
                    sky.undraw()
                    ice_creams[ice_creams_index].move(806 - ice_creams[ice_creams_index].getAnchor().getX(), 0)
                    ice_creams[ice_creams_index].undraw()
                    coin.move(806 - coin.getAnchor().getX(), 0)
                    coin.undraw()
                    pigs[pigsIndex].move(806 - pigs[pigsIndex].getAnchor().getX(), 0)
                    pigs[pigsIndex].undraw()
                    scoretxt2.undraw()
                    numBonustxt.undraw()
                    obs_speed = -20
                    cloud_speed = -5
                    frame_counter = 0
                    numBonus = 0
                    headIndex = 4
                    mouthIndex = 4
                    gs6.draw(win)
                    heads[headIndex].draw(win)
                    mouths[mouthIndex].draw(win)
                    highscore = score
                    highscoretxt.setText(highscore)
                    highscoretxt.draw(win)
                    gamestate = 6
            else:
                if score < highscore:
                    characters[characterIndex].undraw()
                    characters[4].undraw()
                    gs3.undraw()
                    cloud1.undraw()
                    cloud2.undraw()
                    sky.undraw()
                    ice_creams[ice_creams_index].move(806 - ice_creams[ice_creams_index].getAnchor().getX(), 0)
                    ice_creams[ice_creams_index].undraw()
                    coin.move(806 - coin.getAnchor().getX(), 0)
                    coin.undraw()
                    pigs[pigsIndex].move(806 - pigs[pigsIndex].getAnchor().getX(), 0)
                    pigs[pigsIndex].undraw()
                    scoretxt2.undraw()
                    numBonustxt.undraw()
                    obs_speed = -20
                    cloud_speed = -5
                    frame_counter = 0
                    numBonus = 0
                    headIndex = 2
                    mouthIndex = 2
                    gs5.draw(win)
                    heads[headIndex].draw(win)
                    mouths[mouthIndex].draw(win)
                    scoretxt.setText(score)
                    scoretxt.draw(win)
                    highscoretxt.draw(win)
                    gamestate = 5
                        
                # Go to the highscore screen
                elif score > highscore:
                    characters[characterIndex].undraw()
                    characters[4].undraw()
                    gs3.undraw()
                    cloud1.undraw()
                    cloud2.undraw()
                    sky.undraw()
                    ice_creams[ice_creams_index].move(806 - ice_creams[ice_creams_index].getAnchor().getX(), 0)
                    ice_creams[ice_creams_index].undraw()
                    coin.move(806 - coin.getAnchor().getX(), 0)
                    coin.undraw()
                    pigs[pigsIndex].move(806 - pigs[pigsIndex].getAnchor().getX(), 0)
                    pigs[pigsIndex].undraw()
                    scoretxt2.undraw()
                    numBonustxt.undraw()
                    obs_speed = -20
                    cloud_speed = -5
                    frame_counter = 0
                    numBonus = 0
                    headIndex = 4
                    mouthIndex = 4
                    gs6.draw(win)
                    heads[headIndex].draw(win)
                    mouths[mouthIndex].draw(win)
                    highscore = score
                    highscoretxt.setText(highscore)
                    highscoretxt.draw(win)
                    gamestate = 6                    
            character_is_colliding = 0

        elif character_is_colliding == 2:
            # Subtract one from the number of bonus lives when the character isn't touching the obstacles anymore
            # For ice cream cones
            if obs_drawn == 1 or obs_drawn == 2 or obs_drawn == 3:
                if character_is_jumping:
                    if characters[4].getAnchor().getX() - 50 > ice_creams[ice_creams_index].getAnchor().getX() + 20:
                        character_is_colliding = 0
                        numBonus -= 1

                elif character_is_ducking:
                    if characters[5].getAnchor().getX() - 46 > ice_creams[ice_creams_index].getAnchor().getX() + 20:
                        character_is_colliding = 0
                        numBonus -= 1
                        
                else:
                    if characters[characterIndex].getAnchor().getX() - 50 > ice_creams[ice_creams_index].getAnchor().getX() + 20:
                        character_is_colliding = 0
                        numBonus -= 1

                
                     
            # For flying pigs
            if obs_drawn == 5 or obs_drawn == 6 or obs_drawn == 7:
                if character_is_jumping:
                    if pigsIndex == 0 or pigsIndex == 1:
                        if characters[4].getAnchor().getY() - 38 > pigs[pigsIndex].getAnchor().getY() + 32:
                            character_is_colliding = 0
                            numBonus -= 1
                       
                    elif pigsIndex == 2 or pigsIndex == 3:
                        if characters[4].getAnchor().getX() - 50 > pigs[pigsIndex].getAnchor().getX() + 40:
                            character_is_colliding = 0
                            numBonus -= 1

                elif character_is_ducking:
                    if pigsIndex == 0 or pigsIndex == 1:
                        if characters[4].getAnchor().getY() - 30 > pigs[pigsIndex].getAnchor().getY() + 32:
                            character_is_colliding = 0
                            numBonus -= 1
                       
                    elif pigsIndex == 2 or pigsIndex == 3:
                        if characters[4].getAnchor().getX() - 46 > pigs[pigsIndex].getAnchor().getX() + 40:
                            character_is_colliding = 0
                            numBonus -= 1
                          
                else:
                    if pigsIndex == 0 or pigsIndex == 1:
                        if characters[characterIndex].getAnchor().getY() - 38 > pigs[pigsIndex].getAnchor().getY() + 32:
                            character_is_colliding = 0
                            numBonus -= 1
                         
                    elif pigsIndex == 2 or pigsIndex == 3:
                        if characters[characterIndex].getAnchor().getX() - 50 > pigs[pigsIndex].getAnchor().getX() + 40:
                            character_is_colliding = 0
                            numBonus -= 1
                                                 
        # Developer Key: If the user presses "5", they are directed to the game
        # over screen.
        if "5" in k:
            if character_is_jumping == True:
                characters[4].undraw()
                character_is_jumping = False
            else:
                characters[characterIndex].undraw()
            gs3.undraw()
            cloud1.undraw()
            cloud2.undraw()
            sky.undraw()
            ice_creams[ice_creams_index].move(806 - ice_creams[ice_creams_index].getAnchor().getX(), 0)
            ice_creams[ice_creams_index].undraw()
            coin.move(806 - coin.getAnchor().getX(), 0)
            coin.undraw()
            pigs[pigsIndex].move(806 - pigs[pigsIndex].getAnchor().getX(), 0)
            pigs[pigsIndex].undraw()
            scoretxt2.undraw()
            numBonustxt.undraw()
            obs_speed = -20
            cloud_speed = -5
            frame_counter = 0
            headIndex = 2
            mouthIndex = 2
            gs5.draw(win)
            scoretxt.setText(score)
            heads[headIndex].draw(win)
            mouths[mouthIndex].draw(win)
            scoretxt.draw(win)
            highscoretxt.draw(win)
            gamestate = 5
            
        # Developer Key: If the user presses "6", they are directed to the
        # highscore screen.
        # If the user's score is higher than their highscore, they are directed
        # to the highscore screen.
        if "6" in k:
            if character_is_jumping == True:
                characters[4].undraw()
                character_is_jumping = False
            else:
                characters[characterIndex].undraw()
            gs3.undraw()
            cloud1.undraw()
            cloud2.undraw()
            sky.undraw()
            ice_creams[ice_creams_index].move(806 - ice_creams[ice_creams_index].getAnchor().getX(), 0)
            ice_creams[ice_creams_index].undraw()
            coin.move(806 - coin.getAnchor().getX(), 0)
            coin.undraw()
            pigs[pigsIndex].move(806 - pigs[pigsIndex].getAnchor().getX(), 0)
            pigs[pigsIndex].undraw()
            scoretxt2.undraw()
            numBonustxt.undraw()
            obs_speed = -20
            cloud_speed = -5
            frame_counter = 0
            headIndex = 4
            mouthIndex = 4
            gs6.draw(win)
            heads[headIndex].draw(win)
            mouths[mouthIndex].draw(win)
            highscore = score
            highscoretxt.setText(highscore)
            highscoretxt.draw(win)
            gamestate = 6
            
    elif gamestate == 4:
        frame_counter += 1
        if frame_counter == 50:
            frame_counter = 0
            gs4.undraw()
            sky.draw(win)
            gs3.draw(win)
            cloud1.draw(win)
            cloud2.draw(win)
            characters[characterIndex].draw(win)
            ice_creams_index = randint(0, 2)
            ice_creams[ice_creams_index].draw(win)
            coin.draw(win)
            numBonustxt.draw(win)
            pigsIndex = randint(0, 3)
            pigs[pigsIndex].draw(win)
            gamestate = 3
            seconds = 0
            
    elif gamestate == 5:
        headFrameCounter += 1
        mouthFrameCounter += 1
        if headFrameCounter == 10 and mouthFrameCounter == 10:
            heads[headIndex].undraw()
            mouths[mouthIndex].undraw()
            headIndex += 1
            mouthIndex += 1
            if headIndex == 4 and mouthIndex == 4:
                headIndex = 2
                mouthIndex = 2
            heads[headIndex].draw(win)
            mouths[mouthIndex].draw(win)
            headFrameCounter = 1
            mouthFrameCounter = 1
            
        frame_counter += 1
        if frame_counter == 50:
            frame_counter = 0
            seconds += 1
            
        if seconds == 3:
            seconds = 0
            gs5.undraw()
            highscoretxt.undraw()
            scoretxt.undraw()
            score = 0
            heads[headIndex].undraw()
            mouths[mouthIndex].undraw()
            headIndex = 0
            mouthIndex = 0
            gs0.draw(win)
            heads[headIndex].draw(win)
            mouths[mouthIndex].draw(win)
            gamestate = 0
            char_select = 0
            
    elif gamestate == 6:
        headFrameCounter += 1
        mouthFrameCounter += 1
        if headFrameCounter == 10 and mouthFrameCounter == 10:
            heads[headIndex].undraw()
            mouths[mouthIndex].undraw()
            headIndex += 1
            mouthIndex += 1
            if headIndex == 6 and mouthIndex == 6:
                headIndex = 4
                mouthIndex = 4
            heads[headIndex].draw(win)
            mouths[mouthIndex].draw(win)
            headFrameCounter = 1
            mouthFrameCounter = 1
            
        frame_counter += 1
        if frame_counter == 50:
            frame_counter = 0
            seconds += 1
            
        if seconds == 3:
            seconds = 0
            gs6.undraw()
            heads[headIndex].undraw()
            mouths[mouthIndex].undraw()
            highscoretxt.undraw()
            score = 0
            headIndex = 0
            mouthIndex = 0
            gs0.draw(win)
            heads[headIndex].draw(win)
            mouths[mouthIndex].draw(win)
            gamestate = 0
            char_select = 0
