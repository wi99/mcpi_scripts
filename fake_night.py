#! /usr/bin/env python

import minecraft.minecraft as minecraft
import minecraft.block as block

mc = minecraft.Minecraft.create()

#mc.setBlocks(-128,63,-128, 127,63,127, block.LEAVES):
#Sky coordinates differ in different worlds
mc.setBlocks(-160,60,-160, 160,60,160, block.LEAVES)
