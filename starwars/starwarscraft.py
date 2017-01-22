# starwarscraft.py - original by Martin O'Hanlon
# modified by David Whale 22/01/2017

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as vec3
import mcpi.minecraftstuff as mcstuff
import math
from time import sleep
#from threading import Thread


#----- CRAFT SHAPE DEFINITIONS ------------------------------------------------

XWING_BLOCKS = [
    mcstuff.ShapeBlock(0,0,-2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(0,0,-1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(0,0,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-3,1,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(0,0,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(3,1,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-3,1,1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-1,1,1,block.WOOL.id,8),
    mcstuff.ShapeBlock(0,1,1,block.WOOL.id,3),
    mcstuff.ShapeBlock(1,1,1,block.WOOL.id,8),
    mcstuff.ShapeBlock(3,1,1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-2,1,2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-1,1,2,block.WOOL.id,8),
    mcstuff.ShapeBlock(0,1,2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(1,1,2,block.WOOL.id,8),
    mcstuff.ShapeBlock(2,1,2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-3,-1,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(3,-1,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-3,-1,1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-1,0,1,block.WOOL.id,8),
    mcstuff.ShapeBlock(0,0,1,block.WOOL.id,3),
    mcstuff.ShapeBlock(1,0,1,block.WOOL.id,8),
    mcstuff.ShapeBlock(3,-1,1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-2,-1,2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-1,0,2,block.WOOL.id,8),
    mcstuff.ShapeBlock(0,0,2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(1,0,2,block.WOOL.id,8),
    mcstuff.ShapeBlock(2,-1,2,block.IRON_BLOCK)
]

XWING_DIAGONAL_BLOCKS = [
    mcstuff.ShapeBlock(-2,1,-2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(2,0,-2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-3,1,-1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(1,0,-1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-3,1,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-2,1,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-1,1,0,block.WOOL.id, 8),
    mcstuff.ShapeBlock(0,0,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-2,1,1,block.WOOL.id, 8),
    mcstuff.ShapeBlock(-1,1,1,block.WOOL.id, 3),
    mcstuff.ShapeBlock(0,1,1,block.WOOL.id, 8),
    mcstuff.ShapeBlock(-1,1,2,block.WOOL.id, 8),
    mcstuff.ShapeBlock(0,1,2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(2,1,2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(0,1,3,block.IRON_BLOCK),
    mcstuff.ShapeBlock(1,1,3,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-2,-1,-2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-3,-1,-1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-3,-1,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-2,0,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-1,0,0,block.WOOL.id, 8),
    mcstuff.ShapeBlock(-2,0,1,block.WOOL.id, 8),
    mcstuff.ShapeBlock(-1,0,1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(0,0,1,block.WOOL.id, 8),
    mcstuff.ShapeBlock(-1,0,2,block.WOOL.id, 8),
    mcstuff.ShapeBlock(0,0,2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(2,-1,2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(0,-1,3,block.IRON_BLOCK),
    mcstuff.ShapeBlock(1,-1,3,block.IRON_BLOCK)
]

MILLENIUM_FALCON_BLOCKS = [
    mcstuff.ShapeBlock(-1,0,-2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(0,0,-2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(1,0,-2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-2,0,-1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-1,0,-1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(0,1,-1,block.WOOL.id,8),
    mcstuff.ShapeBlock(1,0,-1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(2,0,-1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-3,0,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-2,0,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-1,1,0,block.WOOL.id,8),
    mcstuff.ShapeBlock(0,1,0,block.WOOL.id,8),
    mcstuff.ShapeBlock(1,1,0,block.WOOL.id,8),
    mcstuff.ShapeBlock(2,0,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(3,0,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-3,0,1,block.WOOL.id,7),
    mcstuff.ShapeBlock(-2,0,1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-1,0,1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(0,1,1,block.WOOL.id,8),
    mcstuff.ShapeBlock(1,0,1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(2,0,1,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-3,0,2,block.WOOL.id,7),
    mcstuff.ShapeBlock(-1,0,2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(0,0,2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(1,0,2,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-1,0,3,block.IRON_BLOCK),
    mcstuff.ShapeBlock(1,0,3,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-1,0,4,block.IRON_BLOCK),
    mcstuff.ShapeBlock(1,0,4,block.IRON_BLOCK),
    mcstuff.ShapeBlock(0,0,-1,block.WOOL.id,8),
    mcstuff.ShapeBlock(-1,0,0,block.WOOL.id,8),
    mcstuff.ShapeBlock(0,0,0,block.WOOL.id,8),
    mcstuff.ShapeBlock(1,0,0,block.WOOL.id,8),
    mcstuff.ShapeBlock(0,0,1,block.WOOL.id,8)
]

TIE_FIGHTER_BLOCKS = [
    mcstuff.ShapeBlock(0,0,0,block.IRON_BLOCK),
    mcstuff.ShapeBlock(-1,-1,-1,block.WOOL.id,15),
    mcstuff.ShapeBlock(-1,-1,0,block.WOOL.id,15),
    mcstuff.ShapeBlock(-1,-1,1,block.WOOL.id,15),
    mcstuff.ShapeBlock(-1,0,-1,block.WOOL.id,15),
    mcstuff.ShapeBlock(-1,0,0,block.WOOL.id,15),
    mcstuff.ShapeBlock(-1,0,1,block.WOOL.id,15),
    mcstuff.ShapeBlock(-1,1,-1,block.WOOL.id,15),
    mcstuff.ShapeBlock(-1,1,0,block.WOOL.id,15),
    mcstuff.ShapeBlock(-1,1,1,block.WOOL.id,15),
    mcstuff.ShapeBlock(1,-1,-1,block.WOOL.id,15),
    mcstuff.ShapeBlock(1,-1,0,block.WOOL.id,15),
    mcstuff.ShapeBlock(1,-1,1,block.WOOL.id,15),
    mcstuff.ShapeBlock(1,0,-1,block.WOOL.id,15),
    mcstuff.ShapeBlock(1,0,0,block.WOOL.id,15),
    mcstuff.ShapeBlock(1,0,1,block.WOOL.id,15),
    mcstuff.ShapeBlock(1,1,-1,block.WOOL.id,15),
    mcstuff.ShapeBlock(1,1,0,block.WOOL.id,15),
    mcstuff.ShapeBlock(1,1,1,block.WOOL.id,15)
]


#----- HELPERS ----------------------------------------------------------------

# finds point on sphere (based on polar co-ordinates) 
def findPointOnSphere(cx, cy, cz, radius, phi, theta):
    #phi - angle around the pole 0<= phi <= 360
    #theta - angle from plan 'up' -90 <= theta <= 90
    x = cx + radius * math.cos(math.radians(theta)) * math.cos(math.radians(phi))
    z = cz + radius * math.cos(math.radians(theta)) * math.sin(math.radians(phi))
    y = cy + radius * math.sin(math.radians(theta))
    return int(round(x,0)), int(round(y,0)), int(round(z,0))


#----- MC OBJECT --------------------------------------------------------------
#
# An arbitrary moveable object inside Minecraft

class MCObject(object):
    def __init__(self, blocks, pos):
        # Convert tuple/list to a real position
        if type(pos) == tuple or type(pos) == list:
            pos = vec3.Vec3(pos[0], pos[1], pos[2])

        self.blocks       = blocks
        self.mc           = minecraft.Minecraft.create()
        self.shape        = mcstuff.MinecraftShape(self.mc, pos, blocks)
        self.turnYawAngle = 0
        self.pitchAngle   = 0

    def clear(self):
        self.shape.clear()

    def draw(self):
        self.shape.draw()

    def move_by(self, x=None, y=None, z=None):
        nx, ny, nz = self.position.x, self.position.y, self.position.z
        if x is not None: nx += x
        if y is not None: ny += y
        if z is not None: nz += z
        self.shape.move(nx, ny, nz)

    def move_to(self, x, y, z):
        self.shape.move(x, y, z)

    def rotate_by(self, yaw=0, pitch=0, roll=0):
        self.shape.rotateBy(yaw, pitch, roll)

    def rotate_to(self, yaw, pitch, roll):
        self.shape.rotate(yaw, pitch, roll)

    def fly(self):
        if self.turnYawAngle != 0:
            self.rotate_by(self.turnYawAngle, 0, 0)

        x, y, z = findPointOnSphere(self.position.x, self.position.y, self.position.z,
                                    1, self.shape.yaw - 90, self.shape.pitch)
        self.shape.move(x,y,z)

    def fly_to(self, x, y, z, speed=0.1):
        mcDraw        = mcstuff.MinecraftDrawing(self.mc)
        blocksBetween = mcDraw.getLine(self.shape.position.x,
                                       self.shape.position.y,
                                       self.shape.position.z,
                                       x,
                                       y,
                                       z)

        for blockBetween in blocksBetween:
            self.shape.move(blockBetween.x, blockBetween.y, blockBetween.z)
            # time to sleep between each block move
            sleep(speed)

    @property
    def position(self):
        return self.shape.position


#----- STARWARS CRAFT ---------------------------------------------------------
#
# Really this is just a threaded blocks object (base class)

## class StarwarsCraft:
##     def __init__(self, craftBlocks, pos):
## ## 
##         self.mc = minecraft.Minecraft.create()
## ## 
##         #create the craft
##         self.craftShape = mcstuff.MinecraftShape(self.mc, pos, craftBlocks)
## ## 
##         self.flying = False
##         self.turnYawAngle = 0
##         self.pitchAngle = 0
## ## 
##     #fly the craft to a position, speed is the time to wait between moving
##     def flyTo(self,x,y,z,speed,background=False):
##         #run it in its own thread
##         flyToThread = Thread(None, self._flyTo, None, (x, y, z, speed))
##         flyToThread.start()
##         
##         #if backgroud == True, return the thread, otherwise wait for it to finish
##         if background == False:
##             flyToThread.join()
## ## 
##         return flyToThread
## ## 
##     def _flyTo(self,x,y,z,speed):
##         mcDraw = mcstuff.MinecraftDrawing(self.mc)
##         blocksBetween = mcDraw.getLine(self.craftShape.position.x,
##                                        self.craftShape.position.y,
##                                        self.craftShape.position.z,
##                                        x,
##                                        y,
##                                        z)
##         
##         for blockBetween in blocksBetween:
##             self.craftShape.move(blockBetween.x, blockBetween.y, blockBetween.z)
##             # time to sleep between each block move
##             sleep(speed)
## ## 
##     def fly(self, speed):
##         self.flying = True
##         self.flyThread = Thread(None, self._fly, None, (speed,))
##         self.flyThread.start()
##         
##         return self.flyThread
## ## 
##     def _fly(self, speed):
##         while self.flying:
##             if self.turnYawAngle != 0:
##                 self.rotateBy(self.turnYawAngle, 0, 0)
##             
##             x, y, z = findPointOnSphere(self.position.x, self.position.y, self.position.z,
##                                         1, self.craftShape.yaw - 90, self.craftShape.pitch)
##             self.craftShape.move(x,y,z)
##             sleep(speed)
## ## 
##     def stop(self):
##         self.flying = False
##         self.flyThread.join()
## ## 
##     def clear(self):
##         self.craftShape.clear()
##     
##     def draw(self):
##         self.craftShape.draw()
## ## 
##     def rotate(self, yaw, pitch, roll):
##         self.craftShape.rotate(yaw, pitch, roll)
## ## 
##     def rotateBy(self, yaw, pitch, roll):
##         self.craftShape.rotateBy(yaw, pitch, roll)
## ## 
##     def turn(self, angle):
##         self.turnYawAngle = angle
## ## 
##     @property
##     def position(self):
##         return self.craftShape.position
## ## 
## 
## #----- TIE FIGHTER ------------------------------------------------------------
## #
## # This is a threaded active object
## ## 
## class TieFighter(StarwarsCraft):
##     def __init__(self, pos):
##         StarwarsCraft.__init__(self, TIE_FIGHTER_BLOCKS, pos)
## ## 
## 
## #----- MILLENIUM FALCON -------------------------------------------------------
## #
## # This is a threaded active object
## ## 
## class MilleniumFalcon(StarwarsCraft):
##     def __init__(self, pos):
##         StarwarsCraft.__init__(self, MILLENIUM_FALCON_BLOCKS, pos)
## ## 
## 
## #----- XWING FIGHTER DIAGONAL -------------------------------------------------
## #
## # This is a threaded active object
## ## 
## class XWingFighterDiagonal(StarwarsCraft):
##     def __init__(self, pos):
##         StarwarsCraft.__init__(self, XWING_DIAGONAL_BLOCKS, pos)
## ## 
## 
## #----- XWING FIGHTER ----------------------------------------------------------
## #
## # This is a threaded active object
## ## 
## class XWingFighter(StarwarsCraft):
##     def __init__(self, pos):
##         StarwarsCraft.__init__(self, XWING_BLOCKS, pos)


#----- TESTS ------------------------------------------------------------------

## if __name__ == "__main__":
##     mc = minecraft.Minecraft.create()
##     
##     playerPos = mc.player.getTilePos()
##     craftPos = playerPos.clone()
##     craftPos.y += 10
##     craftPos.z += 20
##     craft = XWingFighter(craftPos)
##     sleep(5)
## ## 
##     craft.fly(0.25)
##     sleep(5)
##     craft.turn(5)
##     sleep(10)
##     craft.turn(-5)
##     sleep(10)
##     craft.turn(0)
##     sleep(5)
##     craft.stop()
##     sleep(2)
##     craft.clear()
## ## 
## if __name__ == "old__main__":
## ## 
##     mc = minecraft.Minecraft.create()
##     
##     playerPos = mc.player.getTilePos()
## ## 
## 
##     #create the craft around the player
##     tie1Pos = playerPos.clone()
##     tie1Pos.x -= 10
##     tie1 = TieFighter(tie1Pos)
## ## 
##     tie2Pos = playerPos.clone()
##     tie2Pos.x += 10
##     tie2 = TieFighter(tie2Pos)
##     falconPos = playerPos.clone()
##     falconPos.z += 10
##     falcon = MilleniumFalcon(falconPos)
##     xWingPos = playerPos.clone()
##     xWingPos.y += 10
##     xWing = XWingFighter(xWingPos)
## ## 
##     sleep(25)
## ## 
##     #set the craft to fly (threaded)
##     tie1Fly = tie1.fly(tie1Pos.x, tie1Pos.y, tie1Pos.z + 25, 0.25, True)
##     tie2Fly = tie2.fly(tie2Pos.x, tie2Pos.y, tie2Pos.z + 25, 0.25, True)
##     falconFly = falcon.fly(falconPos.x, falconPos.y, falconPos.z + 25, 0.25, True)
##     xWingFly = xWing.fly(xWingPos.x + 25, xWingPos.y, xWingPos.z - 25, 0.25, True)
## ## 
##     #wait for the craft to stop
##     tie1Fly.join()
##     tie2Fly.join()
##     falconFly.join()
##     xWingFly.join()
## ## 
##     #clear the craft
##     tie1.clear()
##     tie2.clear()
##     falcon.clear()
##     xWing.clear()

#----- TEST HARNESS -----------------------------------------------------------

if __name__ == "__main__":
    mc         = minecraft.Minecraft.create()
    player_pos = mc.player.getTilePos()
    xp         = player_pos.clone()
    xp.y       += 10
    xwing      = MCObject(XWING_BLOCKS, xp)
    mc.player.setTilePos(xp)

    mc.postToChat("Here is your X-wing")
    xwing.draw()

    mc.postToChat("Fly for a bit")
    for i in range(20):
        xwing.fly()
        ##mc.player.setTilePos(xwing.position)
        sleep(0.1)

    mc.postToChat("rotate -90")
    xwing.rotate_by(yaw=-90)

    mc.postToChat("fly for a bit")
    for i in range(20):
        xwing.fly()
        ##mc.player.setTilePos(xwing.position)
        sleep(0.5)

    mc.postToChat("mission completed")

# END
