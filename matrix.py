
from random import randint
from copy import deepcopy
import numpy as np

class Matrix():

    def __init__(self, lins, cols):
        self.matrix = np.zeros((lins,cols), dtype=int)
        self.dist = 0
        self.previous = None
        self.move = ""
    
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

    def buildMatrix(self, str):
        numbers = str.split(",")
        if self.validNumbers(numbers):
            i=0
            for k in range(3):
                for j in range(3):
                    self.matrix[k][j] = int(numbers[i])
                    i += 1

    def searchBlock(self, value):
        for k in range(3):
            for j in range(3):
                if self.matrix[k][j] == value:
                    return (k,j)

    def moveup(self, zero):
        self.matrix[zero[0]][zero[1]] = self.matrix[zero[0]-1][zero[1]]
        self.matrix[zero[0]-1][zero[1]] = 0
    def movedown(self, zero):
        self.matrix[zero[0]][zero[1]] = self.matrix[zero[0]+1][zero[1]]
        self.matrix[zero[0]+1][zero[1]] = 0
    def moveright(self, zero):
        self.matrix[zero[0]][zero[1]] = self.matrix[zero[0]][zero[1]+1]
        self.matrix[zero[0]][zero[1]+1] = 0
    def moveleft(self, zero):
        self.matrix[zero[0]][zero[1]] = self.matrix[zero[0]][zero[1]-1]
        self.matrix[zero[0]][zero[1]-1] = 0

    def getPossibleNodes(self, moves):
        zero = self.searchBlock(0)
        possibleNodes = []
        if zero[0] > 0:
            self.moveup(zero)
            moves.append("up")
            possibleNodes.append(deepcopy(self))
            zero = self.searchBlock(0)
            self.movedown(zero)
            zero = self.searchBlock(0)
        if zero[0] < 2:
            self.movedown(zero)
            moves.append("down")
            possibleNodes.append(deepcopy(self))
            zero = self.searchBlock(0)
            self.moveup(zero)
            zero = self.searchBlock(0)
        if zero[1] > 0:
            self.moveleft(zero)
            moves.append("left")
            possibleNodes.append(deepcopy(self))
            zero = self.searchBlock(0)
            self.moveright(zero)
            zero = self.searchBlock(0)
        if zero[1] < 2:
            self.moveright(zero)
            moves.append("right")
            possibleNodes.append(deepcopy(self))
            zero = self.searchBlock(0)
            self.moveleft(zero)
            zero = self.searchBlock(0)
        return possibleNodes

    def getXY(self, value): #returns correct position of "value"
        if value == 1:
            return (0, 0)
        elif value == 2:
            return (0, 1)
        elif value == 3:
            return (0, 2)
        elif value == 4:
            return (1, 0)
        elif value == 5:
            return (1, 1)
        elif value == 6:
            return (1, 2)
        elif value == 7:
            return (2, 0)
        elif value == 8:
            return (2, 1)

    def manhattanDist(self):
        res = 0
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] != 0:
                    fi, fj = self.getXY(self.matrix[i][j])
                    res += abs(fi - i) + abs(fj - j)
        self.dist = res
        return res

    def getMatrix(self):
        return self.matrix

    def isEqual(self, matrix):
        return (self.matrix == matrix).all()

    def setPrevious(self, p):
        self.previous = p

    def __cmp__(self, other):
        return self.dist == other.dist
    def __lt__(self, other):
        return self.dist < other.dist
