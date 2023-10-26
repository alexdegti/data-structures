#A class that represents a minimum heap data structure.
class MinimumHeap(object):

	#A method that performs initialisation.
	#If the data argument is not provided, the heap data
	#structure remains empty.
	def __init__(self, data = None):

		self.heap = []

		if not data == None:
			self.heap.append(data)


	#A method that returns the adequate parent node index for the
	#given nodeIndex argument. 
	def GetParentIndex(self, nodeIndex):

		return (nodeIndex - 1) // 2


	#A method that returns the adequate left child node index for
	#the given nodeIndex argument.
	def GetLeftChildIndex(self, nodeIndex):

		return (nodeIndex * 2) + 1


	#A method that returns the adequate right child node index for
	#the given nodeIndex argument.
	def GetRightChildIndex(self, nodeIndex):

		return (nodeIndex * 2) + 2


	#A method that returns the adequate parent node for the
	#given nodeIndex argument. 
	def GetParent(self, nodeIndex):

		return self.heap[self.GetParentIndex(nodeIndex)]


	#A method that returns the adequate left child node or None, for
	#the given nodeIndex argument.
	def GetLeftChild(self, nodeIndex):

		return self.heap[self.GetLeftChildIndex(nodeIndex)] if self.GetLeftChildIndex(nodeIndex) < len(self.heap) else None


	#A method that returns the adequate right child node or None, for
	#the given nodeIndex argument.
	def GetRightChild(self, nodeIndex):

		return self.heap[self.GetRightChildIndex(nodeIndex)] if self.GetRightChildIndex(nodeIndex) < len(self.heap) else None


	#A method that inserts the given data argument into the minimum heap data strucutre.
	def Insert(self, data):

		#Inserts the given data argument at the rightmost position.
		self.heap.append(data)

		#The index of the data that was just inserted.
		currentNodeIndex = len(self.heap) - 1

		#Performs swaps between the node at currentNodeIndex and its parent node, in order
		#to maintain the property of the minimum heap data structure.
		while (not currentNodeIndex == 0) and self.heap[currentNodeIndex] < self.heap[self.GetParentIndex(currentNodeIndex)]:
			self.heap[currentNodeIndex], self.heap[self.GetParentIndex(currentNodeIndex)], currentNodeIndex = self.GetParent(currentNodeIndex), self.heap[currentNodeIndex], self.GetParentIndex(currentNodeIndex)


	#A method that prints the minimum heap data structure to the screen.
	def PrintMinimumHeap(self):

		if len(self.heap) == 0:
			print("Empty minimum heap.")
		elif len(self.heap) == 1:
			print(f"root: {self.heap[0]}")
		else:
			print(f"root: {self.heap[0]}, left child: {self.GetLeftChild(0)}, right child: {self.GetRightChild(0)}")
			for index in range(1, len(self.heap)):
				print(f"current node: {self.heap[index]}, parent: {self.GetParent(index)}, left child: {self.GetLeftChild(index)}, right child: {self.GetRightChild(index)}")


	#A method that extracts, and returns the minimum element of the minimum heap
	#data structure.
	def ExtractMinimum(self):

		#Swaps the minimum element with the rightmost element in the minimum heap
		#data structure.
		minimum, self.heap[0], currentNodeIndex  = self.heap[0], self.heap.pop(), 0

		#Swaps the node at currentNodeIndex with one of its children in case one of them
		#is smaller, in order to maintain the property of the minimum heap data structure.
		while (not self.GetLeftChild(currentNodeIndex) == None and self.heap[currentNodeIndex] > self.GetLeftChild(currentNodeIndex)) or (not self.GetRightChild(currentNodeIndex) == None and self.heap[currentNodeIndex] > self.GetRightChild(currentNodeIndex)):
			  	if self.GetLeftChild(currentNodeIndex) < self.GetRightChild(currentNodeIndex):
			  		self.heap[currentNodeIndex], self.heap[self.GetLeftChildIndex(currentNodeIndex)], currentNodeIndex = self.GetLeftChild(currentNodeIndex), self.heap[currentNodeIndex], self.GetLeftChildIndex(currentNodeIndex)
			  	else:
			  		self.heap[currentNodeIndex], self.heap[self.GetRightChildIndex(currentNodeIndex)], currentNodeIndex = self.GetRightChild(currentNodeIndex), self.heap[currentNodeIndex], self.GetRightChildIndex(currentNodeIndex)

		return minimum


