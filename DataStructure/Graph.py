# Graph

# Adjacency Matrix

# Adjacency List
class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}
		self.distance = 0
		self.pred = None
		self.color = 'white'

	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr] = weight

	def __str__(self):
		return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

	def getConnections(self):
		return self.connectedTo

	def getId(self):
		return self.id

	def getWeight(self, nbr):
		return self.connectedTo[nbr]

	def getDistance(self):
		return self.distance

	def getPred(self):
		return self.pred

	def getColor(self):
		return self.color

	def setDistance(self, NewDistance):
		self.distance = NewDistance

	def setPred(self, NewPred):
		self.pred = NewPred

	def setColor(self, NewColor):
		self.color = NewColor

class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self, key):
		self.numVertices += 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def getVertex(self, n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def __contains__(self, n):
		return n in self.vertList

	def addEdge(self, f, t, cost=0):
		if f not in self.vertList:
			nv = self.addVertex(f)
		if t not in self.vertList:
			nv = self.addVertex(t)
		self.vertList[f].addNeighbor(self.vertList[t], cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())


g = Graph()
for i in range(6):
	g.addVertex(i)
print(g.vertList)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:
	for w in v.getConnections():
		print("( %s , %s )" % (v.getId(), w.getId()))


# The Word Ladder Problem

# Word ladder graph
def buildGraph(wordFile):
	d = {}
	g = Graph()
	wfile = open(wordFile, 'r')

	for line in wfile:
		word = line[:-1]
		for i in range(len(word)):
			bucket = word[:i] + '_' + word[i+1:]
			if bucket in d:
				d[bucket].append(word)
			else:
				d[bucket] = [word]

	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1 != word2:
					g.addEdge(word1, word2)

	return g


# BFS (Breadth First Search)
# O(V+E)
def bfs(g, start):
	start.setDistance(0)
	start.setPred(None)
	vertQueue = []
	vertQueue.insert(0, start)
	while (len(vertQueue) > 0):
		currentVert = vertQueue.pop()
		for nbr in currentVert.getConnections():
			if (nbr.getColor() == 'white'):
				nbr.setColor('gray')
				nbr.setDistance(currentVert.getDistance() + 1)
				nbr.setPred(currentVert)
				vertQueue.insert(0, nbr)
		currentVert.setColor('black')


def traverse(y):
	x = y
	while (x.getPred()):
		print(x.getId())
		x = x.getPred()
	print(x.getId())


# The Knight’s Tour Problem

def knightGraph(bdSize):
	ktGraph = Graph()
	for row in range(bdSize):
		for col in range(bdSize):
			nodeId = posToNodeId(row, col, bdSize)
			newPositions = genLegalMoves(row, col, bdSize)
			for e in newPositions:
				nid = posToNodeId(e[0], e[1], bdSize)
				ktGraph.addEdge(nodeId, nid)
	return ktGraph


def posToNodeId(row, column, board_size):
	return (row * board_size) + column


def genLegalMoves(x, y, bdSize):
	newMoves = []
	moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
				   ( 1, -2), ( 1, 2), ( 2, -1), ( 2, 1)]
	for i in moveOffsets:
		newX = x + i[0]
		newY = y + i[1]
		if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
			newMoves.append((newX, newY))

	return newMoves


def legalCoord(x, bdSize):
	if x >= 0 and x < bdSize:
		return True
	else:
		return False


# DFS (Depth First Search)
# O(V+E)
def knightTour(n, path, u, limit):
	u.setColor('gray')
	path.append(u)
	if n < limit:
		nbrList = list(u.getConnections())
		i = 0
		done = False
		while i < len(nbrList) and not done:
			if nbrList[i].getColor() == 'white':
				done = knightTour(n+1, path, nbrList[i], limit)
			i += 1
		if not done:
			path.pop()
			u.setColor('white')
	else:
		done = True
	return done


def orderByAvail(n):
	resList = []
	for v in n.getConnections():
		if v.getColor() == 'white':
			c = 0
			for w in v.getConnections():
				if w.getColor() == 'white':
					c = c + 1
			resList.append((c,v))
	resList.sort(key=lambda x: x[0])
	return [y[1] for y in resList]


class DFSGraph(graph):
	def __init__(self):
		super().__init__()
		self.time = 0

	def dfs(self):
		for aVertex in self:
			aVertex.setColor('white')
			aVertex.setPred(-1)
		for aVertex in self:
			if aVertex.getColor() == 'white':
				self.dfsvisit(aVertex)

	def dfsvisit(self, startVertex):
		startVertex.setColor('gray')
		self.time += 1
		startVertex.setDiscovery(self.time)
		for nextVertex in startVertex.getConnections():
			if nextVertex.getColor() == 'white':
				nextVertex.setPred(startVertex)
				self.dfsvisit(nextVertex)
		startVertex.setColor('black')
		self.time += 1
		startVertex.setFinish(self.time)


# Topological Sorting
# Call dfs(g) for some graph g. The main reason we want to call depth first search is to compute the finish times for each of the vertices.
#Store the vertices in a list in decreasing order of finish time.
#Return the ordered list as the result of the topological sort.


# Shortest Path Problems

# Dijkstra’s Algorithm
# O((V+E)log(V))
def dijkstra(aGraph, start):
	pq = PriorityQueue()
	start.setDistance(0)
	pq.buildHeap([(v.getDistance(), v) for v in aGraph])
	while not pq.isEmpty():
		currentVert = pq.delMin()
		for nextVert in currentVert.getConnections():
			newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
			if newDist < nextVert.getDistance():
				nextVert.setDistance(newDist)
				nextVert.setPred(currentVert)
				pq.decreaseKey(nextVert, newDist)


# Prim’s Spanning Tree Algorithm
def prim(G, start):
	pq = PriorityQueue()
	for v in G:
		v.setDistance(sys.maxsize)
		v.setPred(None)
	start.setDistance(0)
	pq.buildHeap([(v.getDistance(), v) for v in G])
	while not pq.isEmpty():
		currentVert = pq.delMin()
		for nextVert in currentVert.getConnections():
			newCost = currentVert.getWeight(nextVert)
			if nextVert in pq and newCost < nextVert.getDistance():
				nextVert.setPred(currentVert)
				nextVert.setDistance(newCost)
				pq.decreaseKey(nextVert, newCost)
