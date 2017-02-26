#!/usr/bin/env python
#https://www.youtube.com/watch?v=dfRcQHM9F4M

import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create('')

#Clear area
mc.setBlocks(31,19,-2, 18,0,22, block.AIR)

#Platform to run on
mc.setBlocks(21,3,6, 19,1,14, block.GLASS)
mc.setBlocks(21,3,7, 20,2,13, block.AIR)
mc.setBlocks(21,1,7, 20,1,13, block.STONE_BRICK)
mc.setBlocks(20,4,7, 20,4,13, block.FENCE_GATE.id, 1)
mc.setBlocks(21,2,7, 21,2,13, block.WOOL.id, 4)
mc.setBlocks(21,2,9, 21,2,11, block.WOOL.id, 1)
mc.setBlock(21,2,10, block.WOOL.id, 14)
mc.setBlock(21,0,6, block.WOOD)
mc.setBlock(19,0,6, block.WOOD)
mc.setBlock(21,0,14, block.WOOD)
mc.setBlock(19,0,14, block.WOOD)

time.sleep(1)

#CASTLE
#Side
mc.setBlocks(31,2,-2, 30,-1,22, block.STONE_BRICK)
mc.setBlock(31,3,-2, block.STONE_BRICK)
mc.setBlock(31,3,22, block.STONE_BRICK)
mc.setBlocks(30,3,-1, 30,2,21, block.AIR)
mc.setBlock(31,2,0, block.AIR)
mc.setBlock(31,2,2, block.AIR)
mc.setBlock(31,2,4, block.AIR)
mc.setBlock(31,2,16, block.AIR)
mc.setBlock(31,2,18, block.AIR)
mc.setBlock(31,2,20, block.AIR)
#Center
mc.setBlocks(31,18,5, 30,-1,15, block.STONE_BRICK)
mc.setBlocks(30,17,6, 30,1,14, block.AIR)
mc.setBlocks(30,0,13, 30,0,7, block.AIR)
