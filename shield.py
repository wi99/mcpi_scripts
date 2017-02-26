#! /usr/bin/env python

import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()

#Do not make this value smaller than 5 or the lava will be to close to the player.
radius = 5

if __name__ == '__main__':
	try:
		while True:
			pos = mc.player.getTilePos()
		
			lavapos1 = pos.x, pos.y+1, pos.z+radius
			if mc.getBlock(lavapos1) == block.AIR.id:
				mc.setBlock(lavapos1, block.LAVA_STATIONARY)
				lava1 = True
			else:
				lava1 = False
		
			lavapos2 = pos.x+radius, pos.y+1, pos.z
			if mc.getBlock(lavapos2) == block.AIR.id:
				mc.setBlock(lavapos2, block.LAVA_STATIONARY)
				lava2 = True
			else:
				lava2 = False
			
			lavapos3 = pos.x, pos.y+1, pos.z-radius
			if mc.getBlock(lavapos3) == block.AIR.id:
				mc.setBlock(lavapos3, block.LAVA_STATIONARY)
				lava3 = True
			else:
				lava3 = False

			lavapos4 = pos.x-radius, pos.y+1, pos.z
			if mc.getBlock(lavapos4) == block.AIR.id:
				mc.setBlock(lavapos4, block.LAVA_STATIONARY)
				lava4 = True
			else:
				lava4 = False

			waterpos1 = pos.x, pos.y, pos.z
			if mc.getBlock(waterpos1) == block.AIR.id:
				mc.setBlock(waterpos1, block.WATER_STATIONARY)
				water1 = True
			else:
				water1 = False

			lavapos5 = pos.x+radius, pos.y+1, pos.z+radius
			if mc.getBlock(lavapos5) == block.AIR.id:
				mc.setBlock(lavapos5, block.LAVA_STATIONARY)
				lava5 = True
			else:
				lava5 = False
		
			lavapos6 = pos.x+radius, pos.y+1, pos.z-radius
			if mc.getBlock(lavapos6) == block.AIR.id:
				mc.setBlock(lavapos6, block.LAVA_STATIONARY)
				lava6 = True
			else:
				lava6 = False
		
			lavapos7 = pos.x-radius, pos.y+1, pos.z-radius
			if mc.getBlock(lavapos7) == block.AIR.id:
				mc.setBlock(lavapos7, block.LAVA_STATIONARY)
				lava7 = True
			else:
				lava7 = False
	
			lavapos8 = pos.x-radius, pos.y+1, pos.z+radius
			if mc.getBlock(lavapos8) == block.AIR.id:
				mc.setBlock(lavapos8, block.LAVA_STATIONARY)
				lava8 = True
			else:
				lava8 = False
		
			while True:
				newpos = mc.player.getTilePos()
				if newpos != pos:
					if lava1 == True:
						mc.setBlock(lavapos1, block.AIR)
					if lava2 == True:
						mc.setBlock(lavapos2, block.AIR)
					if lava3 == True:
						mc.setBlock(lavapos3, block.AIR)
					if lava4 == True:
						mc.setBlock(lavapos4, block.AIR)
					if water1 == True:
						mc.setBlock(waterpos1, block.AIR)
					if lava5 == True:
						mc.setBlock(lavapos5, block.AIR)
					if lava6 == True:
						mc.setBlock(lavapos6, block.AIR)
					if lava7 == True:
						mc.setBlock(lavapos7, block.AIR)
					if lava8 == True:
						mc.setBlock(lavapos8, block.AIR)
					break

	except KeyboardInterrupt:
		if lava1 == True:
			mc.setBlock(lavapos1, block.AIR)
		if lava2 == True:
			mc.setBlock(lavapos2, block.AIR)
		if lava3 == True:
			mc.setBlock(lavapos3, block.AIR)
		if lava4 == True:
			mc.setBlock(lavapos4, block.AIR)
		if water1 == True:
			mc.setBlock(waterpos1, block.AIR)
		if lava5 == True:
			mc.setBlock(lavapos5, block.AIR)
		if lava6 == True:
			mc.setBlock(lavapos6, block.AIR)
		if lava7 == True:
			mc.setBlock(lavapos7, block.AIR)
		if lava8 == True:
			mc.setBlock(lavapos8, block.AIR)
