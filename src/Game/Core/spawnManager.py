from settings import *
from Entities.plateform import Plateform
from Entities.plateform import MovingPlatform
from Entities.plateform import Whiteplatform
from Entities.spring import Spring
from Entities.jetpack import Jetpack
import random
class SpawnManager:
    def __init__(self):
        self.decay = 0.9999


    def update(self, plateformsList, player, springs, jetpacks):
        self.create_new_platform(plateformsList, player, springs, jetpacks)

    def create_new_platform(self, plateformsList, player, springs, jetpacks):
        if (plateformsList[-1].rect.y >= 0):
            self.choose_platform(plateformsList, player, springs, jetpacks)

    def choose_platform(self, plateformsList, player, springs, jetpacks):
        r = random.random()
        randomSpring = random.random()
        randomJetpack = random.random()
                
        if  r <= player.probaMovingPlatform():
            self.plateform = MovingPlatform(random.uniform(Plateform.position_platform_y, -70.0), random.randrange(30, WIDTH - 30))

            if randomSpring <= Plateform.spawnChanceSpring:
                spring = Spring(self.plateform, 20, -10)
                springs.append(spring)

            elif randomJetpack <= Plateform.spawnChanceJetpacks:
                jetpack = Jetpack(self.plateform, 20, -35)
                jetpacks.append(jetpack)
                        
        elif r <= player.probaMovingPlatform() + player.probaWhitePlatform():
            self.plateform = Whiteplatform(random.uniform(Plateform.position_platform_y, -70.0), random.randrange(30, WIDTH - 30))

            if randomJetpack <= Plateform.spawnChanceJetpacks:
                jetpack = Jetpack(self.plateform, 20, -35)
                jetpacks.append(jetpack)


        else:
            self.plateform = Plateform(random.uniform(Plateform.position_platform_y, -70.0), random.randrange(30, WIDTH - 30))

            if randomSpring <= Plateform.spawnChanceSpring:
                spring = Spring(self.plateform, 20, -10)
                springs.append(spring)

            elif randomJetpack <= Plateform.spawnChanceJetpacks:
                jetpack = Jetpack(self.plateform, 20, -35)
                jetpacks.append(jetpack)

            plateformsList.append(self.plateform)

            if Plateform.spawnChanceJetpacks > 0.005:
                Plateform.spawnChanceJetpacks *= self.decay
            
            if Plateform.spawnChanceSpring > 0.08:
                 Plateform.spawnChanceSpring *= self.decay

            if Plateform.position_platform_y >= -300:
                Plateform.position_platform_y -= 0.1