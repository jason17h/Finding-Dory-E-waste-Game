from pygame import * # importing the pygame module
import random # importing random module
import math # importing math module

init() # initializing pygame module

SIZE = width, height = 1000, 800 # setting the size of the screen
screen = display.set_mode(SIZE) # variable for the screen

# setting the colours:
BLACK = (0, 0, 0)
SKYBLUE = (0, 204, 255)
TURQUOISE = (0, 220, 220)
WHITE = (255, 255, 255)
DARKBLUE = (0, 0, 66)

# setting the fonts:
myFont = font.SysFont("Broadway", 55) 
myFont2 = font.SysFont("Broadway", 100)
myFont3 = font.SysFont("Broadway", 40)
myFont4 = font.SysFont("verdana", 50)
myFont5 = font.SysFont("verdana", 80)

# setting variables related to the images used in the program
backgroundImg = image.load('ocean.jpg') # the image that will be used as the background
backgroundSize = backgroundImg.get_rect().size
userImg = image.load('Dory (1).png') # the sprite of the character
userSize = userImg.get_rect().size
userImg2 = image.load('backwards_dory.png') # the sprite of the character flipped
# the size of userImg2 should be the same as userImg 1
enemyImg = image.load('broken_computer.png') # the enemy
enemySize = enemyImg.get_rect().size
menuImg = image.load('wallpaper.jpg') # the background of the menu screen
##menuSize = menuImg.get_rect().size
logoImg = image.load('finding_dory_logo.png') # the logo/title of the game
logoSize = logoImg.get_rect().size
instructionsImg = [image.load('instructions1.jpg'), image.load('instructions2.jpg'), image.load('instructions3.jpg'), image.load('instructions4.jpg'), image.load('instructions5.jpg')] # there are 5 instructions screens: this is the list containing them
replayImg = image.load('replayBG.jpg')

#setting the soundtrack that will be playing in the background:
mixer.music.load("soundtrack.mp3")

# setting the constants for the list:
ENEMYX = USERX = 0 # The first spot in the list (where the x coordinate of the enemy/user will be)
ENEMYY = USERY = 1 # The second spot in the list (where the y coordinate of the enemy/user will be)
ENEMYSPEED = USERSPEED = 2 # The third spot in the list (where the speed/direction of the enemy/user will be)
USERSPRITE = 3 # The fourth spot of the user list (where the user image will be)

def mainMenu(button, mx, my, textStart, textInstructions, textQuit): # this is the function of the main menu
    
    screen.blit(menuImg, (-100, 0)) # drawing the background
    screen.blit(logoImg, ((width-logoSize[0])//2, 25)) # drawing the logo/title
        
    # drawing the boxes for each option the user can choose
    quitRect = Rect(200, 650, 600, 100) # quit box
    instructionsRect = Rect(200, 500, 600, 100) # instructions box
    startRect = Rect(200, 350, 600, 100)    # start box
    draw.rect(screen, WHITE, startRect, 10) # start box
    draw.rect(screen, WHITE, instructionsRect, 10) #instructions box
    draw.rect(screen, WHITE, quitRect, 10) # quit box

    # this will highlight the box and the text if the mouse is hovering over the box
    if startRect.collidepoint(mx, my) == True: # checks if the mouse (mx, my) is in the start box
        draw.rect(screen, DARKBLUE, startRect, 10) # redrawing the rectangle of the highlighted box
        textStart = myFont.render("START", 1, DARKBLUE) # rendering the highlighted version of "START" 
    elif instructionsRect.collidepoint(mx, my) == True: # checks if the mouse (mx, my) is in the instructions box
        draw.rect(screen, DARKBLUE, instructionsRect, 10) # redrawing the rectangle of the highlighted box
        textInstructions = myFont.render("INSTRUCTIONS", 1, DARKBLUE) # rendering the highlighted version of "INSTRUCTIONS"        
    elif quitRect.collidepoint(mx, my) == True: # checks if the mouse (mx, my) is in the quit box
        draw.rect(screen, DARKBLUE, quitRect, 10)  # redrawing the rectangle of the highlighted box
        textQuit = myFont.render("QUIT", 1, DARKBLUE) # rendering  "QUIT"
    
    # drawing out all of the text on the main menu
    screen.blit(textStart, Rect((width - startSize[0])//2, 350 + (100 - startSize[1])//2, startSize[0], startSize[1])) # start button
    screen.blit(textInstructions, Rect((width - changeLvlSize[0])//2, 500 + (100 - changeLvlSize[1])//2, changeLvlSize[0], changeLvlSize[1])) # level change button
    screen.blit(textQuit, Rect((width - quitSize[0])//2, 650 + (100 - quitSize[1])//2, quitSize[0], quitSize[1])) # quit button
    

    if button == 1: # if mouse was left clicked 
        if quitRect.collidepoint(mx, my):
            return "QUIT" # quit box: menu state becomes "QUIT"
        elif instructionsRect.collidepoint(mx, my):
            return "INSTRUCTIONS" # level change box: menu state becomes "LVLCHANGE"
        elif startRect.collidepoint(mx, my):
            time.wait(100)
            return "START" # star box: menu state becomes "START"
            
    display.flip() # update screen
    
    return "MAINMENU" # if no boxes are selected, "MAINMENU" is returned

def instructions(mx, my, screenNum): # function for the instructions screen
    
    screen.blit(instructionsImg[screenNum - 1], (0, 0)) # drawing the background
    
    display.flip()  # update screen
    
    if button == 1: # if the mouse is clicked anywhere on the screen, the game will return to the main menu
        screenNum += 1 # there are a total of 5 instructions screens: every click will advance to the next screen
    
    if screenNum > 5: # once the user is past the final screen, the screenNum will be reset to 1 and the user will return to the main menu
        screenNum = 1
        return "MAINMENU", screenNum
    
    return "INSTRUCTIONS", screenNum # if the user does not do anything, the instructions screen will stay




def initEnemy(enemies): # module that will initialize each enemy at a certain position on the screen
    #enemies = 10*level    # sets the amount of enemies there will be
    enemyX = [] # represents the x coordinate of the ball
    enemyY = [] # represents the y coordinate of the ball
    enemySpeed = [] # represents the speed/direction of the ball 
    enemySpeedRange = 3
    
    for i in range(enemies): # runs 10 times (10 easy enemies)
        enemyX.append(200*i + 300) # separates the enemies horizontally 100 units
        enemyY.append(random.randint(0, 800 - enemySize[1])) # sets the enemy at a random vertical position
        enemySpeed.append(random.randint(-1 * enemySpeedRange, enemySpeedRange)) # sets the speed/directino of the enemy (corresponding to its level)
        if enemySpeed[i] == 0: # we don't want any still enemies, so if enemySpeed == 0, it will automatically switch to the level of the game
            enemySpeed[i] = enemySpeedRange
    
    enemyData = [enemyX, enemyY, enemySpeed] # setting the data of the enemy
    return enemyData, enemySpeedRange # returning the data to be used throughout the program

def initUser(): # initializes the position of the user
    userX = 100 # initializes the user's x coordinate at 100
    userY = 400 # initializes the user's y coordinate at 400
    userSpeed = 1 # the user's speed is set to 1
    userSprite = userImg
    userData = [userX, userY, userSpeed, userSprite] # setting the user data
    return userData # returning the user data

def gamePlay(enemyData, userData, enemies, enemySpeedRange, back): # function for the actual game part of the game
        
    screen.blit(backgroundImg, (backgroundX, backgroundY)) # painting the background of the game (the ocean) 
    screen.blit(backgroundImg, (backgroundX2, backgroundY)) # painting the background again (so the image "repaints" itself after the original image runs out
    screen.blit(backgroundImg, (backgroundX3, backgroundY)) # painting the background again (so the image "repaints" itself after the original image runs out
    screen.blit(userData[USERSPRITE], (userData[USERX], userData[USERY])) # painting the user
    backbutton = Rect(10, 10, 170, 70) # setting the rectangle for the back button
    draw.rect(screen, WHITE, backbutton) # drawing the back button
    pointsText = "Points: " + str(points) # setting the text for the number of points
    pointsRender = myFont.render(pointsText, True, WHITE) # rendering the text for the number of points
    size = myFont.size(pointsText)    #getting the size of the text
    screen.blit(pointsRender, Rect(width - size[0] - 10, 0, size[0], size[1])) # drawing the text    
    
    # data for the back button:
    backSize = myFont3.size("BACK")
    backText = myFont3.render("BACK", 1, DARKBLUE)    
    
    # loop that checks if a new enemy must be generated:
    if enemyData[ENEMYX][enemies - 1] + enemySize[0] <= width:
        enemies += 1  #increases enemies by 1
        enemyData[ENEMYX].append(200*(4) + 300) # separates the enemies horizontally
        enemyData[ENEMYY].append(random.randint(0, 800 - enemySize[1])) # sets the enemy at a random vertical position
        enemyData[ENEMYSPEED].append(random.randint(-1 * enemySpeedRange, enemySpeedRange)) # sets the speed/direction of the enemy
        if enemyData[ENEMYSPEED][enemies - 1] == 0: # we don't want any still enemies, so if enemySpeed == 0, it will automatically switch to the speed range
            enemyData[ENEMYSPEED][enemies - 1] = enemySpeedRange       
        
    for i in range(enemies): # loop that draws the enemies
        if enemyData[ENEMYX][i] > -1 * enemySize[0] and enemyData[ENEMYX][i] < width + enemySize[0]: # ensures that only enemies that are on the screen are drawn
            screen.blit(enemyImg, (enemyData[ENEMYX][i], enemyData[ENEMYY][i])) # drawing enemies
        
    if backbutton.collidepoint(mx, my) == True: #if the mouse hovers over the back button, the colours will invert
        draw.rect(screen, DARKBLUE, backbutton)
        backText = myFont3.render("BACK", 1, WHITE)
        if button == 1: # if the button clicks, all of the data will be reset for the user and the enemy
            userData = initUser()
            enemyData, enemySpeedRange = initEnemy(enemies)

            return "MAINMENU", userData, enemyData, enemies, True # returning the necessary values
        
    screen.blit(backText, Rect(10 + (170 - backSize[0])//2, 10 + (70 - backSize[1])//2, backSize[0], backSize[1])) # drawing the back button/text
        
    display.flip() # updating screen
        
    return "START", userData, enemyData, enemies, False # returning the necessary data
    
    
def collisionCheck(enemyData, userData, backgroundX, backgroundX2, backgroundX3, points, enemies, back): # function to check if user/enemies have collided
    menuState = "START" # menustate is set to START by default
    for i in range(enemies): # loop to check the collision between all enemies
        distance = math.sqrt(((userData[USERX] + userSize[0]//2) - (enemyData[ENEMYX][i] + enemySize[0]//2))**2 + ((userData[USERY] + userSize[1]//2) - (enemyData[ENEMYY][i] + enemySize[1]//2))**2) # checking the distance between the two points (user and enemy)
        if distance < userSize[0]//2 + enemySize[1]//2: # if the distance is smaller than the sum of the radii, all of the data will be reset.
            userData = initUser() # resetting user
            backgroundX = 0 # resetting background
            backgroundX2 = backgroundSize[0] # resetting other background
            enemyData, enemySpeedRange = initEnemy(enemies) # resetting enemy data
            points = 0 # resetting points
            
            menuState = "REPLAY" # sets the menu state to REPLAY to show the replay screen
            
    if back == True: # if the back button has been pressed, the user will return to the main menu
        menuState = "MAINMENU"
    
    return userData, enemyData, backgroundX, backgroundX2, backgroundX3, points, menuState # returning all necessary data
    
    

def moveEnemy(enemyData, enemies): # function to move enemies
    for i in range(enemies): # loop to run through the amount of enemies
        if enemyData[ENEMYX][i] > -1 * enemySize[0] and enemyData[ENEMYX][i] < width + enemySize[0]: # ensures that only enemies that are on the screen are moved
            enemyData[ENEMYY][i] += enemyData[ENEMYSPEED][i] # moves the enemy
            if enemyData[ENEMYY][i] > height - enemySize[1] or enemyData[ENEMYY][i] < 0: 
                enemyData[ENEMYSPEED][i] *= -1 # makes the enemies bounce on the screen if they reach the top or the bottom
            
    return enemyData # returning the data

def moveUser(userData, enemyData, backgroundX, backgroundX2, backgroundX3, points, enemies, enemySpeedRange): # function to move the user
    if KEY_LEFT == True: # if the left key is pressed, user x coordinate will decrease by 3 and the sprite will become a reflected image of the original
        userData[USERX] -= 3
        userData[USERSPRITE] = userImg2
        if userData[USERX] < 0: # this will prevent the user from going off of the screen
            userData[USERX] = 0
    if KEY_UP == True: # if the up key is pressed, the y coordinate will decrease by 3.
        userData[USERY] -= 3
        if userData[USERY] < 0:
            userData[USERY] = 0 # this will prevent the user from going off of the screen
    if KEY_DOWN == True: # if the down key is pressed, the user will go down 3 units
        userData[USERY] += 3  
        if userData[USERY] + userSize[1] > height:
            userData[USERY] = height - userSize[1] # this will prevent the user from going off of the screen
        
    if KEY_RIGHT == True:   # if the right key is pressed, the user will move to the right
        userData[USERSPRITE] = userImg
        if userData[USERX] < 350: # if the user is behind 350 pixels, the sprite itself will move
            userData[USERX] += 3
        else: # if not, the background will move instead
            backgroundX -= 3
            backgroundX2 -= 3
            # the following lines will reset the location of backgroundX and backgroundX2 everytime they are needed again
            if backgroundX + backgroundSize[0] <= width + 3:
                backgroundX2 = backgroundX + backgroundSize[0]
            if backgroundX2 + backgroundSize[0] <= width + 3:
                backgroundX = backgroundX2 + backgroundSize[0]
            for i in range(enemies): # the enemies will move along with the background
                enemyData[ENEMYX][i] -= 3
    
                
    for j in range(points, enemies): # this will run the loop, starting at the last enemy that has been passed (points)
        if userData[USERX] + userSize[0]//2 >= enemyData[ENEMYX][j] + enemySize[0]//2: # this will add a point each time the user passes an enemy
            points += 1
            if points % 5 == 0 and enemySpeedRange <= 10: # 10 will be the maximum speed; the speed will increase every 5 points
                enemySpeedRange += 1 # this will increase the range of the speed
                
    return userData, enemyData, backgroundX, backgroundX2, backgroundX3, points, enemySpeedRange # returning all data

def replay(button, mx, my): # function to ask if the user would like to play again
    screen.blit(replayImg, (0, 0)) # drawing the background
    
    # rectangles to represent the yes and no boxes
    yesRect = Rect(100, 800 - 350, 205, 105)
    noRect = Rect(495 + 210, 800 - 350, 205, 105)
    
    if button == 1:
        if yesRect.collidepoint(mx, my): # if the button is pressed while the mx and my are in the yes box, the user will restart
            return "START"
        elif noRect.collidepoint(mx, my): # if the button is pressed while mx and my are in the no box, the user will go back to the menu
            return "MAINMENU"
    
    
    display.flip() # updating the screen

    return "REPLAY" #returning replay if no actions have been taken

running = True # this is to help the main loop run
enemies = 5 # sets the initial # of enemies to 5
myClock = time.Clock() # used to control the fps
enemySpeedRange = 3 # default enemy speed range of 3
enemyData, enemySpeedRange = initEnemy(enemies) # initializing the enemies
userData = initUser() # initializing the user
# setting the state of each arrow key
KEY_LEFT = False
KEY_RIGHT = False
KEY_UP = False
KEY_DOWN = False
# setting the initial background coordinates
backgroundX = 0
backgroundY = 0
backgroundX2 = backgroundSize[0] #2289
backgroundX3 = backgroundSize[0] + backgroundSize[0]

back = False # initializes the back button as not being pressed

points = 0 # initializes the # of points as 0

startSize = myFont.size("START") # getting the size of "START"
changeLvlSize = myFont.size("INSTRUCTIONS") # getting the size of "INSTRUCTIONS"
quitSize = myFont.size("QUIT") # getting the size of "QUIT"

screenNum = 1 # initializing the instructions screen

mx = my = 0 # sets mx and my as 0

menuState = "MAINMENU" # sets default menustate as main menu



mixer.music.play(-1, 0.0) # playing the music

while running: # main loop
    
    button = 0 # resets the button to being not clicked each time the loop runs

    # the following lines will initialize the font for the code; they must be declared each time the loop runs because they may change in the mainMenu function, so they must be reset back to normal at the beginning of each loop
    textStart = myFont.render("START", 1, WHITE) # rendering "START"
    textInstructions = myFont.render("INSTRUCTIONS", 1, WHITE) # rendering "INSTRUCTIONSCHANGE LEVEL"
    textQuit = myFont.render("QUIT", 1, WHITE) # rendering "QUIT"     


    for evnt in event.get(): # checks each event
        mx, my = mouse.get_pos() # getting the mouse position
        if evnt.type == QUIT: # quits program
            running = False # breaks the loop
        if evnt.type == MOUSEBUTTONDOWN: # if mouse is clicked, program will track the button
            button = evnt.button  
        if evnt.type == KEYDOWN:
            # changing the state of the keys depending on if they're pressed and held or not
            if evnt.key == K_LEFT: 
                KEY_LEFT = True
            if evnt.key == K_RIGHT:
                KEY_RIGHT = True
            if evnt.key == K_UP:
                KEY_UP = True
            if evnt.key == K_DOWN:
                KEY_DOWN = True        
        if evnt.type == KEYUP:
            if evnt.key == K_LEFT:
                KEY_LEFT = False
            if evnt.key == K_RIGHT:
                KEY_RIGHT = False
            if evnt.key == K_UP:
                KEY_UP = False
            if evnt.key == K_DOWN:
                KEY_DOWN = False
    
    # this is where the game really begins: depending on the current menu state, certain functions will run.            
    if menuState == "MAINMENU": 
        menuState = mainMenu(button, mx, my, textStart, textInstructions, textQuit)            
                
    elif menuState == "INSTRUCTIONS":
        menuState, screenNum = instructions(mx, my, screenNum)
    elif menuState == "QUIT":
        running = False
    elif menuState == "START":           
        menuState, userData, enemyData, enemies, back = gamePlay(enemyData, userData, enemies, enemySpeedRange, back)
        enemyData = moveEnemy(enemyData, enemies) 
        userData, enemyData, backgroundX, backgroundX2, backgroundX3, points, enemySpeedRange = moveUser(userData, enemyData, backgroundX, backgroundX2, backgroundX3, points, enemies, enemySpeedRange)
        userData, enemyData, backgroundX, backgroundX2, backgroundX3, points, menuState = collisionCheck(enemyData, userData, backgroundX, backgroundX2, backgroundX3, points, enemies, back)     
    elif menuState == "REPLAY":
        menuState = replay(button, mx, my)
  
    myClock.tick(60) # sets fps to 60


quit() # quits program