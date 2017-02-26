import minecraft.minecraft as minecraft
import minecraft.block as block
import random
import time

mc = minecraft.Minecraft.create()
mc.postToChat("Minecraft Whac-a-Block")

pos = mc.player.getTilePos()

mc.setBlocks(pos.x - 1, pos.y, pos.z + 3,
			 pos.x + 1, pos.y + 2, pos.z + 3,
			 block.STONE.id)

mc.postToChat("Get ready ...")
time.sleep(2)
mc.postToChat("Go")

blocksLit = 0
points = 0

while blocksLit < 9:
	time.sleep(0.2)
	blocksLit = blocksLit + 1
	lightCreated = False
	while not lightCreated:
		xPos = pos.x + random.randint(-1,1)
		yPos = pos.y + random.randint(0,2)
		zPos = pos.z + 3
		if mc.getBlock(xPos, yPos, zPos) == block.STONE.id:
			mc.setBlock(xPos, yPos, zPos, block.GLOWSTONE_BLOCK.id)
			lightCreated = True
	for hitBlock in mc.events.pollBlockHits():
		if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.GLOWSTONE_BLOCK.id:
			mc.setBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z, block.STONE.id)
			blocksLit = blocksLit - 1
			points = points + 1

mc.postToChat("Game Over - points = " + str(points))
