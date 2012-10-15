'''
Created on Oct 15, 2012

@author: mariaz
'''
import unittest


class Board(object):
    
    def __init__(self, cellValues):
        self.cells = [Cell(v) for v in cellValues]
        count = len(self.cells)

        self.cells[0].left = self.cells[-1]
        self.cells[-1].right = self.cells[0]

        for i in range(count - 1):
            self.cells[i+1].left = self.cells[i]
            self.cells[i].right = self.cells[i+1]
    
    def getCell(self, index):
        return self.cells[index]

    def state(self):
        return [c.value for c in self.cells]

    def evolve(self):
        newValues = [cell.futureValue() for cell in self.cells]
        for i in range(len(newValues)) :
            self.cells[i].value = newValues[i]
    
class Cell(object):
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
    def state(self):
        return [self.left.value, self.value, self.right.value]
    
    
    def futureValue(self):
        rule24 = {
                  (1,1,1) : 0,
                  (1,1,0) : 0,
                  (1,0,1) : 0,
                  (1,0,0) : 1,
                  (0,1,1) : 1,
                  (0,1,0) : 0,
                  (0,0,1) : 0,
                  (0,0,0) : 0
                  }
        return rule24[tuple(self.state())]



class Test(unittest.TestCase):
    
    def testThatMiddleCellHasCorrectValues(self):
        board = Board([1,0,0])
        cell = board.getCell(1)
        self.assertEqual(cell.value, 0)
        self.assertEqual(cell.left.value, 1)
        self.assertEqual(cell.right.value, 0)

    def testThatLastCellHasCorrectValues(self):
        board = Board([1,0,0])
        cell = board.getCell(2)
        self.assertEqual(cell.value, 0)
        self.assertEqual(cell.left.value, 0)
        self.assertEqual(cell.right.value, 1)

    def testCellCanGiveItsState(self):
        leftCell = Cell(1)
        cell = Cell(0)
        rightCell = Cell(0)
        cell.left = leftCell
        cell.right = rightCell
        self.assertEqual(cell.state(), [1,0,0])

    def testCellEvolution(self):
        board = Board([1,0,0])
        middleCell = board.getCell(1)
        rightCell = board.getCell(2)
        self.assertEqual(middleCell.futureValue(), 1)
        self.assertEqual(rightCell.futureValue(), 0)
        
    def testBoardStateReporting(self):
        board = Board([1,0,0])
        self.assertEqual(board.state(), [1,0,0])
        
    def testBoardEvolution(self):
        board = Board([1,0,0])
        board.evolve()
        self.assertEqual(board.state(), [0,1,0])
        

    def testSecondGeneration(self):
        board = Board([1,0,0])
        board.evolve()
        board.evolve()
        self.assertEquals(board.state(), [0,0,1])

    def testSingleCellEvolveToDead(self):
        board = Board([1,1,1])
        self.assertEqual(board.getCell(1).futureValue(), 0)

#    def testSingleCellEvolveToLive(self):
#        board = Board([])
#        self.assertEqual(board.futureCell([1,0,0]), 1)
#    
#    def testClusterGeneration(self):
#        board = Board([1,0,0])
#        self.assertEquals(board.buildClusters(), [[0, 1, 0], [1, 0, 0], [0, 0, 1]])
#    
#    def testRingBuffer(self):
#        board = Board([1,0,0])
#        self.assertEqual(board.ringBuffer(), [0,1,0,0,1])
#        
#    def testBigBuffer(self):
#        board = Board([1,0,0,1,0,0])
#        self.assertEqual(board.evolve(),[0, 1, 0, 0, 1, 0])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFirstGeneration']
    unittest.main()