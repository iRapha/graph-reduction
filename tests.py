from utils.MatrixPrototypes import *
from score import score, diagnose
from utils import viz
from randomPermutation import getRandom

matrix7 = AdjacencyMatrix(7);
matrix7.addVertices(["A", "B", "C", "D", "E", "F", "G"])
matrix7.addEdge("D", "A")
matrix7.addEdge("D", "F")
matrix7.addEdge("D", "B")
matrix7.addEdge("B", "C")
matrix7.addEdge("B", "E")
matrix7.addEdge("F", "G")

matrix26 = AdjacencyMatrix(26)
matrix26.addVertices(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"])
matrix26.addEdge("A", "J")
matrix26.addEdge("A", "K")
matrix26.addEdge("J", "I")
matrix26.addEdge("I", "H")
matrix26.addEdge("I", "C")
matrix26.addEdge("I", "E")
matrix26.addEdge("K", "L")
matrix26.addEdge("B", "D")
matrix26.addEdge("C", "D")
matrix26.addEdge("C", "O")
matrix26.addEdge("L", "O")
matrix26.addEdge("L", "F")
matrix26.addEdge("O", "G")
matrix26.addEdge("E", "N")
matrix26.addEdge("G", "H")
matrix26.addEdge("D", "M")
matrix26.addEdge("M", "F")

matrix8 = AdjacencyMatrix(8)
matrix8.addVertices(["A", "B", "C", "D", "E", "F", "G", "H"])
matrix8.addEdge("A", "B")
matrix8.addEdge("A", "C")
matrix8.addEdge("A", "E")
matrix8.addEdge("B", "F")
matrix8.addEdge("B", "D")
matrix8.addEdge("C", "D")
matrix8.addEdge("C", "G")
matrix8.addEdge("E", "F")
matrix8.addEdge("E", "G")
matrix8.addEdge("H", "F")
matrix8.addEdge("H", "G")
matrix8.addEdge("H", "D")

matrix21 = AdjacencyMatrix(21)
matrix21.addVertices(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"])
matrix21.addEdge("A", "B")
matrix21.addEdge("A", "C")
matrix21.addEdge("A", "D")
matrix21.addEdge("A", "E")
matrix21.addEdge("B", "F")
matrix21.addEdge("B", "G")
matrix21.addEdge("B", "H")
matrix21.addEdge("B", "I")
matrix21.addEdge("C", "J")
matrix21.addEdge("C", "K")
matrix21.addEdge("C", "L")
matrix21.addEdge("C", "M")
matrix21.addEdge("D", "N")
matrix21.addEdge("D", "O")
matrix21.addEdge("D", "P")
matrix21.addEdge("D", "Q")
matrix21.addEdge("E", "R")
matrix21.addEdge("E", "S")
matrix21.addEdge("E", "T")
matrix21.addEdge("E", "U")

matrix4 = AdjacencyMatrix(4)
matrix4.addVertices(["A", "B", "C", "D"])
matrix4.addEdge("A", "B")
matrix4.addEdge("A", "C")
matrix4.addEdge("A", "D")
matrix4.addEdge("B", "C")
matrix4.addEdge("D", "B")
matrix4.addEdge("D", "C")

matrix34 = AdjacencyMatrix(34)
matrix34.addVertices([str(e) for e in xrange(1, 35)])
matrix34.addEdge("2", "1")
matrix34.addEdge("3", "1")
matrix34.addEdge("3", "2")
matrix34.addEdge("4", "1")
matrix34.addEdge("4", "2")
matrix34.addEdge("4", "3")
matrix34.addEdge("5", "1")
matrix34.addEdge("6", "1")
matrix34.addEdge("7", "1")
matrix34.addEdge("7", "5")
matrix34.addEdge("7", "6")
matrix34.addEdge("8", "1")
matrix34.addEdge("8", "2")
matrix34.addEdge("8", "3")
matrix34.addEdge("8", "4")
matrix34.addEdge("9", "1")
matrix34.addEdge("9", "3")
matrix34.addEdge("10", "3")
matrix34.addEdge("11", "1")
matrix34.addEdge("11", "5")
matrix34.addEdge("11", "6")
matrix34.addEdge("12", "1")
matrix34.addEdge("13", "1")
matrix34.addEdge("13", "4")
matrix34.addEdge("14", "1")
matrix34.addEdge("14", "2")
matrix34.addEdge("14", "3")
matrix34.addEdge("14", "4")
matrix34.addEdge("17", "6")
matrix34.addEdge("17", "7")
matrix34.addEdge("18", "1")
matrix34.addEdge("18", "2")
matrix34.addEdge("20", "1")
matrix34.addEdge("20", "2")
matrix34.addEdge("22", "1")
matrix34.addEdge("22", "2")
matrix34.addEdge("26", "24")
matrix34.addEdge("26", "25")
matrix34.addEdge("28", "3")
matrix34.addEdge("28", "24")
matrix34.addEdge("28", "25")
matrix34.addEdge("29", "3")
matrix34.addEdge("30", "24")
matrix34.addEdge("30", "27")
matrix34.addEdge("31", "2")
matrix34.addEdge("31", "9")
matrix34.addEdge("32", "1")
matrix34.addEdge("32", "25")
matrix34.addEdge("32", "26")
matrix34.addEdge("32", "29")
matrix34.addEdge("33", "3")
matrix34.addEdge("33", "9")
matrix34.addEdge("33", "15")
matrix34.addEdge("33", "16")
matrix34.addEdge("33", "19")
matrix34.addEdge("33", "21")
matrix34.addEdge("33", "23")
matrix34.addEdge("33", "24")
matrix34.addEdge("33", "30")
matrix34.addEdge("33", "31")
matrix34.addEdge("33", "32")
matrix34.addEdge("34", "9")
matrix34.addEdge("34", "10")
matrix34.addEdge("34", "14")
matrix34.addEdge("34", "15")
matrix34.addEdge("34", "16")
matrix34.addEdge("34", "19")
matrix34.addEdge("34", "20")
matrix34.addEdge("34", "21")
matrix34.addEdge("34", "23")
matrix34.addEdge("34", "24")
matrix34.addEdge("34", "27")
matrix34.addEdge("34", "28")
matrix34.addEdge("34", "29")
matrix34.addEdge("34", "30")
matrix34.addEdge("34", "31")
matrix34.addEdge("34", "32")
matrix34.addEdge("34", "33")

matrixBin = AdjacencyMatrix(15)
matrixBin.addVertices([str(e) for e in xrange(1, 16)])
matrixBin.addEdge("1", "2")
matrixBin.addEdge("1", "3")
matrixBin.addEdge("2", "4")
matrixBin.addEdge("2", "5")
matrixBin.addEdge("3", "6")
matrixBin.addEdge("3", "7")
matrixBin.addEdge("4", "8")
matrixBin.addEdge("4", "9")
matrixBin.addEdge("5", "10")
matrixBin.addEdge("5", "11")
matrixBin.addEdge("6", "12")
matrixBin.addEdge("6", "13")
matrixBin.addEdge("7", "14")
matrixBin.addEdge("7", "15")


import hillclimb
import simulatedannealing
import sampleGraph

# PICK YOUR STARTING MATRIX
# matrix = matrix7
# matrix = matrix26
# matrix = matrix8
# matrix = matrix21
# matrix = matrix4
# matrix = matrix34
matrix = matrixBin

randSolution = getRandom(matrix.vertices)

# FOR HILL CLIMBING, UNCOMMENT FIRST LINE.
# FOR SIMU ANNEALIN, UNCOMMENT SECOND LINE.
# solution, score, tries = hillclimb.climbhill(matrix, randSolution)
solution, fScore = simulatedannealing.simulateanneal(matrix, randSolution)

print "Random Solution"
diagnose(matrix, randSolution)
print "Final Solution"
diagnose(matrix, solution)

viz.display(matrix, randSolution)
viz.display(matrix, solution)
