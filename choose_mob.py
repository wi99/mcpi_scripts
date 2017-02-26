#! /usr/bin/env python

__author__ = 'William S'

'''
It goes through each entity so a mob may not always show up.
Entities are registered to mc.entity only if they were there when you started the game (Restart the game to get the current entities registered).
Mobs created after you start the game will not show up.
'''

import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()

playerPosition = mc.player.getTilePos()

mc.setBlocks(playerPosition.x - 1, playerPosition.y, playerPosition.z + 1, playerPosition.x + 1, playerPosition.y, playerPosition.z + 3, block.FENCE)
mc.setBlock(playerPosition.x, playerPosition.y, playerPosition.z + 2, block.AIR)

playerIds = mc.getPlayerEntityIds()
playerId = min(playerIds)
entityId = 0

mc.postToChat("Break the glass block to choose that mob")
mc.setBlock(playerPosition.x, playerPosition.y + 1, playerPosition.z + 1, block.GLASS)

while True: 
	try:
		entityId = entityId + 1
		if entityId < playerId:
			entityPosition = mc.entity.getPos(entityId)
			entityPosition = minecraft.Vec3(int(entityPosition.x), int(entityPosition.y), int(entityPosition.z))
			mc.postToChat('Mob ' + str(int(entityId)))
			mc.entity.setTilePos(entityId, playerPosition.x, playerPosition.y, playerPosition.z + 2)
			time.sleep(3)
			if mc.getBlock(playerPosition.x, playerPosition.y + 1, playerPosition.z + 1) == block.GLASS.id:
				mc.entity.setPos(entityId, entityPosition.x, entityPosition.y, entityPosition.z)
			else:
				break
		else:
			break

	except Exception:
		continue

if entityId < playerId:
	mc.postToChat('You chose mob ' + str(int(entityId)))

elif mc.getBlock(playerPosition.x, playerPosition.y + 1, playerPosition.z + 1) == block.GLASS.id:
	mc.postToChat("You did not choose a mob.")
	mc.setBlocks(playerPosition.x - 1, playerPosition.y, playerPosition.z + 1, playerPosition.x + 1, playerPosition.y + 2, playerPosition.z + 3, block.AIR)
