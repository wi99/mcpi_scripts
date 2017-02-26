#! /usr/bin/env python

import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()
if __name__ == '__main__':
	
	mc.postToChat('X,Y,Z')
	while (True):
		time.sleep(5)
		playerPosition = mc.player.getTilePos()
		playerPosition = minecraft.Vec3(int(playerPosition.x), int(playerPosition.y), int(playerPosition.z))
		mc.postToChat(playerPosition)

