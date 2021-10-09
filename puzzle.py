from typing import Set
import pygame
import colors
from random import seed
from random import randint

class Puzzle:
    
    def __init__(self, x, y, width, height, state, parent, move, depth, cost, key,  blocks = []):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.blocks = blocks
        self.key = key
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def new(x, y, width, height):
        return Puzzle(x, y, width, height, "","","",0,0,"left", [])

    def validNumbers(self,numbers):
        valid = False
        if len(numbers) == 9:
            ref = list(range(9))
            valid = True
            for i in numbers:
                if int(i) not in ref:
                    valid = False
                else: 
                    ref.remove(int(i))

        return valid
    
    def randomBlocks(self): 
        ref = list(range(9))
        blocks = ""

        while len(ref)>0:
            value = randint(0, 8)
            if value in ref:
                blocks += str(value)
                if len(ref) != 1:
                    blocks += ","
                ref.remove(value)

        self.setBlocks(blocks)

    def setBlocks(self, string):
        numbers = string.split(",")
        blocks = []
        if self.validNumbers(numbers) :
            block_x=self.x
            block_y=self.y

            block_w = self.width/3
            block_h = self.height/3
            i=0
            for k in range(3):
                for j in range(3):
                    blocks.append({'rect':pygame.Rect(block_x, block_y, block_w, block_h),'color':colors.BABY_BLUE,'block':numbers[i]})
                    block_x += block_w+1 #right
                    i+=1
                block_y += block_h+1 #down
                block_x = self.x
            self.blocks = blocks
            return True
        return False

    def initialize(self):
        block_x=self.x
        block_y=self.y

        block_w = self.width/3
        block_h = self.height/3

        print("w:",block_w,"h:",block_h)
        blockNumber=1
        for i in range(3):
            for j in range(3):
                square = pygame.Rect(block_x, block_y, block_w, block_h)
                if blockNumber>8:
                    self.blocks.append({'rect':square,'color':colors.BLACK,'block':str(0)})
                else:
                    self.blocks.append({'rect':square,'color':colors.BABY_BLUE,'block':str(blockNumber)})
                blockNumber+=1
                block_x += block_w+1 #right
            block_y += block_h+1 #down
            block_x = self.x

