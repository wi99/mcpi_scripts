#!/usr/bin/env python
#https://www.youtube.com/watch?v=dfRcQHM9F4M

import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import random

mc = minecraft.Minecraft.create('')

mc.saveCheckpoint()

time.sleep(5)

def drop_sand(interval):
	for block_num in range(0,8):
		time.sleep(interval)
		mc.setBlock(30, 17, random.randrange(7, 14), block.SAND)

mc.postToChat('Level 1!')
drop_sand(3)
mc.postToChat('Level 2!')
drop_sand(2.5)
mc.postToChat('Level 3!')
drop_sand(2)
mc.postToChat('Level 4!')
drop_sand(1.5)
mc.postToChat('Bonus Round!')
for block_num in range(0,8):
	time.sleep(2)
	z = random.randrange(7, 14)
	mc.setBlock(30, 17, z, block.GRAVEL)
	time.sleep(0.2)
	mc.setBlock(30, 17, z, block.GRAVEL)

time.sleep(2)
mc.postToChat('A bigger challenge awaits you!')
time.sleep(4)

mc.restoreCheckpoint()
