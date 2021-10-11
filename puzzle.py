from random import randint
from matrix import Matrix
from queue import PriorityQueue
import random
import pygame
import colors
import numpy as np

class Puzzle:
    
    def __init__(self, x, y, width, height, state, parent, move, depth, cost, matrix, key,  blocks = []):
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
        self.matrix = matrix

    @staticmethod
    def new(x, y, width, height):
        return Puzzle(x, y, width, height, "", "", "", 0, 0, Matrix(3,3), "left", [])

    def validNumbers(self, numbers):
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
        n = randint(30,40)
        for i in range(n):
            zero = self.matrix.searchBlock(0)
            possibleMoves = []
            #move up
            if zero[0] > 0:
                possibleMoves.append(self.matrix.moveup)
            if zero[0] < 2:
                possibleMoves.append(self.matrix.movedown)
            if zero[1] > 0:
                possibleMoves.append(self.matrix.moveleft)
            if zero[1] < 2:
                possibleMoves.append(self.matrix.moveright)
            random.choice(possibleMoves)(zero)
        self.setBlocksMatrix()

    def setBlocksMatrix(self):
        blocks = []
        block_x=self.x
        block_y=self.y
        block_w = self.width/3
        block_h = self.height/3

        m = self.matrix.getMatrix()
        i=0
        for k in range(3):
            for j in range(3):
                blocks.append({'rect':pygame.Rect(block_x, block_y, block_w, block_h),'color':colors.BABY_BLUE,'block':m[k][j]})
                block_x += block_w+1 
                i+=1
            block_y += block_h+1
            block_x = self.x
        self.blocks = blocks

    def setBlocks(self, string):
        numbers = string.split(",")
        blocks = []
        if self.validNumbers(numbers) :
            block_x=self.x
            block_y=self.y

            block_w = self.width/3
            block_h = self.height/3
            self.matrix.buildMatrix(string)
            i=0
            for k in range(3):
                for j in range(3):
                    blocks.append({'rect':pygame.Rect(block_x, block_y, block_w, block_h),'color':colors.BABY_BLUE,'block':int(numbers[i])})
                    block_x += block_w+1 #right
                    i+=1
                block_y += block_h+1 #down
                block_x = self.x
            self.blocks = blocks
            return True
        return False

    def initialize(self):
        blocks =  "1,2,3,4,5,6,7,8,0"
        self.setBlocks(blocks)

    def existsIn(self,elem, list = []):
        for item in list:
            if item.isEqual(elem):
                return True
        return False

    def bestFirst(self):
        #função de avaliação por busca em largura
        node = self.matrix
        Mfinal = Matrix(3,3)
        Mfinal.buildMatrix("1,2,3,4,5,6,7,8,0") #1,2,3,4,5,6,7,8,0
        final = Mfinal.getMatrix()
        queue = PriorityQueue()
        queue.put(node)
        visitedNodes = []

        
        while(not node.isEqual(final) and not queue.empty()):
            node = queue.get()
            visitedNodes.append(node)
            moves = []
            childNodes = node.getPossibleNodes(moves)
            for i in range(len(childNodes)):
                if not self.existsIn(childNodes[i].getMatrix(),visitedNodes):
                    childNodes[i].move = moves[i]
                    childNodes[i].manhattanDist()
                    childNodes[i].setPrevious(node)
                    queue._put(childNodes[i])
            
        if(node.isEqual(final)):
            moves = []
            moves.append(node.move)
            nd = node.previous
            while nd != None:
                if nd.move != '':
                    moves.append(nd.move)
                nd = nd.previous
            return moves[::-1]
        return []
        
            
            
            

