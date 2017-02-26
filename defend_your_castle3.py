#!/usr/bin/env python
#https://www.youtube.com/watch?v=dfRcQHM9F4M

import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create('')

mc.player.setTilePos(20, 2, 10)

mc.postToChat('DEFEND YOUR CASTLE!')
time.sleep(2)
mc.postToChat('ATTACK IN...')
time.sleep(2)
mc.postToChat('3...')
time.sleep(1)
mc.postToChat('2...')
time.sleep(1)
mc.postToChat('1...')
time.sleep(1)
mc.postToChat('Begin')

working = True

while working == True:
	pos = mc.player.getTilePos()
	mc.setBlock(pos.x+10, pos.y+1, pos.z, block.STONE_SLAB)
	mc.setBlock(pos.x+10, pos.y+1, pos.z+1, block.AIR)
	mc.setBlock(pos.x+10, pos.y+1, pos.z-1, block.AIR)
	for z in range(7, 14):
		if mc.getBlock(30,3,z) == block.SAND.id or mc.getBlock(30,3,z) == block.GRAVEL.id:
			mc.postToChat('Game Over!')
			working = False
