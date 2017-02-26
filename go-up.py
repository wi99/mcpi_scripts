#! /usr/bin/env python

import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()
if __name__ == '__main__':
	
	playerPosition = mc.player.getTilePos()
	playerPosition = minecraft.Vec3(int(playerPosition.x), int(playerPosition.y), int(playerPosition.z))
	
	mc.setBlock(playerPosition.x, playerPosition.y + 50, playerPosition.z, block.AIR)
	mc.player.setTilePos(playerPosition.x, playerPosition.y + 50, playerPosition.z)
	mc.postToChat('WHEEEEEEEE!!')
	mc.setBlock(playerPosition.x, playerPosition.y + 2, playerPosition.z, block.WATER_STATIONARY)
	time.sleep(2.5)
	mc.setBlock(playerPosition.x, playerPosition.y + 2, playerPosition.z, block.AIR)