#! /usr/bin/env python

__author__="William S"

'''
It goes through each entity so a mob may not always show up.
Entities are registered to mc.entity only if they were there when you started the game (Restart the game to get the current entities registered).
Mobs created after you start the game will not show up.
'''

import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()

playerPosition = mc.player.getPos()

playerIds = mc.getPlayerEntityIds()
playerId = min(playerIds)
entityId = 0

print 'Player ID: ' + str(playerId)
mc.postToChat('Player ID: ' + str(playerId))

mc.postToChat("All entities will appear in your position in 10 secoonds.")
time.sleep(10)

while True: 
	try:
		entityId = entityId + 1
		if entityId < playerId:
			mc.entity.setPos(entityId, playerPosition.x, playerPosition.y, playerPosition.z)
		else:
			break

	except Exception:
		continue
