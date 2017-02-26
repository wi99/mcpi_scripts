#! /usr/bin/env python

#https://arghbox.files.wordpress.com/2014/04/freeze_a5.pdf

import minecraft.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time
import minecraft.block as block

while True:
#	time.sleep(0.2)
	pos = mc.player.getPos()
	x = pos.x
	y = pos.y
	z = pos.z

	blockBelow = mc.getBlock(x, y - 1, z)

	water = block.WATER_STATIONARY.id #(9)
	ice = block.ICE.id

	if blockBelow == water:
		mc.setBlock(x, y - 1, z, ice)
