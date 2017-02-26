#!/usr/bin/env python

import minecraft.minecraft as minecraft
import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()
playerTilePos = mc.player.getTilePos()

time.sleep(30)
mc.postToChat("Brought to you by www.timkering.co.uk")
time.sleep(5)
mc.postToChat("Timker 2: The Minecraft Creation")
time.sleep(15)

#HOUSE_1
#SPACE
mc.setBlocks(-5, 0, -5, 14, 30, 14, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(0, -1, 0, 10, -1, 10, block.STONE_SLAB_DOUBLE)
mc.setBlocks(0, 0, 0, 10, 8, 10, block.BRICK_BLOCK)
mc.setBlocks(1, 0, 1, 9, 8, 9, block.AIR)
#WALL_ONE
mc.setBlocks(2, 1, 0, 3, 2, 0, block.GLASS)
mc.setBlocks(7, 1, 0, 8, 2, 0, block.GLASS)
mc.setBlocks(2, 6, 0, 3, 7, 0, block.GLASS)
mc.setBlocks(7, 6, 0, 8, 7, 0, block.GLASS)
#WALL_TWO
mc.setBlocks(10, 1, 2, 10, 2, 3, block.GLASS)
mc.setBlocks(10, 1, 7, 10, 2, 8, block.GLASS)
mc.setBlocks(10, 6, 2, 10, 7, 3, block.GLASS)
mc.setBlocks(10, 6, 7, 10, 7, 8, block.GLASS)
#WALL_THREE
mc.setBlocks(2, 1, 10, 3, 2, 10, block.GLASS)
mc.setBlocks(7, 1, 10, 8, 2, 10, block.GLASS)
mc.setBlocks(2, 6, 10, 3, 7, 10, block.GLASS)
mc.setBlocks(7, 6, 10, 8, 7, 10, block.GLASS)
#FRONT_WALL
mc.setBlocks(0, 1, 2, 0, 2, 3, block.GLASS)
mc.setBlocks(0, 1, 7, 0, 2, 8, block.GLASS)
mc.setBlocks(0, 6, 2, 0, 7, 3, block.GLASS)
mc.setBlocks(0, 6, 7, 0, 7, 8, block.GLASS)
mc.setBlocks(0, 0, 5, 0, 1, 5, block.AIR)
#SECOND_FLOOR
mc.setBlocks(1, 4, 1, 9, 4, 9, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(5, 4, 5, 8, 4, 5, block.AIR)
mc.setBlock(4,0,5,block.STAIRS_WOOD)
mc.setBlock(5,1,5,block.STAIRS_WOOD)
mc.setBlock(6,2,5,block.STAIRS_WOOD)
mc.setBlock(7,3,5,block.STAIRS_WOOD)
mc.setBlock(8,4,5,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(1, 5, 5, 4, 8, 5, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 1, 5, 8, 4, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 2, 5, 6, 2, block.AIR)
mc.setBlocks(5, 5, 6, 5, 8, 9, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 8, 5, 6, 8, block.AIR)
#ROOF
mc.setBlocks(0, 9, 0, 10, 9, 10, block.STONE)
mc.setBlocks(1, 9, 1, 9, 9, 9, block.GLASS)
mc.setBlocks(1, 10, 1, 9, 10, 9, block.STONE)
mc.setBlocks(2, 10, 2, 8, 10, 8, block.LAVA_STATIONARY)
mc.setBlocks(2, 11, 2, 8, 11, 8, block.STONE)
mc.setBlocks(3, 12, 3, 7, 12, 7, block.STONE)
mc.setBlocks(4, 13, 4, 6, 13, 6, block.STONE)
mc.setBlocks(5, 14, 5, 5, 14, 5, block.STONE)

#HOUSE_2
#SPACE
time.sleep(30)
mc.setBlocks(-5, 0, 15, 14, 30, 34, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(0, -1, 20, 10, -1, 30, block.STONE_SLAB_DOUBLE)
mc.setBlocks(0, 0, 20, 10, 8, 30, block.BRICK_BLOCK)
mc.setBlocks(1, 0, 21, 9, 8, 29, block.AIR)
#WALL_ONE
mc.setBlocks(2, 1, 20, 3, 2, 20, block.GLASS)
mc.setBlocks(7, 1, 20, 8, 2, 20, block.GLASS)
mc.setBlocks(2, 6, 20, 3, 7, 20, block.GLASS)
mc.setBlocks(7, 6, 20, 8, 7, 20, block.GLASS)
#WALL_TWO
mc.setBlocks(10, 1, 22, 10, 2, 23, block.GLASS)
mc.setBlocks(10, 1, 27, 10, 2, 28, block.GLASS)
mc.setBlocks(10, 6, 22, 10, 7, 23, block.GLASS)
mc.setBlocks(10, 6, 27, 10, 7, 28, block.GLASS)
#WALL_THREE
mc.setBlocks(2, 1, 30, 3, 2, 30, block.GLASS)
mc.setBlocks(7, 1, 30, 8, 2, 30, block.GLASS)
mc.setBlocks(2, 6, 30, 3, 7, 30, block.GLASS)
mc.setBlocks(7, 6, 30, 8, 7, 30, block.GLASS)
#FRONT_WALL
mc.setBlocks(0, 1, 22, 0, 2, 23, block.GLASS)
mc.setBlocks(0, 1, 27, 0, 2, 28, block.GLASS)
mc.setBlocks(0, 6, 22, 0, 7, 23, block.GLASS)
mc.setBlocks(0, 6, 27, 0, 7, 28, block.GLASS)
mc.setBlocks(0, 0, 25, 0, 1, 25, block.AIR)
#SECOND_FLOOR
mc.setBlocks(1, 4, 21, 9, 4, 29, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(5, 4, 25, 8, 4, 25, block.AIR)
mc.setBlock(4,0,25,block.STAIRS_WOOD)
mc.setBlock(5,1,25,block.STAIRS_WOOD)
mc.setBlock(6,2,25,block.STAIRS_WOOD)
mc.setBlock(7,3,25,block.STAIRS_WOOD)
mc.setBlock(8,4,25,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(1, 5, 25, 4, 8, 25, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 21, 5, 8, 24, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 22, 5, 6, 22, block.AIR)
mc.setBlocks(5, 5, 26, 5, 8, 29, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 28, 5, 6, 28, block.AIR)
#ROOF
mc.setBlocks(0, 9, 20, 10, 9, 30, block.STONE)
mc.setBlocks(1, 9, 21, 9, 9, 29, block.GLASS)
mc.setBlocks(1, 10, 21, 9, 10, 29, block.STONE)
mc.setBlocks(2, 10, 22, 8, 10, 28, block.LAVA_STATIONARY)
mc.setBlocks(2, 11, 22, 8, 11, 28, block.STONE)
mc.setBlocks(3, 12, 23, 7, 12, 27, block.STONE)
mc.setBlocks(4, 13, 24, 6, 13, 26, block.STONE)
mc.setBlocks(5, 14, 25, 5, 14, 25, block.STONE)

#HOUSE_3
#SPACE
time.sleep(5)
mc.setBlocks(-5, 0, 35, 14, 30, 54, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(0, -1, 40, 10, -1, 50, block.STONE_SLAB_DOUBLE)
mc.setBlocks(0, 0, 40, 10, 8, 50, block.BRICK_BLOCK)
mc.setBlocks(1, 0, 41, 9, 8, 49, block.AIR)
#WALL_ONE
mc.setBlocks(2, 1, 40, 3, 2, 40, block.GLASS)
mc.setBlocks(7, 1, 40, 8, 2, 40, block.GLASS)
mc.setBlocks(2, 6, 40, 3, 7, 40, block.GLASS)
mc.setBlocks(7, 6, 40, 8, 7, 40, block.GLASS)
#WALL_TWO
mc.setBlocks(10, 1, 42, 10, 2, 43, block.GLASS)
mc.setBlocks(10, 1, 47, 10, 2, 48, block.GLASS)
mc.setBlocks(10, 6, 42, 10, 7, 43, block.GLASS)
mc.setBlocks(10, 6, 47, 10, 7, 48, block.GLASS)
#WALL_THREE
mc.setBlocks(2, 1, 50, 3, 2, 50, block.GLASS)
mc.setBlocks(7, 1, 50, 8, 2, 50, block.GLASS)
mc.setBlocks(2, 6, 50, 3, 7, 50, block.GLASS)
mc.setBlocks(7, 6, 50, 8, 7, 50, block.GLASS)
#FRONT_WALL
mc.setBlocks(0, 1, 42, 0, 2, 43, block.GLASS)
mc.setBlocks(0, 1, 47, 0, 2, 48, block.GLASS)
mc.setBlocks(0, 6, 42, 0, 7, 43, block.GLASS)
mc.setBlocks(0, 6, 47, 0, 7, 48, block.GLASS)
mc.setBlocks(0, 0, 45, 0, 1, 45, block.AIR)
#SECOND_FLOOR
mc.setBlocks(1, 4, 41, 9, 4, 49, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(5, 4, 45, 8, 4, 45, block.AIR)
mc.setBlock(4,0,45,block.STAIRS_WOOD)
mc.setBlock(5,1,45,block.STAIRS_WOOD)
mc.setBlock(6,2,45,block.STAIRS_WOOD)
mc.setBlock(7,3,45,block.STAIRS_WOOD)
mc.setBlock(8,4,45,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(1, 5, 45, 4, 8, 45, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 41, 5, 8, 44, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 42, 5, 6, 42, block.AIR)
mc.setBlocks(5, 5, 46, 5, 8, 49, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 48, 5, 6, 48, block.AIR)
#ROOF
mc.setBlocks(0, 9, 40, 10, 9, 50, block.STONE)
mc.setBlocks(1, 9, 41, 9, 9, 49, block.GLASS)
mc.setBlocks(1, 10, 41, 9, 10, 49, block.STONE)
mc.setBlocks(2, 10, 42, 8, 10, 48, block.LAVA_STATIONARY)
mc.setBlocks(2, 11, 42, 8, 11, 48, block.STONE)
mc.setBlocks(3, 12, 43, 7, 12, 47, block.STONE)
mc.setBlocks(4, 13, 44, 6, 13, 46, block.STONE)
mc.setBlocks(5, 14, 45, 5, 14, 45, block.STONE)

#HOUSE_4
#SPACE
time.sleep(5)
mc.setBlocks(-5, 0, 55, 14, 30, 74, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(0, -1, 60, 10, -1, 70, block.STONE_SLAB_DOUBLE)
mc.setBlocks(0, 0, 60, 10, 8, 70, block.BRICK_BLOCK)
mc.setBlocks(1, 0, 61, 9, 8, 69, block.AIR)
#WALL_ONE
mc.setBlocks(2, 1, 60, 3, 2, 60, block.GLASS)
mc.setBlocks(7, 1, 60, 8, 2, 60, block.GLASS)
mc.setBlocks(2, 6, 60, 3, 7, 60, block.GLASS)
mc.setBlocks(7, 6, 60, 8, 7, 60, block.GLASS)
#WALL_TWO
mc.setBlocks(10, 1, 62, 10, 2, 63, block.GLASS)
mc.setBlocks(10, 1, 67, 10, 2, 68, block.GLASS)
mc.setBlocks(10, 6, 62, 10, 7, 63, block.GLASS)
mc.setBlocks(10, 6, 67, 10, 7, 68, block.GLASS)
#WALL_THREE
mc.setBlocks(2, 1, 70, 3, 2, 70, block.GLASS)
mc.setBlocks(7, 1, 70, 8, 2, 70, block.GLASS)
mc.setBlocks(2, 6, 70, 3, 7, 70, block.GLASS)
mc.setBlocks(7, 6, 70, 8, 7, 70, block.GLASS)
#FRONT_WALL
mc.setBlocks(0, 1, 62, 0, 2, 63, block.GLASS)
mc.setBlocks(0, 1, 67, 0, 2, 68, block.GLASS)
mc.setBlocks(0, 6, 62, 0, 7, 63, block.GLASS)
mc.setBlocks(0, 6, 67, 0, 7, 68, block.GLASS)
mc.setBlocks(0, 0, 65, 0, 1, 65, block.AIR)
#SECOND_FLOOR
mc.setBlocks(1, 4, 61, 9, 4, 69, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(5, 4, 65, 8, 4, 65, block.AIR)
mc.setBlock(4,0,65,block.STAIRS_WOOD)
mc.setBlock(5,1,65,block.STAIRS_WOOD)
mc.setBlock(6,2,65,block.STAIRS_WOOD)
mc.setBlock(7,3,65,block.STAIRS_WOOD)
mc.setBlock(8,4,65,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(1, 5, 65, 4, 8, 65, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 61, 5, 8, 64, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 62, 5, 6, 62, block.AIR)
mc.setBlocks(5, 5, 66, 5, 8, 69, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 68, 5, 6, 68, block.AIR)
#ROOF
mc.setBlocks(0, 9, 60, 10, 9, 70, block.STONE)
mc.setBlocks(1, 9, 61, 9, 9, 69, block.GLASS)
mc.setBlocks(1, 10, 61, 9, 10, 69, block.STONE)
mc.setBlocks(2, 10, 62, 8, 10, 68, block.LAVA_STATIONARY)
mc.setBlocks(2, 11, 62, 8, 11, 68, block.STONE)
mc.setBlocks(3, 12, 63, 7, 12, 67, block.STONE)
mc.setBlocks(4, 13, 64, 6, 13, 66, block.STONE)
mc.setBlocks(5, 14, 65, 5, 14, 65, block.STONE)

#HOUSE_5
#SPACE
time.sleep(5)
mc.setBlocks(-5, 0, 75, 14, 30, 94, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(0, -1, 80, 10, -1, 90, block.STONE_SLAB_DOUBLE)
mc.setBlocks(0, 0, 80, 10, 8, 90, block.BRICK_BLOCK)
mc.setBlocks(1, 0, 81, 9, 8, 89, block.AIR)
#WALL_ONE
mc.setBlocks(2, 1, 80, 3, 2, 80, block.GLASS)
mc.setBlocks(7, 1, 80, 8, 2, 80, block.GLASS)
mc.setBlocks(2, 6, 80, 3, 7, 80, block.GLASS)
mc.setBlocks(7, 6, 80, 8, 7, 80, block.GLASS)
#WALL_TWO
mc.setBlocks(10, 1, 82, 10, 2, 83, block.GLASS)
mc.setBlocks(10, 1, 87, 10, 2, 88, block.GLASS)
mc.setBlocks(10, 6, 82, 10, 7, 83, block.GLASS)
mc.setBlocks(10, 6, 87, 10, 7, 88, block.GLASS)
#WALL_THREE
mc.setBlocks(2, 1, 90, 3, 2, 90, block.GLASS)
mc.setBlocks(7, 1, 90, 8, 2, 90, block.GLASS)
mc.setBlocks(2, 6, 90, 3, 7, 90, block.GLASS)
mc.setBlocks(7, 6, 90, 8, 7, 90, block.GLASS)
#FRONT_WALL
mc.setBlocks(0, 1, 82, 0, 2, 83, block.GLASS)
mc.setBlocks(0, 1, 87, 0, 2, 88, block.GLASS)
mc.setBlocks(0, 6, 82, 0, 7, 83, block.GLASS)
mc.setBlocks(0, 6, 87, 0, 7, 88, block.GLASS)
mc.setBlocks(0, 0, 85, 0, 1, 85, block.AIR)
#SECOND_FLOOR
mc.setBlocks(1, 4, 81, 9, 4, 89, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(5, 4, 85, 8, 4, 85, block.AIR)
mc.setBlock(4,0,85,block.STAIRS_WOOD)
mc.setBlock(5,1,85,block.STAIRS_WOOD)
mc.setBlock(6,2,85,block.STAIRS_WOOD)
mc.setBlock(7,3,85,block.STAIRS_WOOD)
mc.setBlock(8,4,85,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(1, 5, 85, 4, 8, 85, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 81, 5, 8, 84, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 82, 5, 6, 82, block.AIR)
mc.setBlocks(5, 5, 86, 5, 8, 89, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 88, 5, 6, 88, block.AIR)
#ROOF
mc.setBlocks(0, 9, 80, 10, 9, 90, block.STONE)
mc.setBlocks(1, 9, 81, 9, 9, 89, block.GLASS)
mc.setBlocks(1, 10, 81, 9, 10, 89, block.STONE)
mc.setBlocks(2, 10, 82, 8, 10, 88, block.LAVA_STATIONARY)
mc.setBlocks(2, 11, 82, 8, 11, 88, block.STONE)
mc.setBlocks(3, 12, 83, 7, 12, 87, block.STONE)
mc.setBlocks(4, 13, 84, 6, 13, 86, block.STONE)
mc.setBlocks(5, 14, 85, 5, 14, 85, block.STONE)
#HOUSE_6
#SPACE
time.sleep(3)
mc.setBlocks(-5, 0, 95, 14, 30, 114, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(0, -1, 100, 10, -1, 110, block.STONE_SLAB_DOUBLE)
mc.setBlocks(0, 0, 100, 10, 8, 110, block.BRICK_BLOCK)
mc.setBlocks(1, 0, 101, 9, 8, 109, block.AIR)
#WALL_ONE
mc.setBlocks(2, 1, 100, 3, 2, 100, block.GLASS)
mc.setBlocks(7, 1, 100, 8, 2, 100, block.GLASS)
mc.setBlocks(2, 6, 100, 3, 7, 100, block.GLASS)
mc.setBlocks(7, 6, 100, 8, 7, 100, block.GLASS)
#WALL_TWO
mc.setBlocks(10, 1, 102, 10, 2, 103, block.GLASS)
mc.setBlocks(10, 1, 107, 10, 2, 108, block.GLASS)
mc.setBlocks(10, 6, 102, 10, 7, 103, block.GLASS)
mc.setBlocks(10, 6, 107, 10, 7, 108, block.GLASS)
#WALL_THREE
mc.setBlocks(2, 1, 110, 3, 2, 110, block.GLASS)
mc.setBlocks(7, 1, 110, 8, 2, 110, block.GLASS)
mc.setBlocks(2, 6, 110, 3, 7, 110, block.GLASS)
mc.setBlocks(7, 6, 110, 8, 7, 110, block.GLASS)
#FRONT_WALL
mc.setBlocks(0, 1, 102, 0, 2, 103, block.GLASS)
mc.setBlocks(0, 1, 107, 0, 2, 108, block.GLASS)
mc.setBlocks(0, 6, 102, 0, 7, 103, block.GLASS)
mc.setBlocks(0, 6, 107, 0, 7, 108, block.GLASS)
mc.setBlocks(0, 0, 105, 0, 1, 105, block.AIR)
#SECOND_FLOOR
mc.setBlocks(1, 4, 101, 9, 4, 109, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(5, 4, 105, 8, 4, 105, block.AIR)
mc.setBlock(4,0,105,block.STAIRS_WOOD)
mc.setBlock(5,1,105,block.STAIRS_WOOD)
mc.setBlock(6,2,105,block.STAIRS_WOOD)
mc.setBlock(7,3,105,block.STAIRS_WOOD)
mc.setBlock(8,4,105,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(1, 5, 105, 4, 8, 105, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 101, 5, 8, 104, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 102, 5, 6, 102, block.AIR)
mc.setBlocks(5, 5, 106, 5, 8, 109, block.WOOD_PLANKS)
mc.setBlocks(5, 5, 108, 5, 6, 108, block.AIR)
#ROOF
mc.setBlocks(0, 9, 100, 10, 9, 110, block.STONE)
mc.setBlocks(1, 9, 101, 9, 9, 109, block.GLASS)
mc.setBlocks(1, 10, 101, 9, 10, 109, block.STONE)
mc.setBlocks(2, 10, 102, 8, 10, 108, block.LAVA_STATIONARY)
mc.setBlocks(2, 11, 102, 8, 11, 108, block.STONE)
mc.setBlocks(3, 12, 103, 7, 12, 107, block.STONE)
mc.setBlocks(4, 13, 104, 6, 13, 106, block.STONE)
mc.setBlocks(5, 14, 105, 5, 14, 105, block.STONE)

#NEW_ROW
#HOUSE_7
#SPACE
time.sleep(3)
mc.setBlocks(-25, 0, 95, -6, 30, 114, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(-20, -1, 100, -10, -1, 110, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-20, 0, 100, -10, 8, 110, block.BRICK_BLOCK)
mc.setBlocks(-19, 0, 101, -11, 8, 109, block.AIR)
#WALL_ONE
mc.setBlocks(-18, 1, 100, -17, 2, 100, block.GLASS)
mc.setBlocks(-13, 1, 100, -12, 2, 100, block.GLASS)
mc.setBlocks(-18, 6, 100, -17, 7, 100, block.GLASS)
mc.setBlocks(-13, 6, 100, -12, 7, 100, block.GLASS)
mc.setBlocks(-15, 0, 100, -15, 1, 100, block.AIR)
#WALL_TWO
mc.setBlocks(-10, 1, 102, -10, 2, 103, block.GLASS)
mc.setBlocks(-10, 1, 107, -10, 2, 108, block.GLASS)
mc.setBlocks(-10, 6, 102, -10, 7, 103, block.GLASS)
mc.setBlocks(-10, 6, 107, -10, 7, 108, block.GLASS)
#WALL_THREE
mc.setBlocks(-18, 1, 110, -17, 2, 110, block.GLASS)
mc.setBlocks(-13, 1, 110, -12, 2, 110, block.GLASS)
mc.setBlocks(-18, 6, 110, -17, 7, 110, block.GLASS)
mc.setBlocks(-13, 6, 110, -12, 7, 110, block.GLASS)
#FRONT_WALL
mc.setBlocks(-20, 1, 102, -20, 2, 103, block.GLASS)
mc.setBlocks(-20, 1, 107, -20, 2, 108, block.GLASS)
mc.setBlocks(-20, 6, 102, -20, 7, 103, block.GLASS)
mc.setBlocks(-20, 6, 107, -20, 7, 108, block.GLASS)
#SECOND_FLOOR
mc.setBlocks(-19, 4, 101, -11, 4, 109, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(-15, 4, 105, -12, 4, 105, block.AIR)
mc.setBlock(-16,0,105,block.STAIRS_WOOD)
mc.setBlock(-15,1,105,block.STAIRS_WOOD)
mc.setBlock(-14,2,105,block.STAIRS_WOOD)
mc.setBlock(-13,3,105,block.STAIRS_WOOD)
mc.setBlock(-12,4,105,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(-19, 5, 105, -16, 8, 105, block.WOOD_PLANKS)
mc.setBlocks(-15, 5, 101, -15, 8, 104, block.WOOD_PLANKS)
mc.setBlocks(-15, 5, 102, -15, 6, 102, block.AIR)
mc.setBlocks(-15, 5, 106, -15, 8, 109, block.WOOD_PLANKS)
mc.setBlocks(-15, 5, 108, -15, 6, 108, block.AIR)
#ROOF
mc.setBlocks(-20, 9, 100, -10, 9, 110, block.STONE)
mc.setBlocks(-19, 9, 101, -11, 9, 109, block.GLASS)
mc.setBlocks(-19, 10, 101, -11, 10, 109, block.STONE)
mc.setBlocks(-18, 10, 102, -12, 10, 108, block.LAVA_STATIONARY)
mc.setBlocks(-18, 11, 102, -12, 11, 108, block.STONE)
mc.setBlocks(-17, 12, 103, -13, 12, 107, block.STONE)
mc.setBlocks(-16, 13, 104, -14, 13, 106, block.STONE)
mc.setBlocks(-15, 14, 105, -15, 14, 105, block.STONE)

#HOUSE_8
#SPACE
time.sleep(3)
mc.setBlocks(-45, 0, 95, -26, 30, 114, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(-40, -1, 100, -30, -1, 110, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-40, 0, 100, -30, 8, 110, block.BRICK_BLOCK)
mc.setBlocks(-39, 0, 101, -31, 8, 109, block.AIR)
#WALL_ONE
mc.setBlocks(-38, 1, 100, -37, 2, 100, block.GLASS)
mc.setBlocks(-33, 1, 100, -32, 2, 100, block.GLASS)
mc.setBlocks(-38, 6, 100, -37, 7, 100, block.GLASS)
mc.setBlocks(-33, 6, 100, -32, 7, 100, block.GLASS)
mc.setBlocks(-35, 0, 100, -35, 1, 100, block.AIR)
#WALL_TWO
mc.setBlocks(-30, 1, 102, -30, 2, 103, block.GLASS)
mc.setBlocks(-30, 1, 107, -30, 2, 108, block.GLASS)
mc.setBlocks(-30, 6, 102, -30, 7, 103, block.GLASS)
mc.setBlocks(-30, 6, 107, -30, 7, 108, block.GLASS)
#WALL_THREE
mc.setBlocks(-38, 1, 110, -37, 2, 110, block.GLASS)
mc.setBlocks(-33, 1, 110, -32, 2, 110, block.GLASS)
mc.setBlocks(-38, 6, 110, -37, 7, 110, block.GLASS)
mc.setBlocks(-33, 6, 110, -32, 7, 110, block.GLASS)
#FRONT_WALL
mc.setBlocks(-40, 1, 102, -40, 2, 103, block.GLASS)
mc.setBlocks(-40, 1, 107, -40, 2, 108, block.GLASS)
mc.setBlocks(-40, 6, 102, -40, 7, 103, block.GLASS)
mc.setBlocks(-40, 6, 107, -40, 7, 108, block.GLASS)
#SECOND_FLOOR
mc.setBlocks(-39, 4, 101, -31, 4, 109, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(-35, 4, 105, -32, 4, 105, block.AIR)
mc.setBlock(-36,0,105,block.STAIRS_WOOD)
mc.setBlock(-35,1,105,block.STAIRS_WOOD)
mc.setBlock(-34,2,105,block.STAIRS_WOOD)
mc.setBlock(-33,3,105,block.STAIRS_WOOD)
mc.setBlock(-32,4,105,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(-39, 5, 105, -36, 8, 105, block.WOOD_PLANKS)
mc.setBlocks(-35, 5, 101, -35, 8, 104, block.WOOD_PLANKS)
mc.setBlocks(-35, 5, 102, -35, 6, 102, block.AIR)
mc.setBlocks(-35, 5, 106, -35, 8, 109, block.WOOD_PLANKS)
mc.setBlocks(-35, 5, 108, -35, 6, 108, block.AIR)
#ROOF
mc.setBlocks(-40, 9, 100, -30, 9, 110, block.STONE)
mc.setBlocks(-39, 9, 101, -31, 9, 109, block.GLASS)
mc.setBlocks(-39, 10, 101, -31, 10, 109, block.STONE)
mc.setBlocks(-38, 10, 102, -32, 10, 108, block.LAVA_STATIONARY)
mc.setBlocks(-38, 11, 102, -32, 11, 108, block.STONE)
mc.setBlocks(-37, 12, 103, -33, 12, 107, block.STONE)
mc.setBlocks(-36, 13, 104, -34, 13, 106, block.STONE)
mc.setBlocks(-35, 14, 105, -35, 14, 105, block.STONE)

#HOUSE_9
#SPACE
time.sleep(3)
mc.setBlocks(-65, 0, 95, -46, 30, 114, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(-60, -1, 100, -50, -1, 110, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-60, 0, 100, -50, 8, 110, block.BRICK_BLOCK)
mc.setBlocks(-59, 0, 101, -51, 8, 109, block.AIR)
#WALL_ONE
mc.setBlocks(-58, 1, 100, -57, 2, 100, block.GLASS)
mc.setBlocks(-53, 1, 100, -52, 2, 100, block.GLASS)
mc.setBlocks(-58, 6, 100, -57, 7, 100, block.GLASS)
mc.setBlocks(-53, 6, 100, -52, 7, 100, block.GLASS)
mc.setBlocks(-55, 0, 100, -55, 1, 100, block.AIR)
#WALL_TWO
mc.setBlocks(-50, 1, 102, -50, 2, 103, block.GLASS)
mc.setBlocks(-50, 1, 107, -50, 2, 108, block.GLASS)
mc.setBlocks(-50, 6, 102, -50, 7, 103, block.GLASS)
mc.setBlocks(-50, 6, 107, -50, 7, 108, block.GLASS)
#WALL_THREE
mc.setBlocks(-58, 1, 110, -57, 2, 110, block.GLASS)
mc.setBlocks(-53, 1, 110, -52, 2, 110, block.GLASS)
mc.setBlocks(-58, 6, 110, -57, 7, 110, block.GLASS)
mc.setBlocks(-53, 6, 110, -52, 7, 110, block.GLASS)
#FRONT_WALL
mc.setBlocks(-60, 1, 102, -60, 2, 103, block.GLASS)
mc.setBlocks(-60, 1, 107, -60, 2, 108, block.GLASS)
mc.setBlocks(-60, 6, 102, -60, 7, 103, block.GLASS)
mc.setBlocks(-60, 6, 107, -60, 7, 108, block.GLASS)
#SECOND_FLOOR
mc.setBlocks(-59, 4, 101, -51, 4, 109, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(-55, 4, 105, -52, 4, 105, block.AIR)
mc.setBlock(-56,0,105,block.STAIRS_WOOD)
mc.setBlock(-55,1,105,block.STAIRS_WOOD)
mc.setBlock(-54,2,105,block.STAIRS_WOOD)
mc.setBlock(-53,3,105,block.STAIRS_WOOD)
mc.setBlock(-52,4,105,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(-59, 5, 105, -56, 8, 105, block.WOOD_PLANKS)
mc.setBlocks(-55, 5, 101, -55, 8, 104, block.WOOD_PLANKS)
mc.setBlocks(-55, 5, 102, -55, 6, 102, block.AIR)
mc.setBlocks(-55, 5, 106, -55, 8, 109, block.WOOD_PLANKS)
mc.setBlocks(-55, 5, 108, -55, 6, 108, block.AIR)
#ROOF
mc.setBlocks(-60, 9, 100, -50, 9, 110, block.STONE)
mc.setBlocks(-59, 9, 101, -51, 9, 109, block.GLASS)
mc.setBlocks(-59, 10, 101, -51, 10, 109, block.STONE)
mc.setBlocks(-58, 10, 102, -52, 10, 108, block.LAVA_STATIONARY)
mc.setBlocks(-58, 11, 102, -52, 11, 108, block.STONE)
mc.setBlocks(-57, 12, 103, -53, 12, 107, block.STONE)
mc.setBlocks(-56, 13, 104, -54, 13, 106, block.STONE)
mc.setBlocks(-55, 14, 105, -55, 14, 105, block.STONE)

#HOUSE_10
#SPACE
time.sleep(3)
mc.setBlocks(-85, 0, 95, -66, 30, 114, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(-80, -1, 100, -70, -1, 110, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-80, 0, 100, -70, 8, 110, block.BRICK_BLOCK)
mc.setBlocks(-79, 0, 101, -71, 8, 109, block.AIR)
#WALL_ONE
mc.setBlocks(-78, 1, 100, -77, 2, 100, block.GLASS)
mc.setBlocks(-73, 1, 100, -72, 2, 100, block.GLASS)
mc.setBlocks(-78, 6, 100, -77, 7, 100, block.GLASS)
mc.setBlocks(-73, 6, 100, -72, 7, 100, block.GLASS)
mc.setBlocks(-75, 0, 100, -75, 1, 100, block.AIR)
#WALL_TWO
mc.setBlocks(-70, 1, 102, -70, 2, 103, block.GLASS)
mc.setBlocks(-70, 1, 107, -70, 2, 108, block.GLASS)
mc.setBlocks(-70, 6, 102, -70, 7, 103, block.GLASS)
mc.setBlocks(-70, 6, 107, -70, 7, 108, block.GLASS)
#WALL_THREE
mc.setBlocks(-78, 1, 110, -77, 2, 110, block.GLASS)
mc.setBlocks(-73, 1, 110, -72, 2, 110, block.GLASS)
mc.setBlocks(-78, 6, 110, -77, 7, 110, block.GLASS)
mc.setBlocks(-73, 6, 110, -72, 7, 110, block.GLASS)
#FRONT_WALL
mc.setBlocks(-80, 1, 102, -80, 2, 103, block.GLASS)
mc.setBlocks(-80, 1, 107, -80, 2, 108, block.GLASS)
mc.setBlocks(-80, 6, 102, -80, 7, 103, block.GLASS)
mc.setBlocks(-80, 6, 107, -80, 7, 108, block.GLASS)
#SECOND_FLOOR
mc.setBlocks(-79, 4, 101, -71, 4, 109, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(-75, 4, 105, -72, 4, 105, block.AIR)
mc.setBlock(-76,0,105,block.STAIRS_WOOD)
mc.setBlock(-75,1,105,block.STAIRS_WOOD)
mc.setBlock(-74,2,105,block.STAIRS_WOOD)
mc.setBlock(-73,3,105,block.STAIRS_WOOD)
mc.setBlock(-72,4,105,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(-79, 5, 105, -76, 8, 105, block.WOOD_PLANKS)
mc.setBlocks(-75, 5, 101, -75, 8, 104, block.WOOD_PLANKS)
mc.setBlocks(-75, 5, 102, -75, 6, 102, block.AIR)
mc.setBlocks(-75, 5, 106, -75, 8, 109, block.WOOD_PLANKS)
mc.setBlocks(-75, 5, 108, -75, 6, 108, block.AIR)
#ROOF
mc.setBlocks(-80, 9, 100, -70, 9, 110, block.STONE)
mc.setBlocks(-79, 9, 101, -71, 9, 109, block.GLASS)
mc.setBlocks(-79, 10, 101, -71, 10, 109, block.STONE)
mc.setBlocks(-78, 10, 102, -72, 10, 108, block.LAVA_STATIONARY)
mc.setBlocks(-78, 11, 102, -72, 11, 108, block.STONE)
mc.setBlocks(-77, 12, 103, -73, 12, 107, block.STONE)
mc.setBlocks(-76, 13, 104, -74, 13, 106, block.STONE)
mc.setBlocks(-75, 14, 105, -75, 14, 105, block.STONE)

#HOUSE_11
#SPACE
time.sleep(3)
mc.setBlocks(-105, 0, 95, -86, 30, 114, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(-100, -1, 100, -90, -1, 110, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-100, 0, 100, -90, 8, 110, block.BRICK_BLOCK)
mc.setBlocks(-99, 0, 101, -91, 8, 109, block.AIR)
#WALL_ONE
mc.setBlocks(-98, 1, 100, -97, 2, 100, block.GLASS)
mc.setBlocks(-93, 1, 100, -92, 2, 100, block.GLASS)
mc.setBlocks(-98, 6, 100, -97, 7, 100, block.GLASS)
mc.setBlocks(-93, 6, 100, -92, 7, 100, block.GLASS)
mc.setBlocks(-95, 0, 100, -95, 1, 100, block.AIR)
#WALL_TWO
mc.setBlocks(-90, 1, 102, -90, 2, 103, block.GLASS)
mc.setBlocks(-90, 1, 107, -90, 2, 108, block.GLASS)
mc.setBlocks(-90, 6, 102, -90, 7, 103, block.GLASS)
mc.setBlocks(-90, 6, 107, -90, 7, 108, block.GLASS)
#WALL_THREE
mc.setBlocks(-98, 1, 110, -97, 2, 110, block.GLASS)
mc.setBlocks(-93, 1, 110, -92, 2, 110, block.GLASS)
mc.setBlocks(-98, 6, 110, -97, 7, 110, block.GLASS)
mc.setBlocks(-93, 6, 110, -92, 7, 110, block.GLASS)
#FRONT_WALL
mc.setBlocks(-100, 1, 102, -100, 2, 103, block.GLASS)
mc.setBlocks(-100, 1, 107, -100, 2, 108, block.GLASS)
mc.setBlocks(-100, 6, 102, -100, 7, 103, block.GLASS)
mc.setBlocks(-100, 6, 107, -100, 7, 108, block.GLASS)
#SECOND_FLOOR
mc.setBlocks(-99, 4, 101, -91, 4, 109, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(-95, 4, 105, -92, 4, 105, block.AIR)
mc.setBlock(-96,0,105,block.STAIRS_WOOD)
mc.setBlock(-95,1,105,block.STAIRS_WOOD)
mc.setBlock(-94,2,105,block.STAIRS_WOOD)
mc.setBlock(-93,3,105,block.STAIRS_WOOD)
mc.setBlock(-92,4,105,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(-99, 5, 105, -96, 8, 105, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 101, -95, 8, 104, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 102, -95, 6, 102, block.AIR)
mc.setBlocks(-95, 5, 106, -95, 8, 109, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 108, -95, 6, 108, block.AIR)
#ROOF
mc.setBlocks(-100, 9, 100, -90, 9, 110, block.STONE)
mc.setBlocks(-99, 9, 101, -91, 9, 109, block.GLASS)
mc.setBlocks(-99, 10, 101, -91, 10, 109, block.STONE)
mc.setBlocks(-98, 10, 102, -92, 10, 108, block.LAVA_STATIONARY)
mc.setBlocks(-98, 11, 102, -92, 11, 108, block.STONE)
mc.setBlocks(-97, 12, 103, -93, 12, 107, block.STONE)
mc.setBlocks(-96, 13, 104, -94, 13, 106, block.STONE)
mc.setBlocks(-95, 14, 105, -95, 14, 105, block.STONE)

#NEW_ROW
#HOUSE_12
#SPACE
time.sleep(3)
mc.setBlocks(-105, 0, 75, -86, 30, 94, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(-100, -1, 80, -90, -1, 90, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-100, 0, 80, -90, 8, 90, block.BRICK_BLOCK)
mc.setBlocks(-99, 0, 81, -91, 8, 89, block.AIR)
#WALL_ONE
mc.setBlocks(-98, 1, 80, -97, 2, 80, block.GLASS)
mc.setBlocks(-93, 1, 80, -92, 2, 80, block.GLASS)
mc.setBlocks(-98, 6, 80, -97, 7, 80, block.GLASS)
mc.setBlocks(-93, 6, 80, -92, 7, 80, block.GLASS)
#WALL_TWO
mc.setBlocks(-90, 1, 82, -90, 2, 83, block.GLASS)
mc.setBlocks(-90, 1, 87, -90, 2, 88, block.GLASS)
mc.setBlocks(-90, 6, 82, -90, 7, 83, block.GLASS)
mc.setBlocks(-90, 6, 87, -90, 7, 88, block.GLASS)
mc.setBlocks(-90, 0, 85, -90, 1, 85, block.AIR)
#WALL_THREE
mc.setBlocks(-98, 1, 90, -97, 2, 90, block.GLASS)
mc.setBlocks(-93, 1, 90, -92, 2, 90, block.GLASS)
mc.setBlocks(-98, 6, 90, -97, 7, 90, block.GLASS)
mc.setBlocks(-93, 6, 90, -92, 7, 90, block.GLASS)
#FRONT_WALL
mc.setBlocks(-100, 1, 82, -100, 2, 83, block.GLASS)
mc.setBlocks(-100, 1, 87, -100, 2, 88, block.GLASS)
mc.setBlocks(-100, 6, 82, -100, 7, 83, block.GLASS)
mc.setBlocks(-100, 6, 87, -100, 7, 88, block.GLASS)
#SECOND_FLOOR
mc.setBlocks(-99, 4, 81, -91, 4, 89, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(-95, 4, 85, -92, 4, 85, block.AIR)
mc.setBlock(-96,0,85,block.STAIRS_WOOD)
mc.setBlock(-95,1,85,block.STAIRS_WOOD)
mc.setBlock(-94,2,85,block.STAIRS_WOOD)
mc.setBlock(-93,3,85,block.STAIRS_WOOD)
mc.setBlock(-92,4,85,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(-99, 5, 85, -96, 8, 85, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 81, -95, 8, 84, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 82, -95, 6, 82, block.AIR)
mc.setBlocks(-95, 5, 86, -95, 8, 89, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 88, -95, 6, 88, block.AIR)
#ROOF
mc.setBlocks(-100, 9, 80, -90, 9, 90, block.STONE)
mc.setBlocks(-99, 9, 81, -91, 9, 89, block.GLASS)
mc.setBlocks(-99, 10, 81, -91, 10, 89, block.STONE)
mc.setBlocks(-98, 10, 82, -92, 10, 88, block.LAVA_STATIONARY)
mc.setBlocks(-98, 11, 82, -92, 11, 88, block.STONE)
mc.setBlocks(-97, 12, 83, -93, 12, 87, block.STONE)
mc.setBlocks(-96, 13, 84, -94, 13, 86, block.STONE)
mc.setBlocks(-95, 14, 85, -95, 14, 85, block.STONE)

#HOUSE_13
#SPACE
time.sleep(3)
mc.setBlocks(-105, 0, 55, -86, 30, 74, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(-100, -1, 60, -90, -1, 70, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-100, 0, 60, -90, 8, 70, block.BRICK_BLOCK)
mc.setBlocks(-99, 0, 61, -91, 8, 69, block.AIR)
#WALL_ONE
mc.setBlocks(-98, 1, 60, -97, 2, 60, block.GLASS)
mc.setBlocks(-93, 1, 60, -92, 2, 60, block.GLASS)
mc.setBlocks(-98, 6, 60, -97, 7, 60, block.GLASS)
mc.setBlocks(-93, 6, 60, -92, 7, 60, block.GLASS)
#WALL_TWO
mc.setBlocks(-90, 1, 62, -90, 2, 63, block.GLASS)
mc.setBlocks(-90, 1, 67, -90, 2, 68, block.GLASS)
mc.setBlocks(-90, 6, 62, -90, 7, 63, block.GLASS)
mc.setBlocks(-90, 6, 67, -90, 7, 68, block.GLASS)
mc.setBlocks(-90, 0, 65, -90, 1, 65, block.AIR)
#WALL_THREE
mc.setBlocks(-98, 1, 70, -97, 2, 70, block.GLASS)
mc.setBlocks(-93, 1, 70, -92, 2, 70, block.GLASS)
mc.setBlocks(-98, 6, 70, -97, 7, 70, block.GLASS)
mc.setBlocks(-93, 6, 70, -92, 7, 70, block.GLASS)
#FRONT_WALL
mc.setBlocks(-100, 1, 62, -100, 2, 63, block.GLASS)
mc.setBlocks(-100, 1, 67, -100, 2, 68, block.GLASS)
mc.setBlocks(-100, 6, 62, -100, 7, 63, block.GLASS)
mc.setBlocks(-100, 6, 67, -100, 7, 68, block.GLASS)
#SECOND_FLOOR
mc.setBlocks(-99, 4, 61, -91, 4, 69, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(-95, 4, 65, -92, 4, 65, block.AIR)
mc.setBlock(-96,0,65,block.STAIRS_WOOD)
mc.setBlock(-95,1,65,block.STAIRS_WOOD)
mc.setBlock(-94,2,65,block.STAIRS_WOOD)
mc.setBlock(-93,3,65,block.STAIRS_WOOD)
mc.setBlock(-92,4,65,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(-99, 5, 65, -96, 8, 65, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 61, -95, 8, 64, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 62, -95, 6, 62, block.AIR)
mc.setBlocks(-95, 5, 66, -95, 8, 69, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 68, -95, 6, 68, block.AIR)
#ROOF
mc.setBlocks(-100, 9, 60, -90, 9, 70, block.STONE)
mc.setBlocks(-99, 9, 61, -91, 9, 69, block.GLASS)
mc.setBlocks(-99, 10, 61, -91, 10, 69, block.STONE)
mc.setBlocks(-98, 10, 62, -92, 10, 68, block.LAVA_STATIONARY)
mc.setBlocks(-98, 11, 62, -92, 11, 68, block.STONE)
mc.setBlocks(-97, 12, 63, -93, 12, 67, block.STONE)
mc.setBlocks(-96, 13, 64, -94, 13, 66, block.STONE)
mc.setBlocks(-95, 14, 65, -95, 14, 65, block.STONE)

#HOUSE_14
#SPACE
time.sleep(3)
mc.setBlocks(-105, 0, 35, -86, 30, 54, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(-100, -1, 40, -90, -1, 50, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-100, 0, 40, -90, 8, 50, block.BRICK_BLOCK)
mc.setBlocks(-99, 0, 41, -91, 8, 49, block.AIR)
#WALL_ONE
mc.setBlocks(-98, 1, 40, -97, 2, 40, block.GLASS)
mc.setBlocks(-93, 1, 40, -92, 2, 40, block.GLASS)
mc.setBlocks(-98, 6, 40, -97, 7, 40, block.GLASS)
mc.setBlocks(-93, 6, 40, -92, 7, 40, block.GLASS)
#WALL_TWO
mc.setBlocks(-90, 1, 42, -90, 2, 43, block.GLASS)
mc.setBlocks(-90, 1, 47, -90, 2, 48, block.GLASS)
mc.setBlocks(-90, 6, 42, -90, 7, 43, block.GLASS)
mc.setBlocks(-90, 6, 47, -90, 7, 48, block.GLASS)
mc.setBlocks(-90, 0, 45, -90, 1, 45, block.AIR)
#WALL_THREE
mc.setBlocks(-98, 1, 50, -97, 2, 50, block.GLASS)
mc.setBlocks(-93, 1, 50, -92, 2, 50, block.GLASS)
mc.setBlocks(-98, 6, 50, -97, 7, 50, block.GLASS)
mc.setBlocks(-93, 6, 50, -92, 7, 50, block.GLASS)
#FRONT_WALL
mc.setBlocks(-100, 1, 42, -100, 2, 43, block.GLASS)
mc.setBlocks(-100, 1, 47, -100, 2, 48, block.GLASS)
mc.setBlocks(-100, 6, 42, -100, 7, 43, block.GLASS)
mc.setBlocks(-100, 6, 47, -100, 7, 48, block.GLASS)
#SECOND_FLOOR
mc.setBlocks(-99, 4, 41, -91, 4, 49, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(-95, 4, 45, -92, 4, 45, block.AIR)
mc.setBlock(-96,0,45,block.STAIRS_WOOD)
mc.setBlock(-95,1,45,block.STAIRS_WOOD)
mc.setBlock(-94,2,45,block.STAIRS_WOOD)
mc.setBlock(-93,3,45,block.STAIRS_WOOD)
mc.setBlock(-92,4,45,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(-99, 5, 45, -96, 8, 45, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 41, -95, 8, 44, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 42, -95, 6, 42, block.AIR)
mc.setBlocks(-95, 5, 46, -95, 8, 49, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 48, -95, 6, 48, block.AIR)
#ROOF
mc.setBlocks(-100, 9, 40, -90, 9, 50, block.STONE)
mc.setBlocks(-99, 9, 41, -91, 9, 49, block.GLASS)
mc.setBlocks(-99, 10, 41, -91, 10, 49, block.STONE)
mc.setBlocks(-98, 10, 42, -92, 10, 48, block.LAVA_STATIONARY)
mc.setBlocks(-98, 11, 42, -92, 11, 48, block.STONE)
mc.setBlocks(-97, 12, 43, -93, 12, 47, block.STONE)
mc.setBlocks(-96, 13, 44, -94, 13, 46, block.STONE)
mc.setBlocks(-95, 14, 45, -95, 14, 45, block.STONE)

#HOUSE_15
#SPACE
time.sleep(3)
mc.setBlocks(-105, 0, 15, -86, 30, 34, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(-100, -1, 20, -90, -1, 30, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-100, 0, 20, -90, 8, 30, block.BRICK_BLOCK)
mc.setBlocks(-99, 0, 21, -91, 8, 29, block.AIR)
#WALL_ONE
mc.setBlocks(-98, 1, 20, -97, 2, 20, block.GLASS)
mc.setBlocks(-93, 1, 20, -92, 2, 20, block.GLASS)
mc.setBlocks(-98, 6, 20, -97, 7, 20, block.GLASS)
mc.setBlocks(-93, 6, 20, -92, 7, 20, block.GLASS)
#WALL_TWO
mc.setBlocks(-90, 1, 22, -90, 2, 23, block.GLASS)
mc.setBlocks(-90, 1, 27, -90, 2, 28, block.GLASS)
mc.setBlocks(-90, 6, 22, -90, 7, 23, block.GLASS)
mc.setBlocks(-90, 6, 27, -90, 7, 28, block.GLASS)
mc.setBlocks(-90, 0, 25, -90, 1, 25, block.AIR)
#WALL_THREE
mc.setBlocks(-98, 1, 30, -97, 2, 30, block.GLASS)
mc.setBlocks(-93, 1, 30, -92, 2, 30, block.GLASS)
mc.setBlocks(-98, 6, 30, -97, 7, 30, block.GLASS)
mc.setBlocks(-93, 6, 30, -92, 7, 30, block.GLASS)
#FRONT_WALL
mc.setBlocks(-100, 1, 22, -100, 2, 23, block.GLASS)
mc.setBlocks(-100, 1, 27, -100, 2, 28, block.GLASS)
mc.setBlocks(-100, 6, 22, -100, 7, 23, block.GLASS)
mc.setBlocks(-100, 6, 27, -100, 7, 28, block.GLASS)
#SECOND_FLOOR
mc.setBlocks(-99, 4, 21, -91, 4, 29, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(-95, 4, 25, -92, 4, 25, block.AIR)
mc.setBlock(-96,0,25,block.STAIRS_WOOD)
mc.setBlock(-95,1,25,block.STAIRS_WOOD)
mc.setBlock(-94,2,25,block.STAIRS_WOOD)
mc.setBlock(-93,3,25,block.STAIRS_WOOD)
mc.setBlock(-92,4,25,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(-99, 5, 25, -96, 8, 25, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 21, -95, 8, 24, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 22, -95, 6, 22, block.AIR)
mc.setBlocks(-95, 5, 26, -95, 8, 29, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 28, -95, 6, 28, block.AIR)
#ROOF
mc.setBlocks(-100, 9, 20, -90, 9, 30, block.STONE)
mc.setBlocks(-99, 9, 21, -91, 9, 29, block.GLASS)
mc.setBlocks(-99, 10, 21, -91, 10, 29, block.STONE)
mc.setBlocks(-98, 10, 22, -92, 10, 28, block.LAVA_STATIONARY)
mc.setBlocks(-98, 11, 22, -92, 11, 28, block.STONE)
mc.setBlocks(-97, 12, 23, -93, 12, 27, block.STONE)
mc.setBlocks(-96, 13, 24, -94, 13, 26, block.STONE)
mc.setBlocks(-95, 14, 25, -95, 14, 25, block.STONE)

#HOUSE_16
#SPACE
time.sleep(3)
mc.setBlocks(-105, 0, -5, -86, 30, 14, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(-100, -1, 0, -90, -1, 10, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-100, 0, 0, -90, 8, 10, block.BRICK_BLOCK)
mc.setBlocks(-99, 0, 1, -91, 8, 9, block.AIR)
#WALL_ONE
mc.setBlocks(-98, 1, 0, -97, 2, 0, block.GLASS)
mc.setBlocks(-93, 1, 0, -92, 2, 0, block.GLASS)
mc.setBlocks(-98, 6, 0, -97, 7, 0, block.GLASS)
mc.setBlocks(-93, 6, 0, -92, 7, 0, block.GLASS)
#WALL_TWO
mc.setBlocks(-90, 1, 2, -90, 2, 3, block.GLASS)
mc.setBlocks(-90, 1, 7, -90, 2, 8, block.GLASS)
mc.setBlocks(-90, 6, 2, -90, 7, 3, block.GLASS)
mc.setBlocks(-90, 6, 7, -90, 7, 8, block.GLASS)
mc.setBlocks(-90, 0, 5, -90, 1, 5, block.AIR)
#WALL_THREE
mc.setBlocks(-98, 1, 10, -97, 2, 10, block.GLASS)
mc.setBlocks(-93, 1, 10, -92, 2, 10, block.GLASS)
mc.setBlocks(-98, 6, 10, -97, 7, 10, block.GLASS)
mc.setBlocks(-93, 6, 10, -92, 7, 10, block.GLASS)
#FRONT_WALL
mc.setBlocks(-100, 1, 2, -100, 2, 3, block.GLASS)
mc.setBlocks(-100, 1, 7, -100, 2, 8, block.GLASS)
mc.setBlocks(-100, 6, 2, -100, 7, 3, block.GLASS)
mc.setBlocks(-100, 6, 7, -100, 7, 8, block.GLASS)
#SECOND_FLOOR
mc.setBlocks(-99, 4, 1, -91, 4, 9, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(-95, 4, 5, -92, 4, 5, block.AIR)
mc.setBlock(-96,0,5,block.STAIRS_WOOD)
mc.setBlock(-95,1,5,block.STAIRS_WOOD)
mc.setBlock(-94,2,5,block.STAIRS_WOOD)
mc.setBlock(-93,3,5,block.STAIRS_WOOD)
mc.setBlock(-92,4,5,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(-99, 5, 5, -96, 8, 5, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 1, -95, 8, 4, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 2, -95, 6, 2, block.AIR)
mc.setBlocks(-95, 5, 6, -95, 8, 9, block.WOOD_PLANKS)
mc.setBlocks(-95, 5, 8, -95, 6, 8, block.AIR)
#ROOF
mc.setBlocks(-100, 9, 0, -90, 9, 10, block.STONE)
mc.setBlocks(-99, 9, 1, -91, 9, 9, block.GLASS)
mc.setBlocks(-99, 10, 1, -91, 10, 9, block.STONE)
mc.setBlocks(-98, 10, 2, -92, 10, 8, block.LAVA_STATIONARY)
mc.setBlocks(-98, 11, 2, -92, 11, 8, block.STONE)
mc.setBlocks(-97, 12, 3, -93, 12, 7, block.STONE)
mc.setBlocks(-96, 13, 4, -94, 13, 6, block.STONE)
mc.setBlocks(-95, 14, 5, -95, 14, 5, block.STONE)

#HOUSE_17
#SPACE
time.sleep(3)
mc.setBlocks(-85, 0, -5, -66, 30, 14, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(-80, -1, 0, -70, -1, 10, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-80, 0, 0, -70, 8, 10, block.BRICK_BLOCK)
mc.setBlocks(-79, 0, 1, -71, 8, 9, block.AIR)
#WALL_ONE
mc.setBlocks(-78, 1, 0, -77, 2, 0, block.GLASS)
mc.setBlocks(-73, 1, 0, -72, 2, 0, block.GLASS)
mc.setBlocks(-78, 6, 0, -77, 7, 0, block.GLASS)
mc.setBlocks(-73, 6, 0, -72, 7, 0, block.GLASS)
#WALL_TWO
mc.setBlocks(-70, 1, 2, -70, 2, 3, block.GLASS)
mc.setBlocks(-70, 1, 7, -70, 2, 8, block.GLASS)
mc.setBlocks(-70, 6, 2, -70, 7, 3, block.GLASS)
mc.setBlocks(-70, 6, 7, -70, 7, 8, block.GLASS)
#WALL_THREE
mc.setBlocks(-78, 1, 10, -77, 2, 10, block.GLASS)
mc.setBlocks(-73, 1, 10, -72, 2, 10, block.GLASS)
mc.setBlocks(-78, 6, 10, -77, 7, 10, block.GLASS)
mc.setBlocks(-73, 6, 10, -72, 7, 10, block.GLASS)
mc.setBlocks(-75, 0, 10, -75, 1, 10, block.AIR)
#FRONT_WALL
mc.setBlocks(-80, 1, 2, -80, 2, 3, block.GLASS)
mc.setBlocks(-80, 1, 7, -80, 2, 8, block.GLASS)
mc.setBlocks(-80, 6, 2, -80, 7, 3, block.GLASS)
mc.setBlocks(-80, 6, 7, -80, 7, 8, block.GLASS)
#SECOND_FLOOR
mc.setBlocks(-79, 4, 1, -71, 4, 9, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(-75, 4, 5, -72, 4, 5, block.AIR)
mc.setBlock(-76,0,5,block.STAIRS_WOOD)
mc.setBlock(-75,1,5,block.STAIRS_WOOD)
mc.setBlock(-74,2,5,block.STAIRS_WOOD)
mc.setBlock(-73,3,5,block.STAIRS_WOOD)
mc.setBlock(-72,4,5,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(-79, 5, 5, -76, 8, 5, block.WOOD_PLANKS)
mc.setBlocks(-75, 5, 1, -75, 8, 4, block.WOOD_PLANKS)
mc.setBlocks(-75, 5, 2, -75, 6, 2, block.AIR)
mc.setBlocks(-75, 5, 6, -75, 8, 9, block.WOOD_PLANKS)
mc.setBlocks(-75, 5, 8, -75, 6, 8, block.AIR)
#ROOF
mc.setBlocks(-80, 9, 0, -70, 9, 10, block.STONE)
mc.setBlocks(-79, 9, 1, -71, 9, 9, block.GLASS)
mc.setBlocks(-79, 10, 1, -71, 10, 9, block.STONE)
mc.setBlocks(-78, 10, 2, -72, 10, 8, block.LAVA_STATIONARY)
mc.setBlocks(-78, 11, 2, -72, 11, 8, block.STONE)
mc.setBlocks(-77, 12, 3, -73, 12, 7, block.STONE)
mc.setBlocks(-76, 13, 4, -74, 13, 6, block.STONE)
mc.setBlocks(-75, 14, 5, -75, 14, 5, block.STONE)

#HOUSE_18
#SPACE
time.sleep(3)
mc.setBlocks(-65, 0, -5, -46, 30, 14, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(-60, -1, 0, -50, -1, 10, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-60, 0, 0, -50, 8, 10, block.BRICK_BLOCK)
mc.setBlocks(-59, 0, 1, -51, 8, 9, block.AIR)
#WALL_ONE
mc.setBlocks(-58, 1, 0, -57, 2, 0, block.GLASS)
mc.setBlocks(-53, 1, 0, -52, 2, 0, block.GLASS)
mc.setBlocks(-58, 6, 0, -57, 7, 0, block.GLASS)
mc.setBlocks(-53, 6, 0, -52, 7, 0, block.GLASS)
#WALL_TWO
mc.setBlocks(-50, 1, 2, -50, 2, 3, block.GLASS)
mc.setBlocks(-50, 1, 7, -50, 2, 8, block.GLASS)
mc.setBlocks(-50, 6, 2, -50, 7, 3, block.GLASS)
mc.setBlocks(-50, 6, 7, -50, 7, 8, block.GLASS)
#WALL_THREE
mc.setBlocks(-58, 1, 10, -57, 2, 10, block.GLASS)
mc.setBlocks(-53, 1, 10, -52, 2, 10, block.GLASS)
mc.setBlocks(-58, 6, 10, -57, 7, 10, block.GLASS)
mc.setBlocks(-53, 6, 10, -52, 7, 10, block.GLASS)
mc.setBlocks(-55, 0, 10, -55, 1, 10, block.AIR)
#FRONT_WALL
mc.setBlocks(-60, 1, 2, -60, 2, 3, block.GLASS)
mc.setBlocks(-60, 1, 7, -60, 2, 8, block.GLASS)
mc.setBlocks(-60, 6, 2, -60, 7, 3, block.GLASS)
mc.setBlocks(-60, 6, 7, -60, 7, 8, block.GLASS)
#SECOND_FLOOR
mc.setBlocks(-59, 4, 1, -51, 4, 9, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(-55, 4, 5, -52, 4, 5, block.AIR)
mc.setBlock(-56,0,5,block.STAIRS_WOOD)
mc.setBlock(-55,1,5,block.STAIRS_WOOD)
mc.setBlock(-54,2,5,block.STAIRS_WOOD)
mc.setBlock(-53,3,5,block.STAIRS_WOOD)
mc.setBlock(-52,4,5,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(-59, 5, 5, -56, 8, 5, block.WOOD_PLANKS)
mc.setBlocks(-55, 5, 1, -55, 8, 4, block.WOOD_PLANKS)
mc.setBlocks(-55, 5, 2, -55, 6, 2, block.AIR)
mc.setBlocks(-55, 5, 6, -55, 8, 9, block.WOOD_PLANKS)
mc.setBlocks(-55, 5, 8, -55, 6, 8, block.AIR)
#ROOF
mc.setBlocks(-60, 9, 0, -50, 9, 10, block.STONE)
mc.setBlocks(-59, 9, 1, -51, 9, 9, block.GLASS)
mc.setBlocks(-59, 10, 1, -51, 10, 9, block.STONE)
mc.setBlocks(-58, 10, 2, -52, 10, 8, block.LAVA_STATIONARY)
mc.setBlocks(-58, 11, 2, -52, 11, 8, block.STONE)
mc.setBlocks(-57, 12, 3, -53, 12, 7, block.STONE)
mc.setBlocks(-56, 13, 4, -54, 13, 6, block.STONE)
mc.setBlocks(-55, 14, 5, -55, 14, 5, block.STONE)

#HOUSE_19
#SPACE
time.sleep(3)
mc.setBlocks(-45, 0, -5, -26, 30, 14, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(-40, -1, 0, -30, -1, 10, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-40, 0, 0, -30, 8, 10, block.BRICK_BLOCK)
mc.setBlocks(-39, 0, 1, -31, 8, 9, block.AIR)
#WALL_ONE
mc.setBlocks(-38, 1, 0, -37, 2, 0, block.GLASS)
mc.setBlocks(-33, 1, 0, -32, 2, 0, block.GLASS)
mc.setBlocks(-38, 6, 0, -37, 7, 0, block.GLASS)
mc.setBlocks(-33, 6, 0, -32, 7, 0, block.GLASS)
#WALL_TWO
mc.setBlocks(-30, 1, 2, -30, 2, 3, block.GLASS)
mc.setBlocks(-30, 1, 7, -30, 2, 8, block.GLASS)
mc.setBlocks(-30, 6, 2, -30, 7, 3, block.GLASS)
mc.setBlocks(-30, 6, 7, -30, 7, 8, block.GLASS)
#WALL_THREE
mc.setBlocks(-38, 1, 10, -37, 2, 10, block.GLASS)
mc.setBlocks(-33, 1, 10, -32, 2, 10, block.GLASS)
mc.setBlocks(-38, 6, 10, -37, 7, 10, block.GLASS)
mc.setBlocks(-33, 6, 10, -32, 7, 10, block.GLASS)
mc.setBlocks(-35, 0, 10, -35, 1, 10, block.AIR)
#FRONT_WALL
mc.setBlocks(-40, 1, 2, -40, 2, 3, block.GLASS)
mc.setBlocks(-40, 1, 7, -40, 2, 8, block.GLASS)
mc.setBlocks(-40, 6, 2, -40, 7, 3, block.GLASS)
mc.setBlocks(-40, 6, 7, -40, 7, 8, block.GLASS)
#SECOND_FLOOR
mc.setBlocks(-39, 4, 1, -31, 4, 9, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(-35, 4, 5, -32, 4, 5, block.AIR)
mc.setBlock(-36,0,5,block.STAIRS_WOOD)
mc.setBlock(-35,1,5,block.STAIRS_WOOD)
mc.setBlock(-34,2,5,block.STAIRS_WOOD)
mc.setBlock(-33,3,5,block.STAIRS_WOOD)
mc.setBlock(-32,4,5,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(-39, 5, 5, -36, 8, 5, block.WOOD_PLANKS)
mc.setBlocks(-35, 5, 1, -35, 8, 4, block.WOOD_PLANKS)
mc.setBlocks(-35, 5, 2, -35, 6, 2, block.AIR)
mc.setBlocks(-35, 5, 6, -35, 8, 9, block.WOOD_PLANKS)
mc.setBlocks(-35, 5, 8, -35, 6, 8, block.AIR)
#ROOF
mc.setBlocks(-40, 9, 0, -30, 9, 10, block.STONE)
mc.setBlocks(-39, 9, 1, -31, 9, 9, block.GLASS)
mc.setBlocks(-39, 10, 1, -31, 10, 9, block.STONE)
mc.setBlocks(-38, 10, 2, -32, 10, 8, block.LAVA_STATIONARY)
mc.setBlocks(-38, 11, 2, -32, 11, 8, block.STONE)
mc.setBlocks(-37, 12, 3, -33, 12, 7, block.STONE)
mc.setBlocks(-36, 13, 4, -34, 13, 6, block.STONE)
mc.setBlocks(-35, 14, 5, -35, 14, 5, block.STONE)

#HOUSE_20
#SPACE
time.sleep(3)
mc.setBlocks(-25, 0, -5, -6, 30, 14, block.AIR)
mc.postToChat("House")
#OUTLINE
mc.setBlocks(-20, -1, 0, -10, -1, 10, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-20, 0, 0, -10, 8, 10, block.BRICK_BLOCK)
mc.setBlocks(-19, 0, 1, -11, 8, 9, block.AIR)
#WALL_ONE
mc.setBlocks(-18, 1, 0, -17, 2, 0, block.GLASS)
mc.setBlocks(-13, 1, 0, -12, 2, 0, block.GLASS)
mc.setBlocks(-18, 6, 0, -17, 7, 0, block.GLASS)
mc.setBlocks(-13, 6, 0, -12, 7, 0, block.GLASS)
#WALL_TWO
mc.setBlocks(-10, 1, 2, -10, 2, 3, block.GLASS)
mc.setBlocks(-10, 1, 7, -10, 2, 8, block.GLASS)
mc.setBlocks(-10, 6, 2, -10, 7, 3, block.GLASS)
mc.setBlocks(-10, 6, 7, -10, 7, 8, block.GLASS)
#WALL_THREE
mc.setBlocks(-18, 1, 10, -17, 2, 10, block.GLASS)
mc.setBlocks(-13, 1, 10, -12, 2, 10, block.GLASS)
mc.setBlocks(-18, 6, 10, -17, 7, 10, block.GLASS)
mc.setBlocks(-13, 6, 10, -12, 7, 10, block.GLASS)
mc.setBlocks(-15, 0, 10, -15, 1, 10, block.AIR)
#FRONT_WALL
mc.setBlocks(-20, 1, 2, -20, 2, 3, block.GLASS)
mc.setBlocks(-20, 1, 7, -20, 2, 8, block.GLASS)
mc.setBlocks(-20, 6, 2, -20, 7, 3, block.GLASS)
mc.setBlocks(-20, 6, 7, -20, 7, 8, block.GLASS)
#SECOND_FLOOR
mc.setBlocks(-19, 4, 1, -11, 4, 9, block.WOOD_PLANKS)
#STAIRCASE
mc.setBlocks(-15, 4, 5, -12, 4, 5, block.AIR)
mc.setBlock(-16,0,5,block.STAIRS_WOOD)
mc.setBlock(-15,1,5,block.STAIRS_WOOD)
mc.setBlock(-14,2,5,block.STAIRS_WOOD)
mc.setBlock(-13,3,5,block.STAIRS_WOOD)
mc.setBlock(-12,4,5,block.STAIRS_WOOD)
#UPSTAIRS_BEDROOMS
mc.setBlocks(-19, 5, 5, -16, 8, 5, block.WOOD_PLANKS)
mc.setBlocks(-15, 5, 1, -15, 8, 4, block.WOOD_PLANKS)
mc.setBlocks(-15, 5, 2, -15, 6, 2, block.AIR)
mc.setBlocks(-15, 5, 6, -15, 8, 9, block.WOOD_PLANKS)
mc.setBlocks(-15, 5, 8, -15, 6, 8, block.AIR)
#ROOF
mc.setBlocks(-20, 9, 0, -10, 9, 10, block.STONE)
mc.setBlocks(-19, 9, 1, -11, 9, 9, block.GLASS)
mc.setBlocks(-19, 10, 1, -11, 10, 9, block.STONE)
mc.setBlocks(-18, 10, 2, -12, 10, 8, block.LAVA_STATIONARY)
mc.setBlocks(-18, 11, 2, -12, 11, 8, block.STONE)
mc.setBlocks(-17, 12, 3, -13, 12, 7, block.STONE)
mc.setBlocks(-16, 13, 4, -14, 13, 6, block.STONE)
mc.setBlocks(-15, 14, 5, -15, 14, 5, block.STONE)

#ROAD
time.sleep(20)
mc.postToChat("Road")
#CLEARANCE
mc.setBlocks(-88, -1, 11, -1, 50, 16, block.AIR)
mc.setBlocks(-6, -1, 11, -1, 50, 99, block.AIR)
mc.setBlocks(-88, -1, 94, -1, 50, 99, block.AIR)
mc.setBlocks(-89, -1, 11, -84, 50, 99, block.AIR)
#COBBLESTONE
mc.setBlocks(-88, -1, 11, -1, -1, 16, block.COBBLESTONE)
mc.setBlocks(-6, -1, 11, -1, -1, 99, block.COBBLESTONE)
mc.setBlocks(-88, -1, 94, -1, -1, 99, block.COBBLESTONE)
mc.setBlocks(-89, -1, 11, -84, -1, 99, block.COBBLESTONE)
#PAVEMENT
mc.setBlocks(-88, -1, 11, -1, -1, 11, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-1, -1, 11, -1, -1, 99, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-88, -1, 99, -1, -1, 99, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-89, -1, 11, -89, -1, 99, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-84, -1, 16, -6, -1, 16, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-6, -1, 16, -6, -1, 94, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-84, -1, 94, -6, -1, 94, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-84, -1, 16, -84, -1, 94, block.STONE_SLAB_DOUBLE)
#CONNECTING_PAVEMENTS
mc.setBlocks(-1, -1, 100, -1, -1, 105, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-89, -1, 99, -95, -1, 99, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-89, -1, 5, -89, -1, 11, block.STONE_SLAB_DOUBLE)
mc.setBlocks( -1, -1, 5, -1, -1, 11, block.STONE_SLAB_DOUBLE)

#GOVT_BUILIDING
time.sleep(20)
mc.postToChat("Government Builiding Constructed")
#SPACE
mc.setBlocks(-50, 0, 46, -3, 50, 65, block.AIR)
#OUTLINE
mc.setBlocks(-44, -1, 46, -7, -1, 65, block.COBBLESTONE)
mc.setBlocks(-22, 0, 49, -37, 17, 62, block.STONE)
#FRONT_WALL
#DOOR
mc.setBlocks(-22, 0, 57, -22, 4, 57, block.SNOW_BLOCK)
mc.setBlocks(-22, 4, 55, -22, 4, 56, block.SNOW_BLOCK)
mc.setBlocks(-22, 0, 54, -22, 4, 54, block.SNOW_BLOCK)
#WINDOWS
mc.setBlocks(-22, 1, 50, -22, 4, 51, block.GLASS)
mc.setBlocks(-22, 7, 50, -22, 10, 51, block.GLASS)
mc.setBlocks(-22, 13, 50, -22, 16, 51, block.GLASS)
mc.setBlocks(-22, 7, 55, -22, 10, 56, block.GLASS)
mc.setBlocks(-22, 13, 55, -22, 16, 56, block.GLASS)
mc.setBlocks(-22, 1, 60, -22, 4, 61, block.GLASS)
mc.setBlocks(-22, 7, 60, -22, 10, 61, block.GLASS)
mc.setBlocks(-22, 13, 60, -22, 16, 61, block.GLASS)
#ROOF
mc.setBlocks(-22, 18, 49, -37, 18, 62, block.SNOW_BLOCK)
#DRIVE
mc.setBlocks(-6, -1, 56, -21, -1, 55, block.COBBLESTONE)
mc.setBlocks(-7, -1, 54, -21, -1, 54, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-7, -1, 57, -21, -1, 57, block.STONE_SLAB_DOUBLE)
#WALL
#FRONT
def loop(c,d):
    while c < 18:
        c=c+2
        z=c+44
        mc.setBlock(-7,0,z,block.STONE)
loop(1, 2)
def loop(c,d):
    while c < 18:
        c=c+2
        z=c+45
        mc.setBlock(-7,1,z,block.STONE)
loop(1, 2)
def loop(c,d):
    while c < 18:
        c=c+2
        z=c+44
        mc.setBlock(-7,2,z,block.STONE)
loop(1, 2)
#WALL_ONE
def loop(c,d):
    while c > -34:
        c=c-2
        x=c-7
        mc.setBlock(x,0,65,block.STONE)
loop(1, 2)
def loop(c,d):
    while c > -34:
        c=c-2
        x=c-8
        mc.setBlock(x,1,65,block.STONE)
loop(1, 2)
def loop(c,d):
    while c > -34:
        c=c-2
        x=c-7
        mc.setBlock(x,2,65,block.STONE)
loop(1, 2)
#WALL_TWO
def loop(c,d):
    while c < 18:
        c=c+2
        z=c+44
        mc.setBlock(-44,0,z,block.STONE)
loop(1, 2)
def loop(c,d):
    while c < 18:
        c=c+2
        z=c+45
        mc.setBlock(-44,1,z,block.STONE)
loop(1, 2)
def loop(c,d):
    while c < 18:
        c=c+2
        z=c+44
        mc.setBlock(-44,2,z,block.STONE)
loop(1, 2)
#WALL_THREE
def loop(c,d):
    while c > -34:
        c=c-2
        x=c-7
        mc.setBlock(x,0,46,block.STONE)
loop(1, 2)
def loop(c,d):
    while c > -34:
        c=c-2
        x=c-8
        mc.setBlock(x,1,46,block.STONE)
loop(1, 2)
def loop(c,d):
    while c > -34:
        c=c-2
        x=c-7
        mc.setBlock(x,2,46,block.STONE)
loop(1, 2)
#CORNERS
mc.setBlocks(-7, 0, 65, -7, 2, 65, block.STONE)
mc.setBlocks(-44, 0, 65, -44, 2, 65, block.STONE)
mc.setBlocks(-44, 0, 46, -44, 2, 46, block.STONE)
mc.setBlocks(-7, 0, 46, -7, 2, 46, block.STONE)
#ENTRANCE
mc.setBlocks(-7,2,57, -7,0,54, block.AIR)
mc.setBlocks(-7, 0, 58, -7, 2, 58, block.STONE)
mc.setBlocks(-7, 0, 53, -7, 2, 53, block.STONE)

#TOBACCO_SHACK
time.sleep(20)
mc.postToChat("Tobacco Store Established")
#CLEARANCE
mc.setBlocks(-13, 0, 29, -4, 30, 41, block.AIR)
#FLOOR
mc.setBlocks(-10, -1, 32, -7, -1, 38, block.WOOD_PLANKS)
#BUILDING
mc.setBlocks(-10, 0, 32, -7, 2, 32, block.WOOD_PLANKS)
mc.setBlocks(-10, 0, 38, -7, 2, 38, block.WOOD_PLANKS)
mc.setBlocks(-10, 0, 33, -10, 2, 37, block.WOOD_PLANKS)
mc.setBlocks(-7, 2, 33, -9, 2, 37, block.WOOD_PLANKS)
mc.setBlocks(-7, 0, 34, -7, 0, 36, block.WOOD_PLANKS)
#CIGARETTE_POSTS
mc.setBlocks(-6, 0, 32, -6, 1, 32, block.DIRT)
mc.setBlocks(-6, 0, 38, -6, 1, 38, block.DIRT)
mc.setBlocks(-6, 2, 32, -6, 3, 32, block.SNOW_BLOCK)
mc.setBlocks(-6, 2, 38, -6, 3, 38, block.SNOW_BLOCK)
mc.setBlocks(-6, 4, 32, -6, 4, 32, block.LAVA_STATIONARY)
mc.setBlocks(-6, 4, 38, -6, 4, 38, block.LAVA_STATIONARY)

#DOCTORS
time.sleep(30)
mc.postToChat("Doctors Surgery Created")
mc.setBlocks(-84,0,46,-64,30,68,block.AIR)
#OUTLINE
mc.setBlocks(-79, -1, 53, -69, -1, 63, block.SNOW_BLOCK)
mc.setBlocks(-79, 0, 53, -69, 3, 63, block.SNOW_BLOCK)
mc.setBlocks(-78, 0, 54, -70, 3, 62, block.AIR)
#ROOF
mc.setBlocks(-79, 4, 53, -69, 4, 63, block.SNOW_BLOCK)
mc.setBlocks(-70, 4, 57, -78, 4, 59, block.WOOL.id, 14)
mc.setBlocks(-73, 4, 54, -75, 4, 62, block.WOOL.id, 14)
#WINDOWS/DOOR
mc.setBlocks(-79, 0, 58, -79, 1, 58, block.AIR)
mc.setBlocks(-79, 1, 60, -79, 2, 61, block.GLASS)
mc.setBlocks(-79, 1, 55, -79, 2, 56, block.GLASS)
mc.setBlocks(-71, 1, 53, -72, 2, 53, block.GLASS)
mc.setBlocks(-77, 1, 53, -76, 2, 53, block.GLASS)
mc.setBlocks(-71, 1, 63, -72, 2, 63, block.GLASS)
mc.setBlocks(-77, 1, 63, -76, 2, 63, block.GLASS)
mc.setBlocks(-69, 1, 60, -69, 2, 61, block.GLASS)
mc.setBlocks(-69, 1, 55, -69, 2, 56, block.GLASS)
#PATH
mc.setBlocks(-80, -1, 58, -84, -1, 58, block.COBBLESTONE)
mc.setBlocks(-80, -1, 57, -83, -1, 57, block.STONE_SLAB_DOUBLE)
mc.setBlocks(-80, -1, 59, -83, -1, 59, block.STONE_SLAB_DOUBLE)

#FOOTBALL_PITCH
time.sleep(15)
mc.postToChat("Football Pitch")
mc.setBlocks(-83, 0, 17, -39, 30, 45, block.AIR)
mc.setBlocks(-83, -1, 17, -39, -1, 45, block.COBBLESTONE)
#GOALS
mc.setBlocks(-76, 0, 34, -76, 2, 29, block.SNOW_BLOCK)
mc.setBlocks(-76, 0, 33, -76, 1, 30, block.AIR)
mc.setBlocks(-45, 0, 34, -45, 2, 29, block.SNOW_BLOCK)
mc.setBlocks(-45, 0, 33, -45, 1, 30, block.AIR)
#LINES
mc.setBlocks(-76, -1, 24, -45, -1, 39, block.SNOW_BLOCK)
mc.setBlocks(-75, -1, 25, -46, -1, 38, block.GRASS)
mc.setBlocks(-61, -1, 24, -61, -1, 38, block.SNOW_BLOCK)
mc.setBlocks(-63, -1, 33, -59, -1, 29, block.SNOW_BLOCK)
mc.setBlocks(-60, -1, 32, -60, -1, 30, block.GRASS)
mc.setBlocks(-62, -1, 32, -62, -1, 30, block.GRASS)
mc.setBlocks(-46, -1, 36, -50, -1, 27, block.SNOW_BLOCK)
mc.setBlocks(-46, -1, 35, -49, -1, 28, block.GRASS)
mc.setBlocks(-75, -1, 36, -72, -1, 27, block.SNOW_BLOCK)
mc.setBlocks(-75, -1, 35, -73, -1, 28, block.GRASS)
#STAND_1
def loop(c,d):
    x=-77
    while c < 4:
        c=c+1
        y=c
        x=x-1
        a=x-1
        mc.setBlocks(x, y, 24, a, y, 39, block.STONE)      
loop(-1, 2)
#STAND_2
def loop(c,d):
    z=23
    while c < 4:
        c=c+1
        y=c
        z=z-1
        a=z-1
        mc.setBlocks(-76, y, z, -45, y, a, block.STONE)      
loop(-1, 2)
#STAND_3
def loop(c,d):
    x=-44
    while c < 4:
        c=c+1
        y=c
        x=x+1
        a=x+1
        mc.setBlocks(x, y, 24, a, y, 39, block.STONE)      
loop(-1, 2)
#STAND_4
def loop(c,d):
    z=40
    while c < 4:
        c=c+1
        y=c
        z=z+1
        a=z+1
        mc.setBlocks(-76, y, z, -45, y, a, block.STONE)      
loop(-1, 2)

#PYRAMID
time.sleep(15)
mc.postToChat("Pyramid")
mc.setBlocks(-38, 0, 17, -11, 30, 45, block.AIR)
def loop(c,d):
    x=-39
    z=17
    a=-11
    b=45
    while c < 13:
        c=c+1
        y=c
        x=x+1
        z=z+1
        a=a-1
        b=b-1
        mc.setBlocks(x, y, z, a, y, b, block.SANDSTONE)      
loop(-1, 2)

#PARK
time.sleep(20)
mc.postToChat("Park")
mc.setBlocks(-7, 0, 66, -65 , 40, 93, block.AIR)
#GRASS
mc.setBlocks(-7, -1, 66, -60 , -1, 93, block.GRASS)
#LOGO
mc.setBlocks(-58, -1, 68, -17 , -1, 73, block.WATER_STATIONARY)
mc.setBlocks(-58, -1, 69, -57 , -1, 72, block.GRASS)
mc.setBlocks(-55, -1, 69, -54 , -1, 72, block.GRASS)
mc.setBlocks(-53, -1, 68, -53 , -1, 72, block.GRASS)
mc.setBlocks(-51, -1, 68, -51 , -1, 72, block.GRASS)
mc.setBlocks(-49, -1, 69, -49 , -1, 72, block.GRASS)
mc.setBlocks(-47, -1, 69, -47 , -1, 72, block.GRASS)
mc.setBlocks(-45, -1, 68, -45 , -1, 72, block.GRASS)
mc.setBlocks(-43, -1, 68, -43 , -1, 69, block.GRASS)
mc.setBlocks(-43, -1, 71, -43 , -1, 72, block.GRASS)
mc.setBlock(-42, -1, 70,block.GRASS)
mc.setBlocks(-41, -1, 68, -41 , -1, 72, block.GRASS)
mc.setBlocks(-39, -1, 69, -38 , -1, 69, block.GRASS)
mc.setBlocks(-39, -1, 71, -38 , -1, 71, block.GRASS)
mc.setBlocks(-37, -1, 68, -37 , -1, 72, block.GRASS)
mc.setBlock(-35, -1, 69,block.GRASS)
mc.setBlocks(-35, -1, 71, -35 , -1, 72, block.GRASS)
mc.setBlock(-34, -1, 72,block.GRASS)
mc.setBlocks(-33, -1, 68, -33 , -1, 70, block.GRASS)
mc.setBlocks(-32, -1, 68, -32 , -1, 72, block.GRASS)
mc.setBlocks(-31, -1, 69, -30 , -1, 72, block.GRASS)
mc.setBlocks(-28, -1, 69, -27 , -1, 72, block.GRASS)
mc.setBlocks(-26, -1, 68, -26 , -1, 72, block.GRASS)
mc.setBlocks(-24, -1, 68, -24 , -1, 71, block.GRASS)
mc.setBlocks(-22, -1, 68, -22 , -1, 71, block.GRASS)
mc.setBlocks(-20, -1, 68, -20 , -1, 72, block.GRASS)
mc.setBlocks(-18, -1, 69, -18 , -1, 71, block.GRASS)

#WATER_FALL
mc.setBlocks(-61, 0, 72, -62, 2, 74, block.STONE)
mc.setBlocks(-61, 0, 73, -61, 1, 73, block.AIR)
mc.setBlocks(-60, -1, 73, -58 , -1, 73, block.WATER_STATIONARY)
mc.setBlock(-61,0,73, block.WATER_STATIONARY)
mc.setBlock(-61,1,73, block.WATER_FLOWING)

#LAKE
def loop(c,d):
    x=-58
    z=84
    b=85
    while c < 6:
        c=c+1
        x=x+2
        z=z-1
        b=b+1
        mc.setBlocks(x, -1, z, x+1, -1, b, block.WATER_STATIONARY)      
loop(-1, 2)
mc.setBlocks(-42,-1,92, -23,-1,77,block.WATER_STATIONARY)
def loop(c,d):
    x=-24
    b=93
    z=76
    while c < 6:
        c=c+1
        x=x+2
        z=z+1
        b=b-1
        mc.setBlocks(x, -1, z, x+1, -1, b, block.WATER_STATIONARY)      
loop(-1, 2)

#VOLCANO
time.sleep(25)
mc.postToChat("Giant Square Volcano")
mc.setBlocks(-66 ,0, 69, -83, 40, 93, block.AIR)
def loop(c,d):
    x=-83
    z=73
    a=-63
    b=93
    f=2
    while c < 16:
        c=c+3
        f=f+1
        y=f*f
        x=x+1
        z=z+1
        a=a-1
        b=b-1
        mc.setBlocks(x, y, z, a, 0, b, block.BEDROCK)      
loop(-1, 2)
mc.setBlocks(-70,63,80,-76,53,86,block.AIR)
mc.setBlocks(-70,53,80,-76,50,86,block.LAVA_STATIONARY)

#TOBACCO_STORE_MELT
time.sleep(25)
mc.postToChat("Tobacco Store has been melted down")
mc.postToChat("by its own cigarettes... Shame")
mc.setBlocks(-6, 3, 32, -6, 3, 32, block.AIR)
mc.setBlocks(-6, 3, 38, -6, 3, 38, block.AIR)
time.sleep(20)
mc.postToChat("Find 'Timker 2' at www.timkering.co.uk where there's more information")
mc.postToChat("on how this world was created (including the source code).")
time.sleep(15)
mc.postToChat("There's also information on the Raspberry Pi and much more")
time.sleep(15)
mc.postToChat("'Like' Timkering on Facebook via the button at")
mc.postToChat("www.timkering.co.uk, where you can vote if you'd like me to write a code to make the Volcano erupt")
time.sleep(15)
mc.postToChat("You can follow Timkering on twitter @timkering")
time.sleep(15)
mc.postToChat("Thanks for watching")
time.sleep(30)
