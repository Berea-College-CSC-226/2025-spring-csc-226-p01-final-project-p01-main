import pygame

class Maze:
    def __init__(self, matrix, size):
        self.matrix = matrix
        self.size = size
        self.cellHeight = len(size[0])
        self.cellWidth = len(size)

    def drawMaze(self):
        pass

    def placeBoundary(self, position):
        pass