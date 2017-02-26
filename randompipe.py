#! /usr/bin/env python

import minecraft.minecraft as minecraft
import minecraft.block as block
import random
import time
import copy

mc = minecraft.Minecraft.create()

x,y,z = mc.player.getTilePos()
point = {'x': x, 'y': y+8, 'z': z}
axes = ['x', 'y', 'z']
mc.setBlock(point['x'], point['y'], point['z'], block.TNT)

#if __name__ == '__main__':
if True:
	while True:
		#Choose either x,y, or z and have it go 1 block in either direction
		axis = random.choice(axes)
		directions = [point[axis] - 2, point[axis] + 2]
		coordinate = random.choice(directions)
		new_point = copy.copy(point) #copy is so only one variable is written
		new_point[axis] = coordinate
		#If that block is air set block
		if mc.getBlock(new_point['x'], new_point['y'], new_point['z']) == block.AIR:
			mc.setBlocks(point['x'], point['y'], point['z'], new_point['x'], new_point['y'], new_point['z'], block.TNT)
			point[axis] = coordinate
			time.sleep(0.2)
