import minecraft.minecraft as minecraft
import minecraft.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

S = 200

r = input("How big do you want your area range to be. Say S to have a superflat ")

mc.setBlocks(pos.x+r,pos.y+100,pos.z+r,pos.x-r,pos.y,pos.z-r,block.AIR)

mc.setBlocks(pos.x+r,pos.y-1,pos.z+r,pos.x-r,pos.y-1,pos.z-r,block.GRASS)

mc.postToChat("your area has been cleared...")
