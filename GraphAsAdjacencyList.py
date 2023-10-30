import random
import Queue

#A costume exception the method BuiilOrder uses.
class NoValidBuildOrderExistsException(Exception):
	pass

#A class that represents a graph node data structure.
#Note, this is an undirected graph.
class Node(object):

	#A method that performs initialisation.
	#If the data argument is not provided, the node data
	#structure remains empty.
	def __init__(self, data = None):

		self.data = data
		self.neighbours = []
		self.visited = False
		#A data member to count the number of nodes that this node
		#is a neighbour of.
		self.isNeighbourOfCount = 0


	#A method that defines equality between two Node objects.
	def __eq__(self, other):

		output = False

		if (not other == None) and self.data == other.data:
			output = True

		return output


	#A method that adds a neighbour to the node data structure.
	def AddNeighbour(self, data):

		self.neighbours.append(Node(data))


	#A method that removes a neighbour from the node data structure,
	#in accordance with the data argument.
	def RemoveNeighbour(self, data):

		self.neighbours.remove(Node(data))



#A class that represents a graph data structure.
class Graph(object):

	#A method that performs initialisation.
	def __init__(self):

		self.nodes = []


	#A method that parses an adequate input file according to
	#the inputFileName argument.
	#The input file consists of lines prefixed with V for a vertex
	#followed by a space and then the vertex' data, or an E for an
	#edge followed by a space and then the two vertices. (undirected graph)
	def ParseGraph(self, inputFileName):

		try:
			inputFile = open(inputFileName, "rt")

			for line in inputFile:
				line = line.split()
				#The current line includes a new node.
				if line[0] == "V":
					self.nodes.append(Node(line[1]))
				#The current line includes a new edge.
				elif line[0] == "E":
					self.nodes[self.nodes.index(Node(line[1]))].AddNeighbour(line[2])
					self.nodes[self.nodes.index(Node(line[2]))].AddNeighbour(line[1])
				else:
					print("Incorrect input file. Parsing failed.")

			inputFile.close()
		except FileNotFoundError:
			print("Could not find the input file.")


	#An auxiliary method that the method BuildOrder utilises.
	#The method parses a directed graph data structure adequate
	#to the provided nodesList and dependenciesList arguments.
	def ParseDirectedGraph(self, nodesList, dependenciesList):

		for node in nodesList:
			self.nodes.append(Node(node))
		
		for dependencie in dependenciesList:
			self.nodes[self.nodes.index(Node(dependencie[0]))].AddNeighbour(self.nodes[self.nodes.index(Node(dependencie[1]))])
			self.nodes[self.nodes.index(Node(dependencie[1]))].isNeighbourOfCount += 1


	#An auxiliary method that the method BuildOrder utilises.
	#The method returns a "secluded node", i.e a node that is not
	#a neighbour of any other node in the directed graph data structure.
	#Returns None if a node as mentioned before does not exist.
	def GetSecludedNode(self):

		output = None

		for node in self.nodes:
			#Found a secluded node.
			if node.isNeighbourOfCount == 0:
				output = node
				#Decreaments the neighbour's isNeighbourOfCount data member.
				for neighbour in node.neighbours:
					neighbour.isNeighbourOfCount -= 1
				#Assigns the secluded node's isNeighbourOfCount data member
				#with a special value, effectively "deleting" it.
				node.isNeighbourOfCount = -1
				break

		return output


	#A method that receives a list of nodes and a list of
	#project dependencies, and determines whether there
	#exists a possible order to complete all of the projects.
	def BuildOrder(self, nodesList, dependenciesList):

		self.ParseDirectedGraph(nodesList, dependenciesList)
		self.PrintGraph()

		output = []

		secludedNode = self.GetSecludedNode()

		#Keeps getting secluded nodes, until either all of the nodes
		#have been picked up, or there are no secluded nodes left in
		#the directed graph data structure, thus there is no feasible
		#building order.
		while (not secludedNode == None) and (not len(output) == len(self.nodes)):
			output.append(secludedNode)
			secludedNode = self.GetSecludedNode()

		if not len(output) == len(self.nodes):
			raise NoValidBuildOrderExistsException

		return output


	#A method that prints the graph data structure to the screen.
	def PrintGraph(self):

		if len(self.nodes) == 0:
			print("Empty graph.")
		else:
			#Iterates through the graph's nodes, and prints the current node
			#and its neighbours.
			for node in self.nodes:
				print(f"current node: {node.data}, neighbours:", end = "")
				for neighbour in node.neighbours:
					print(neighbour.data, end = ", ") 
				print()


	#A method that resets the data member visited of the nodes
	#composing the graph data structure.
	def SearchReset(self):

		for node in self.nodes:
			node.visited = False


	#A method that performs a depth-first-search.
	def DepthFirstSearching(self, node):

		if not node == None:

			#Prints the node's data, and sets the visited data member to True.
			print(node.data)
			self.nodes[self.nodes.index(node)].visited = True

			#Iterates through the neighbours, and calls DepthFirstSearching
			#recursively with each neighbour that is yet to be visited as an
			#argument.
			for neighbour in self.nodes[self.nodes.index(node)].neighbours:
				if not self.nodes[self.nodes.index(neighbour)].visited:
					self.DepthFirstSearching(neighbour)


	#A method that performs a depth-first-search starting from the given
	#node argument.
	def DepthFirstSearch(self, node):

		self.DepthFirstSearching(self.nodes[self.nodes.index(node)])
		self.SearchReset()


	#A method that performs a depth-first-search from a random
	#node in the graph data structure.
	def DepthFirstSearchFromRandomNode(self):

		self.DepthFirstSearch(random.choice(self.nodes))


	#A method that performs a breadth-first-search.
	def BreadthFirstSearching(self, node):

		nodesQueue = Queue.Queue()
		self.nodes[self.nodes.index(node)].visited = True
		nodesQueue.Add(self.nodes[self.nodes.index(node)])

		while not nodesQueue.IsEmpty():
			currentNode = nodesQueue.Remove().data
			print(currentNode.data)

			for neighbour in self.nodes[self.nodes.index(currentNode)].neighbours:
				if not self.nodes[self.nodes.index(neighbour)].visited:
					self.nodes[self.nodes.index(neighbour)].visited = True
					nodesQueue.Add(self.nodes[self.nodes.index(neighbour)])


	#A method that performs a breadth-first-search from the given
	#node argument.
	def BreadthFirstSearch(self, node):

		self.BreadthFirstSearching(self.nodes[self.nodes.index(node)])
		self.SearchReset()


	#A method that performs a breadth-first-search from a random
	#node in the graph data structure.
	def BreadthFirstSearchFromRandomNode(self):

		self.BreadthFirstSearch(random.choice(self.nodes))


	#A method that returns whether there is a route from the
	#firstNode argument to the secondNode argument in the graph
	#data structure.
	def IsThereARouteBetweenNodes(self, firstNode, secondNode):

		self.BreadthFirstSearching(self.nodes[self.nodes.index(firstNode)])

		output = self.nodes[self.nodes.index(secondNode)].visited

		self.SearchReset()

		return output


