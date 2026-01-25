import pygame
from settings import *
from Entities.plateform import Plateform
from Entities.plateform import MovingPlatform
from Entities.plateform import Whiteplatform
from Entities.enemy import Enemy
from Entities.spring import Spring
from Entities.jetpack import Jetpack
import random
class SpawnManager:
    spawnChanceSpring = 0.12
    spawnChanceJetpacks = 0.01
    spawnChanceEnemy = 0.0005
    position_platform_y = -70
    randomEnemy = 0
    def __init__(self):
        self.decay = 0.9999
        self.last = 0
        self.position_axe_y_platform = 0


    def update(self, plateformsList, player, springs, jetpacks, enemies):
        self.create_new_platform(plateformsList, player, springs, jetpacks)
        self.CanEnemySpawn(enemies)
        #print(SpawnManager.randomEnemy)

    def CanEnemySpawn(self, enemies):
        SpawnManager.randomEnemy = random.random()    
        if self.position_axe_y_platform < -70 and SpawnManager.randomEnemy < SpawnManager.spawnChanceEnemy:
            self.create_new_enemy(enemies)

    def create_new_enemy(self, enemies):
            self.enemy = Enemy()
            enemies.append(self.enemy)

    def create_new_platform(self, plateformsList, player, springs, jetpacks):
        if (plateformsList[-1].rect.y >= 0):
            self.choose_platform(plateformsList, player, springs, jetpacks)

    def choose_platform(self, plateformsList, player, springs, jetpacks):
        r = random.random()
        randomSpring = random.random()
        randomJetpack = random.random()
        self.position_axe_y_platform = random.uniform(SpawnManager.position_platform_y, -70.0)
        
        if  r <= player.probaMovingPlatform():
            self.plateform = MovingPlatform(self.position_axe_y_platform, random.randrange(30, WIDTH - 30))

            if randomSpring <= SpawnManager.spawnChanceSpring:
                spring = Spring(self.plateform, 20, -10)
                springs.append(spring)

            elif randomJetpack <= SpawnManager.spawnChanceJetpacks:
                jetpack = Jetpack(self.plateform, 20, -35)
                jetpacks.append(jetpack)
                        
        elif r <= player.probaMovingPlatform() + player.probaWhitePlatform():
            self.plateform = Whiteplatform(self.position_axe_y_platform, random.randrange(30, WIDTH - 30))

            if randomJetpack <= SpawnManager.spawnChanceJetpacks:
                jetpack = Jetpack(self.plateform, 20, -35)
                jetpacks.append(jetpack)


        else:
            self.plateform = Plateform(self.position_axe_y_platform, random.randrange(30, WIDTH - 30))

            if randomSpring <= SpawnManager.spawnChanceSpring:
                spring = Spring(self.plateform, 20, -10)
                springs.append(spring)

            elif randomJetpack <= SpawnManager.spawnChanceJetpacks:
                jetpack = Jetpack(self.plateform, 20, -35)
                jetpacks.append(jetpack)


            if SpawnManager.spawnChanceJetpacks > 0.005:
                SpawnManager.spawnChanceJetpacks *= self.decay
            
            if SpawnManager.spawnChanceSpring > 0.08:
                 SpawnManager.spawnChanceSpring *= self.decay

            if SpawnManager.spawnChanceEnemy < 0.01:
                SpawnManager.spawnChanceEnemy /= self.decay

            if SpawnManager.position_platform_y >= -300:
                SpawnManager.position_platform_y -= 0.1
           # print(self.position_axe_y_platform)
           
        plateformsList.append(self.plateform)

            

