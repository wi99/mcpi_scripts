#! /usr/bin/env python

#Monster Killer I used:
#http://minecraft.gamepedia.com/Tutorials/Mob_grinder#Fall_Damage_Mob_Killer
'''
Run this in survival mode to get resources dropped by dead monsters.
Run it in an area at or close to sea level (y~0).
'''

import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()

if __name__ == '__main__':
	pos = mc.player.getTilePos()

	solid_block = block.COBBLESTONE

	highpos = minecraft.Vec3(pos.x+2, pos.y+28, pos.z+2)

	mc.setBlock(highpos.x-10, pos.y, highpos.z-9, highpos.x+11,highpos.y, highpos.z+11,block.TORCH)

	#Whole Room, not hollowed
	mc.setBlocks(highpos.x-9, highpos.y, highpos.z-9, highpos.x+10,highpos.y+6, highpos.z+10, solid_block)
	#Hollow the top half (keep the cieling)
	mc.setBlocks(highpos.x-8, highpos.y+3, highpos.z-8, highpos.x+9,highpos.y+5, highpos.z+9, block.AIR)
	#Water and Waterway
	mc.setBlocks(highpos.x, highpos.y+1, highpos.z-8, highpos.x+1,highpos.y+2, highpos.z+9, block.AIR)
	mc.setBlocks(highpos.x-8, highpos.y+1, highpos.z, highpos.x+9,highpos.y+2, highpos.z+1, block.AIR)
	mc.setBlocks(highpos.x, highpos.y+1, highpos.z-8, highpos.x+1,highpos.y+1, highpos.z+9, block.WATER_FLOWING)
	mc.setBlocks(highpos.x-8, highpos.y+1, highpos.z, highpos.x+9,highpos.y+1, highpos.z+1, block.WATER_FLOWING)
	mc.setBlocks(highpos.x, highpos.y+1, highpos.z-7, highpos.x+1,highpos.y+1, highpos.z+8, block.AIR)
	mc.setBlocks(highpos.x-7, highpos.y+1, highpos.z, highpos.x+8,highpos.y+1, highpos.z+1, block.AIR)
	#Place torches on top to prevent them from spawning there.
	mc.setBlocks(highpos.x-9, highpos.y+7, highpos.z-9, highpos.x+10,highpos.y+7, highpos.z+10, block.TORCH)
	#Tunnel and 2x2 hole
	mc.setBlocks(highpos.x-1,pos.y,highpos.z-1, highpos.x+2,highpos.y,highpos.z+2, solid_block)
	mc.setBlocks(highpos.x,pos.y,highpos.z, highpos.x+1,highpos.y,highpos.z+1, block.AIR)
	#Opening
	mc.setBlocks(highpos.x-1,pos.y,highpos.z-1, highpos.x+2,pos.y+1,highpos.z+2, block.AIR)
