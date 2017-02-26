#!/usr/bin/env python

import minecraft.minecraft as minecraft
import minecraft.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

y = pos.y
x = pos.x
z = pos.z

height = 63

for y in xrange(y, height):
    x = x + 1
    mc.setBlock(x, y, z, block.MELON)
