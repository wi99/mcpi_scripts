#! /usr/bin/env python

import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import random

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--single', '-s', help='Use a single block instead of default: all.\nChoose: snow, torch, flower_yellow, flower_cyan, mushroom_brown, mushroom_red')
args = parser.parse_args()

mc = minecraft.Minecraft.create()

def six():
	nonsolids = [block.SNOW, block.TORCH, block.FLOWER_YELLOW, block.FLOWER_CYAN, block.MUSHROOM_BROWN, block.MUSHROOM_RED]
	while True:
		x, y, z = mc.player.getTilePos()
		time.sleep(0.1)
		if mc.getBlock(x, y, z) == block.AIR and mc.getBlock(x, y - 1, z) != block.AIR:
			mc.setBlock(x, y, z, random.choice(nonsolids))

def one():
	nonsolids = {'SNOW': 78, 'TORCH': 50, 'FLOWER_YELLOW': 37, 'FLOWER_CYAN': 38, 'MUSHROOM_BROWN': 39, 'MUSHROOM_RED': 40}
	nonsolid = args.single
	nonsolid = nonsolid.upper()
	nonsolid = nonsolids[nonsolid]
	while True:
		x, y, z = mc.player.getTilePos()
		time.sleep(0.1)
		if mc.getBlock(x, y, z) == block.AIR and mc.getBlock(x, y - 1, z) != block.AIR:
			mc.setBlock(x, y, z, nonsolid)

if __name__ == '__main__':
	if args.single == None:
		six()
	else:
		one()
