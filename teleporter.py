import minecraft.minecraft as minecraft
import minecraft.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

mc.postToChat("enable diamond portal first")

def tp():
    mc.postToChat("Ready")
    while(True):
        npos = mc.player.getTilePos()
        if npos.x == eposo.x and npos.y == eposo.y+1 and npos.z == eposo.z:
            mc.player.setPos(epost.x+1.5, epost.y+1, epost.z)
        elif npos.x == epost.x and npos.y == epost.y+1 and npos.z == epost.z:
            mc.player.setPos(eposo.x+1.5, eposo.y+1, eposo.z)

x = 0

while(True):
    event = mc.events.pollBlockHits()
    for event in event:
        eposn = event.pos
        etype = mc.getBlock(eposn.x, eposn.y, eposn.z)
        if etype == block.DIAMOND_BLOCK.id:
            eposo = event.pos
            mc.postToChat("side 1 activated")
            mc.setBlock(eposo.x+1, eposo.y, eposo.z, block.WOOD)
            x = x+1
        elif etype == block.GOLD_BLOCK.id and x == 1:
            epost = event.pos
            mc.postToChat("side 2 activated")
            mc.setBlock(epost.x+1, epost.y, epost.z, block.WOOD)
            tp()
        else:
            mc.postToChat("enable side 1 first")


        
