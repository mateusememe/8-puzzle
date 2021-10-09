from typing import Set
import pygame
import pygame_gui

class Puzzle:
    global BLACK 
    global BABY_BLUE 
    
    def __init__(self, state, parent, move, depth, cost, key,  blocks = []):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.blocks = blocks
        self.key = key
        self.BLACK, self.BABY_BLUE = (0, 0, 0), (137, 207, 240)

    
    def initialize(self):
        top_block=50
        left_block=50
        blockNumber=1
        for i in range(3):
            for j in range(3):
                if blockNumber>8:
                    self.blocks.append({'rect':pygame.Rect(left_block,top_block,99,99),'color':(0, 0, 0),'block':str(0)})
                else:
                    self.blocks.append({'rect':pygame.Rect(left_block,top_block,99,99),'color':(137, 207, 240),'block':str(blockNumber)})
                blockNumber+=1
                left_block+=100
            top_block+=100
            left_block=0

