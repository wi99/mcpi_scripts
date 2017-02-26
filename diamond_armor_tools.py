#! /usr/bin/env python

import minecraft.minecraft as minecraft
import time
import minecraft.block as block

if __name__ == "__main__":
	time.sleep(2)
	mc = minecraft.Minecraft.create()
	x,y,z = mc.player.getTilePos()
	#3 wood blocks and 3 stone blocks
	mc.setBlocks(x-1,y,z-1, x-1,y+2,z-1, block.WOOD)
	mc.setBlocks(x-1,y,z+1, x-1,y+2,z+1, block.STONE)
	#1 workbench
	mc.setBlock(x+1, y, z, block.CRAFTING_TABLE)
	#4 diamond blocks and 1 iron block
	mc.setBlock(x-2,y,z-1, block.DIAMOND_BLOCK)
	mc.setBlock(x-2,y,z+1, block.DIAMOND_BLOCK)
	mc.setBlock(x-2,y+1,z-1, block.DIAMOND_BLOCK)
	mc.setBlock(x-2,y+1,z+1, block.DIAMOND_BLOCK)
	mc.setBlock(x-2,y+1,z, block.IRON_BLOCK)
