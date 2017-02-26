#! /usr/bin/env python

import minecraft.minecraft as minecraft
import time

mc = minecraft.Minecraft.create();

mc.postToChat('x,y,z,block,data')
print 'x,y,z,block,data'

while True:
	hits = mc.events.pollBlockHits()
	for hit in hits:
		block, data = mc.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z)
		text = str(hit.pos.x) + ',' + str(hit.pos.y) + ',' + str(hit.pos.z) + ',' + str(block) + ',' + str(data)
		mc.postToChat(text)
		print text
	time.sleep(0.1)
