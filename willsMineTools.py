#!/usr/bin/python

'''
William's Mine Tools
'''

__author__ = 'William Situ'

import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import Tkinter as tk


def up():
	global xPos, zPos, defaultHeight, height
	pos = xPos, mc.getHeight(xPos,zPos) + height, zPos + 1
	mc.camera.setPos(pos)
	xPos, yPos, zPos = pos
def left():
	global xPos, zPos, defaultHeight, height
	pos = xPos + 1, mc.getHeight(xPos,zPos) + height, zPos
	mc.camera.setPos(pos)
	xPos, yPos, zPos = pos
def down():
	global xPos, zPos, defaultHeight, height
	pos = xPos, mc.getHeight(xPos,zPos) + height, zPos - 1
	mc.camera.setPos(pos)
	xPos, yPos, zPos = pos
def right():
	global xPos, zPos, defaultHeight, height
	pos = xPos - 1, mc.getHeight(xPos,zPos) + height, zPos
	mc.camera.setPos(pos)
	xPos, yPos, zPos = pos

def zoomOut():
	global xPos, zPos, defaultHeight, height
	height = height + 1
	pos = xPos, mc.getHeight(xPos,zPos) + height, zPos
	mc.camera.setPos(pos)
def zoomIn():
	global xPos, zPos, defaultHeight, height
	height = height - 1
	pos = xPos, mc.getHeight(xPos,zPos) + height, zPos
	mc.camera.setPos(pos)
def zoomDefault():
	global xPos, zPos, defaultHeight, height
	height = defaultHeight
	pos = xPos, mc.getHeight(xPos,zPos) + height, zPos
	mc.camera.setPos(pos)

def player_teleport():
        mc.player.setTilePos(xPos, mc.getHeight(xPos,zPos), zPos)
def entity_teleport():
	mc.entity.setTilePos(int(entityID.get()), xPos, mc.getHeight(xPos,zPos), zPos)
def set_block():
	mc.setBlock(xPos, mc.getHeight(xPos,zPos), zPos, int(blockID.get()))

mc = minecraft.Minecraft.create()
mc.camera.setFixed()
xPos, yPos, zPos = mc.player.getTilePos()
defaultHeight = 8
height = defaultHeight

root = tk.Tk()
root.wm_title("Will's Mine Tools")

tk.Button(root, text='up', command=up).grid(row=0, column=1)
tk.Button(root, text='left', command=left).grid(row=1, column=0)
tk.Button(root, text='right', command=right).grid(row=1, column=2)
tk.Button(root, text='down', command=down).grid(row=2, column=1)

tk.Button(root, text='Zoom Out', command=zoomOut).grid(row=3, column=0)
tk.Button(root, text='Zoom Default', command=zoomDefault).grid(row=3, column=1)
tk.Button(root, text='Zoom In', command=zoomIn).grid(row=3, column=2)

tk.Button(root, text='Teleport player here', command=player_teleport).grid(row=4)

entityID = tk.StringVar()
tk.Entry(root, textvariable=entityID).grid(row=5, column=1)
tk.Button(root, text="Teleport entity here (type ID)", command=entity_teleport).grid(row=5, column=0)

blockID = tk.StringVar()
tk.Entry(root, textvariable=blockID).grid(row=6, column=1)
tk.Button(root, text="Set block here (type ID)", command=set_block).grid(row=6, column=0)

root.mainloop()

mc.camera.setNormal()
