#!/usr/bin/env python

import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import random
import sys
import os

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

def random_sb():
    x = random.randint(0, 6)
    z = random.randint(0, 8)
    mc.setBlock(spos.x+x, spos.y+10, spos.z+z, block.SAND)

def make_field():
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x+1, pos.y-1, pos.z-4, pos.x+7, pos.y-1, pos.z+4, block.COBBLESTONE)
    mc.setBlocks(pos.x, pos.y, pos.z-5, pos.x+8, pos.y, pos.z+5, block.COBBLESTONE)
    mc.setBlocks(pos.x, pos.y+1, pos.z-5, pos.x+8, pos.y+1, pos.z+5, block.COBBLESTONE)
    mc.setBlocks(pos.x+1, pos.y+1, pos.z-4, pos.x+7, pos.y+1, pos.z+4, block.AIR)
    mc.player.setTilePos(pos.x+1, pos.y, pos.z-4)

def clear_Field():
    mc.setBlocks(spos.x, spos.y, spos.z, spos.x+6, spos.y, spos.z+8, block.AIR)

def check():
    if mc.getBlock(fpos.x, fpos.y, fpos.z) == block.SAND.id:
        mc.postToChat("you lose it took " + str(int(time.time() - start)) + " seconds")
        mc.player.setTilePos(spos.x-3, spos.y, spos.z+4)
        mc.player.setPos(pos.x, pos.y, pos.z)
        raise SystemExit

make_field()

spos = mc.player.getTilePos()

start = time.time()

mc.player.setTilePos(spos.x, spos.y, spos.z)

while(True):
    fpos = mc.player.getTilePos()
    random_sb()
    check()
    clear_Field()
    time.sleep(0.1)



    
