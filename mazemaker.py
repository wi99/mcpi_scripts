#! /usr/bin/env python

"""
Minecraft Maze Generator
by Sean McManus - www.sean.co.uk

From the book Raspberry Pi Projects

For more great ideas for things to do with your Raspberry Pi, see:
* Raspberry Pi For Dummies
* Scratch Programming in Easy Steps

Download free chapters from both at www.sean.co.uk

"""

import random
import minecraft.minecraft as minecraft
import minecraft.block as block
mc = minecraft.Minecraft.create()

def realx(x):
    return MAZE_X+(x*2)-1

def realz(z):
    return MAZE_Z+(z*2)-1

def showMaker(x, z):
    mc.setBlock(realx(x), GROUND+1, realz(z), 41) # 41=gold

def hideMaker(x, z):
    mc.setBlock(realx(x), GROUND+1, realz(z), 0)         

def demolish(realx, realz):
    mc.setBlocks(realx, GROUND+1, realz, realx, HEIGHT+GROUND, realz, 0)

def testAllWalls(cellx, cellz):
    if mc.getBlock(realx(cellx)+1, GROUND+1, realz(cellz))==MAZE_MATERIAL and mc.getBlock(realx(cellx)-1, GROUND+1, realz(cellz))==MAZE_MATERIAL and mc.getBlock(realx(cellx), GROUND+1, realz(cellz)+1)==MAZE_MATERIAL and mc.getBlock(realx(cellx), GROUND+1, realz(cellz)-1)==MAZE_MATERIAL: 
        return True
    else:
        return False

mc.saveCheckpoint()
originalPos = mc.player.getPos()    
mc.setting("world_immutable", True)
mc.postToChat("Welcome to Minecraft Maze!")

# Configure your maze here
SIZE = 10 
HEIGHT = 3
MAZE_X = 0   
GROUND = 0
MAZE_Z = 0
MAZE_MATERIAL = block.STONE.id
GROUND_MATERIAL = block.GRASS.id
CEILING = True

mc.setBlocks(MAZE_X-10, GROUND, MAZE_Z-10, MAZE_X+(SIZE*2)+10, GROUND+150, MAZE_Z+(SIZE*2)+10, block.AIR)
mc.setBlocks(MAZE_X-10, GROUND, MAZE_Z-10, MAZE_X+(SIZE*2)+10, GROUND, MAZE_Z+(SIZE*2)+10, GROUND_MATERIAL) # lay the ground

mc.setBlock(MAZE_X, GROUND+HEIGHT+1, MAZE_Z, MAZE_MATERIAL) # origin marker

mc.player.setTilePos(MAZE_X+SIZE, GROUND+25, MAZE_Z+SIZE) # move player above middle of maze

mc.postToChat("Now building your maze...")


# build grid of walls
for line in range(0, (SIZE+1)*2, 2):
    mc.setBlocks(MAZE_X+line, GROUND+1, MAZE_Z, MAZE_X+line, GROUND+HEIGHT, MAZE_Z+(SIZE*2), MAZE_MATERIAL)
    mc.setBlocks(MAZE_X, GROUND+1, MAZE_Z+line, MAZE_X+(SIZE*2), GROUND+HEIGHT, MAZE_Z+line, MAZE_MATERIAL)

mc.postToChat("TIP: Fly above it and look down.")

# set up of variables for creating maze
numberOfCells = SIZE*SIZE
numberOfvisitedCells = 1 # 1 for the one we start in
cellsVisitedList = []

xposition = random.randint(1, SIZE)
zposition = random.randint(1, SIZE)
playerx = xposition
playerz = zposition
showMaker(xposition, zposition)
cellsVisitedList.append((xposition, zposition))

while numberOfvisitedCells<numberOfCells:
    possibleDirections=[]

    ## note that this approach automatically excludes positions outside the maze border because they don't have four walls.

    #test whether left cell has all walls
    if testAllWalls(xposition-1, zposition):
        possibleDirections.append("left")

    #test whether right cell has all walls
    if testAllWalls(xposition+1, zposition):
        possibleDirections.append("right")

    #test whether up cell has all walls
    if testAllWalls(xposition, zposition-1):
        possibleDirections.append("up")

    #test whether down cell has all walls
    if testAllWalls(xposition, zposition+1):
        possibleDirections.append("down")

    hideMaker(xposition, zposition)

    if len(possibleDirections)!=0:
        #if there are unvisited neighbour cells, pick a random direction to move in
        directionChosen=random.choice(possibleDirections)

        #knock down wall between cell in direction chosen
        if directionChosen=="left":
            demolish(realx(xposition)-1, realz(zposition))
            xposition -= 1

        if directionChosen=="right":
            demolish(realx(xposition)+1, realz(zposition))
            xposition += 1
            
        if directionChosen=="up":
            demolish(realx(xposition), realz(zposition)-1)
            zposition -= 1

        if directionChosen=="down":
            demolish(realx(xposition), realz(zposition)+1)
            zposition += 1

        numberOfvisitedCells += 1 # after the move, increase number of visited cells
        cellsVisitedList.append((xposition, zposition)) # must go here otherwise gets trapped when tries to retrace
        showMaker(xposition, zposition)
        
    else: # do this when there are no unvisited neighbours
        retrace=cellsVisitedList.pop()
        xposition=retrace[0]
        zposition=retrace[1]
        showMaker(xposition, zposition)

if CEILING == True:
    mc.setBlocks(MAZE_X, GROUND+HEIGHT+1, MAZE_Z, MAZE_X+(SIZE*2), GROUND+HEIGHT+1, MAZE_Z+(SIZE*2), block.GLASS)
        
mc.postToChat("Your maze is ready!")
mc.postToChat("Happy exploring!")
mc.player.setTilePos(realx(playerx), GROUND+1, realz(playerz))

while True:
    x,y,z = mc.player.getTilePos()
    if mc.getBlock(x, y-1, z) == block.GOLD_BLOCK.id:
        mc.postToChat("Congrats! You found the hidden block!")
        mc.setting("world_immutable", False)
        mc.player.setPos(originalPos)
	mc.restoreCheckpoint()
        break
