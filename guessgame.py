#! /usr/bin/env python

import minecraft.minecraft as minecraft
import minecraft.block as block
import random
import time

mc = minecraft.Minecraft.create()

playerx, playery, playerz = mc.player.getTilePos()

y = playery + 1
mc.setBlocks(playerx + 1, playery + 3, playerz + 1, playerx - 1, playery, playerz - 1, block.AIR)
mc.setBlock(playerx, playery, playerz, block.GRASS)
mc.setBlocks(playerx + 1, y, playerz + 1, playerx - 1, y, playerz - 1, block.TNT)
mc.player.setTilePos(playerx, playery + 2, playerz)

xvalues = [playerx - 1, playerx, playerx + 1]
zvalues = [playerz - 1, playerz, playerz + 1]

tntx = random.choice(xvalues)
tntz = random.choice(zvalues)

xvalues.remove(tntx)
zvalues.remove(tntz)
xvalues = xvalues + [tntx]
zvalues = zvalues + [tntz]

mc.setBlock(tntx, y, tntz, block.TNT.id, 1)

mc.postToChat('Try to break all the TNT except the explosive TNT!')
mc.postToChat('Break the grass block when you succeed')

def check():
	for xint in range(0,3):
		for zint in range(0,3):
			if mc.getBlockWithData(xvalues[xint], y, zvalues[zint]) == block.TNT:
				mc.setBlock(playerx, playery, playerz, block.GRASS)
				mc.postToChat('Break all other blocks first.')
				return
			elif str(mc.getBlockWithData(xvalues[xint], y, zvalues[zint])) == 'Block(46, 1)':
				mc.postToChat('You succeeded!')
				mc.setBlock(tntx, y, tntz, block.AIR.id, 1)
				print xint; print playerx; print tntx; print zint; print playerz; print tntz
				exit()

while True:
	if mc.getBlock(playerx, playery, playerz) == block.AIR.id: #if grass block destroyed do this
		if mc.getBlockWithData(tntx, y, tntz) == block.AIR:
			mc.postToChat('You failed!')
			exit()
		else:
			check()


