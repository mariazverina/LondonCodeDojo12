
'''
Created on Oct 15, 2012

@author: mariaz

This was the first attempt using tests to let a design emerge
'''

import unittest


class Board(object):
    def __init__(self, cells):
        self.cells = cells

    def ringBuffer(self):
        return self.cells[-1:] + self.cells + self.cells[:1]

    def buildClusters(self):
        buf = self.ringBuffer()
        clusters = [buf[n:n + 3] for n in range(len(self.cells))]
        return clusters

    def evolve(self):
        clusters = self.buildClusters()
        self.cells = [self.futureCell(cluster) for cluster in clusters]
    
    def futureCell(self, currentCells):
        rule24 = [0, 0, 0, 1, 1, 0, 0, 0]
        ruleIndex = int(''.join([str(d) for d in currentCells]), 2) # 101 -> 5
        return rule24[ruleIndex]
    
    
class Test(unittest.TestCase):

    def testFirstGeneration(self):
        board = Board([1,0,0])
        board.evolve()
        self.assertEquals(board.cells, [0,1,0])

    def testSecondGeneration(self):
        board = Board([1,0,0])
        board.evolve()
        board.evolve()
        self.assertEquals(board.cells, [0,0,1])

    def testSingleCellEvolveToDead(self):
        board = Board([])
        self.assertEqual(board.futureCell([1,1,1]), 0)

    def testSingleCellEvolveToLive(self):
        board = Board([])
        self.assertEqual(board.futureCell([1,0,0]), 1)
    
    '''
    These tests emerged as the 'simple' evolve mechanism proved not simple enough and smaller chunks needed to be broken out and tested
    They are not behaviour driven - more implementation specific and did not carry easily into different implementation
    '''
        
    def testClusterGeneration(self):
        board = Board([1,0,0])
        self.assertEquals(board.buildClusters(), [[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    
    def testRingBuffer(self):
        board = Board([1,0,0])
        self.assertEqual(board.ringBuffer(), [0,1,0,0,1])
        
    def testBigBuffer(self):
        board = Board([1,0,0,1,0,0])
        board.evolve()
        self.assertEqual(board.cells, [0, 1, 0, 0, 1, 0])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFirstGeneration']
    unittest.main()