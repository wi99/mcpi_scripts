#! /usr/bin/env python

"""
Infinite TNT Source
An infinite amount of explosive TNT.
"""

import minecraft.minecraft as minecraft
import minecraft.block as block
import random
import time

mc = minecraft.Minecraft.create()

playerx, playery, playerz = mc.player.getTilePos()

mc.postToChat('Infinite TNT')
mc.setBlock(playerx, playery, playerz, block.TNT.id, 1)

while True:
	if mc.getBlock(playerx, playery, playerz) == block.AIR.id:
		mc.setBlock(playerx, playery, playerz, block.TNT.id, 1)

