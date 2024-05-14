from settings import *
import random


class Maze:
    def __init__(self, app, wallPos):
        self.app = app
        self.visited = []
        self.walls = wallPos
        # x-range index on drawable surface is 1 to 52
        # y range index is 1 to 30
        self.xMax = 106
        self.yMax = 62

    def generateSolid(self):
        for y in range(2, self.yMax):
            for x in range(2, self.xMax):
                self.walls.append((x,y))
                self.draw((x,y), BLACK)
        self.redrawGrid()

        self.generateMaze()

    def generateMaze(self):
        x_pos = random.randint(2,self.xMax)
        y_pos = random.randint(2,self.yMax)
        start_pos = (x_pos, y_pos)

        print(len(self.walls))
        self.recursiveDFS(start_pos)

        print(len(self.walls))

    def checkValid(self, pos):
        if pos not in wall_nodes_coords_list and pos in self.walls:
            return True
        return False

    def recursiveDFS(self, pos):
        movesLeft = ['L', 'R', 'U', 'D']
        i, j = pos

        while movesLeft:
            if len(movesLeft) > 1:
                chooseRandMove = random.randint(0, len(movesLeft) - 1)
                currMove = movesLeft.pop(chooseRandMove)
            elif len(movesLeft) == 1:
                currMove = movesLeft[0]
                movesLeft = []
            # Temporary variabes to not update the original pos of the current node
            xTemp = i
            yTemp = j

            if currMove == 'L':
                xTemp -= 2
            elif currMove == 'R':
                xTemp += 2
            elif currMove == 'U':
                yTemp += 2
            else:
                yTemp -= 2

            newPos = (xTemp, yTemp)

            if self.checkValid(newPos):
                self.walls.remove(newPos)
                # calculate difference between curr pos and neighbouring pos
                xDiff = newPos[0] - i
                yDiff = newPos[1] - j

                # Determine the middle wall position to remove
                middleWallPos = (i+xDiff/2, j+yDiff/2)

                # Remove the middle wall as well
                if self.checkValid(middleWallPos):
                    self.walls.remove((middleWallPos))

                    self.drawMaze(middleWallPos, AQUAMARINE)
                    self.drawMaze(newPos, AQUAMARINE)

                    self.recursiveDFS(newPos)

        return

    def draw(self, pos, colour):
        i, j = pos
        pygame.draw.rect(self.app.screen, colour, (i * 12 + 240, j * 12, 12, 12), 0)

    def redrawGrid(self):
        # Redraw grid (for aesthetic purposes lol)
        for x in range(104):
            pygame.draw.line(self.app.screen, ALICE, (GS_X + x * 12, GS_Y), (GS_X + x * 12, GE_Y))
        for y in range(60):
            pygame.draw.line(self.app.screen, ALICE, (GS_X, GS_Y + y * 12), (GE_X, GS_Y + y * 12))

    def drawMaze(self, pos, colour):
        i, j = pos
        self.draw(pos, colour)

        # Redraw grid (for aesthetic purposes lol)
        for x in range(104):
            pygame.draw.line(self.app.screen, ALICE, (GS_X + x * 12, GS_Y), (GS_X + x * 12, GE_Y))
        for y in range(60):
            pygame.draw.line(self.app.screen, ALICE, (GS_X, GS_Y + y * 12), (GE_X, GS_Y + y * 12))

        pygame.display.update()
