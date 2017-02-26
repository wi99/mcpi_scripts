#!/usr/bin/env python

import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
z = pos.z

mc.postToChat('Upwards Stream')

for y in xrange(pos.y, 60):
	#Wall
	mc.setBlocks(x + 2, y, z + 1, x, y, z - 1, block.COBBLESTONE)
	mc.setBlocks(x + 2, y, z, x, y, z, block.AIR)
	mc.setBlocks(x + 3, y + 1, z + 1, x, y + 1, z - 1, block.GLASS) #Plus 3 prevents water from destroying signs
	#Ceiling (To prevent gravel and sand from falling on the stream)
	mc.setBlocks(x, y + 2, z, x + 2, y + 2, z, block.GLASS)
	#Clear Pathway
	mc.setBlocks(x, y + 1, z, x + 2, y, z, block.AIR)
	#Stream
	mc.setBlock(x + 1, y, z, block.WATER_STATIONARY)
	mc.setBlock(x + 3, y, z, block.STAIRS_COBBLESTONE)
	mc.setBlock(x + 4, y, z, block.COBBLESTONE)
	mc.setBlock(x, y, z, 68)
	#Update variable and wait
	x = x + 2
	time.sleep(1)
	if mc.getBlock(x + 3, y, z) == block.BEDROCK_INVISIBLE.id:
		break

x = x - 2
mc.setBlocks(x + 3, y + 1, z, x + 4, y, z, block.AIR)
