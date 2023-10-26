import Queue
import copy

#A costume exception that the method ComputeHeightBinaryTreeRecursiveAndCheckTreesBalance
#uses.
class UnbalancedTreeException(Exception):
	pass

#A costume exception that the methods IsSubTreeLessEqualsToValue and
#IsSubTreeGreaterThanValue use.
class NotABinarySearchTreeException(Exception):
	pass

#A class that represents a binary tree node data structure.
class BinaryTreeNode(object):

	#A method that performs initialisation.
	#If the arguments are not provided, the binary tree node
	#data structure remains empty.
	def __init__(self, data = None, leftChild = None, rightChild = None, parent = None):

		self.data = data
		self.leftChild = leftChild
		self.rightChild = rightChild
		self.parent = parent
		#A data member utilised for tree traversal.
		self.visited = False


	#A method that defines equality between two BinaryTreeNode objects.
	def __eq__(self, other):

		output = False

		if (not other == None) and self.data == other.data:
			output = True

		return output


	#A method that sets the leftChild data member of the binary tree
	#node data structure.
	def SetLeftChild(self, data):

		self.leftChild = BinaryTreeNode(data)
		self.leftChild.parent = self


	#A method that sets the rightChild data member of the binary tree
	#node data structure.
	def SetRightChild(self, data):

		self.rightChild = BinaryTreeNode(data)
		self.rightChild.parent = self


	#A method that sets the parent data member of the binary tree
	#node data structure.
	def SetParent(self, data):

		self.parent = BinaryTreeNode(data)


	#A method that prints in in-order, the binary tree data structure rooted at given argument node.
	def PrintInOrder(self, node):

		if not node == None:
			node.PrintInOrder(node.leftChild)
			print(node.data)
			node.PrintInOrder(node.rightChild)


	#A method that prints in pre-order, the binary tree data structure rooted at given argument node.
	def PrintPreOrder(self, node):

		if not node == None:
			print(node.data)
			node.PrintPreOrder(node.leftChild)
			node.PrintPreOrder(node.rightChild)


	#A method that prints in post-order, the binary tree data strucutre rooted at given argument node.
	def PrintPostOrder(self, node):

		if not node == None:
			node.PrintPostOrder(node.leftChild)
			node.PrintPostOrder(node.rightChild)
			print(node.data)


	#A method that computes the Depth of a given node in the binary tree data structure.
	#Note that the depth of the root is defined to be 0.
	def ComputeDepthBinaryTree(self, node):

		depth = -1

		while not node == None:
			node = node.parent
			depth += 1

		return depth


	#A method that computes the depth of a given argument node in a complete binary tree data
	#structure
	def ComputeDepthCompleteTree(self, node):

		output = -1

		if not node == None:
			output = 0
			while not node.leftChild == None:
				output += 1
				node = node.leftChild

		return output


	#A method that returns the rightmost node data structure in a complete binary tree data
	#structure.
	def GetRightmostNode(self):

		previousNode, currentNode = None, self

		while not currentNode == None:
			previousNode = currentNode
			currentNode = currentNode.leftChild if self.ComputeDepthCompleteTree(currentNode.leftChild) > self.ComputeDepthCompleteTree(currentNode.rightChild) else currentNode.rightChild

		return previousNode


	#A method that returns the leftmost element in the binary tree data structure rooted
	#at the calling BinaryTreeNode object.
	def GetLeftmostNode(self):

		output = self

		while not output.leftChild == None:
			output = output.leftChild

		return output


	#A recursive method that builds a minimal binary search tree.
	#Note that the listOfSortedElements argument is assumed to be sorted indeed.
	def CreateMinimalBinarySearchTree(self, listOfSortedElements, startIndex, endIndex):

		node = None

		if not endIndex < startIndex:
			middleIndex = (startIndex + endIndex) // 2

			node = BinaryTreeNode(listOfSortedElements[middleIndex])
			node.leftChild = node.CreateMinimalBinarySearchTree(listOfSortedElements, startIndex, middleIndex - 1)
			node.rightChild = node.CreateMinimalBinarySearchTree(listOfSortedElements, middleIndex + 1, endIndex)

		return node


	#An auxiliary method for the IsBalancedImproved method of the binary tree
	#data structure.
	def ComputeHeightBinaryTreeRecursiveAndCheckTreesBalance(self, node):

		height = 0

		if not node == None:

			#Computes recursively the heights of the left and right subtrees.
			leftSubtreeHeight = node.ComputeHeightBinaryTreeRecursiveAndCheckTreesBalance(node.leftChild)
			rightSubtreeHeight = node.ComputeHeightBinaryTreeRecursiveAndCheckTreesBalance(node.rightChild)

			#Checks whether the tree is balanced, raises an exception
			#in case it's not.
			if abs(leftSubtreeHeight - rightSubtreeHeight) >  1:
				raise UnbalancedTreeException
			else:
				height = max(leftSubtreeHeight, rightSubtreeHeight) + 1

		return height
				

	#A recursive method that computes the height of the given node argument.
	def ComputeHeightBinaryTreeRecursive(self, node):

		height = 0

		if not node == None:
			height = max(node.ComputeHeightBinaryTreeRecursive(node.leftChild), node.ComputeHeightBinaryTreeRecursive(node.rightChild)) + 1

		return height


	#An iterative method that computes the height of the given node arguemnt.
	def ComputeHeightBinaryTreeIterative(self, node):

		height, nodes = 0, Queue.Queue()

		if not node == None:

			nodes.Add(node)

			while not nodes.IsEmpty():

				numberOfNodesAtCurrentDepth = nodes.queue.Size()
				height += 1
				
				#Iterates through the nodes at the current depth, and inserts any valid children
				#to the nodes queue, as the nodes at the next depth level.
				while not numberOfNodesAtCurrentDepth == 0:

					currentDepthNode = nodes.Remove().data
					numberOfNodesAtCurrentDepth -= 1
					
					if not currentDepthNode.leftChild == None:
						nodes.Add(currentDepthNode.leftChild)
					if not currentDepthNode.rightChild == None:
						nodes.Add(currentDepthNode.rightChild)


		return height


	#A method that checks whether the tree rooted at the given node
	#argument is balanced.
	def IsBalanced(self, node):

		output = True

		if not node == None:
			#Checks whether the current node is balanced.
			if abs(node.ComputeHeightBinaryTreeRecursive(node.leftChild) - node.ComputeHeightBinaryTreeRecursive(node.rightChild)) > 1:
				output = False
			else:
				#Recurses with the left and right subtrees.
				output = node.IsBalanced(node.leftChild) and node.IsBalanced(node.rightChild)

		return output


	#A method that checks whether the binary tree node data structure
	#is a valid binary search tree node.
	def IsAValidBinarySearchTreeNode(self):

		output = False

		if (self.leftChild == None or self.leftChild.data <= self.data) and (self.rightChild == None or self.data < self.rightChild.data):
			output = True

		return output


	#A method that checks whether the binary tree data structure rooted
	#at given argument node, is a binary search tree.
	def IsBinarySearchTree(self, node):

		return node.IsSubTreeLessEqualsToValue(node.leftChild, node.data) and node.IsSubTreeGreaterThanValue(node.rightChild, node.data)


	#An auxiliary method that checks whether the data data member of
	#the BinaryTreeNode object maintains a "<=" relation with given value argument 
	#along the subtree rooted at given node argument.
	def IsSubTreeLessEqualsToValue(self, node, value):

		output = True

		if not node == None:
			if value < node.data:
				raise NotABinarySearchTreeException
			else:
				output = node.IsSubTreeLessEqualsToValue(node.leftChild, value) and node.IsSubTreeLessEqualsToValue(node.rightChild, value)

		return output


	#An auxiliary method that checks whether the data data member of
	#the BinaryTreeNode object maintains a ">" relation with given value argument 
	#along the subtree rooted at given node argument.
	def IsSubTreeGreaterThanValue(self, node, value):

		output = True

		if not node == None:
			if node.data <= value:
				raise NotABinarySearchTreeException
			else:
				output = node.IsSubTreeGreaterThanValue(node.leftChild, value) and node.IsSubTreeGreaterThanValue(node.rightChild, value)

		return output


	#A method that returns the successor element to the given node argument,
	#in a binary search tree object.
	def BinarySearchTreeSuccessor(self, node):

		output = None

		#Checks whether the right subtree exists, and if so assigns the leftmost
		#element of said subtree as the output.
		if not node.rightChild == None:
			output = node.rightChild.GetLeftmostNode()
		#Finds the adequate parent node of the given node argument.
		else:
			currentNode = node
			currentNodeParent = node.parent
			while (not currentNodeParent == None) and (not currentNodeParent.leftChild == currentNode):
				currentNode = currentNodeParent
				currentNodeParent = currentNodeParent.parent
			output = currentNodeParent

		return output


	#A method that returns an adequate node to the given data
	#argument in a binary tree data structure.
	def GetBinaryTreeNodeByData(self, currentNode, data):

		output = None

		if not currentNode == None:

			if currentNode.data == data:
				output = currentNode
			else:
				if not currentNode.leftChild == None:
					output = currentNode.GetBinaryTreeNodeByData(currentNode.leftChild, data)
				if output == None and (not currentNode.rightChild == None):
					output = currentNode.GetBinaryTreeNodeByData(currentNode.rightChild, data)

		return output


	#A method that returns an adequate node to the given data
	#argument in a binary search tree data structure.
	def GetBinarySearchTreeNodeByData(self, currentNode, data):

		output = None

		if not currentNode == None:

			if currentNode.data == data:
				output = currentNode
			elif currentNode.data < data:
				output = self.GetBinarySearchTreeNodeByData(currentNode.rightChild, data)
			else:
				output = self.GetBinarySearchTreeNodeByData(currentNode.leftChild, data)

		return output


	#A method that checks whether the firstNode argument is an ancestor
	#of the secondNode argument.
	def IsAncestorOf(self, firstNode, secondNode):

		output = False
		while not secondNode == None:
			if firstNode == secondNode:
				output = True
				break
			secondNode = secondNode.parent

		return output


	#A method that returns the other child of the binary tree data structure.
	#Note that if the child argument is not a valid child, then a None value
	#shall be returned.
	def GetOtherChild(self, child):

		output = None

		if child == self.rightChild:
			output = self.leftChild
		elif child == self.leftChild:
			output = self.rightChild

		return output


	#A method that checks whether the firstTree argument equals
	#the secondTree argument.
	#Note that the method assumes neither tree is empty.
	def AreTreesEqual(self, firstTree, secondTree):

		output, firstTreeNodesQueue, secondTreeNodesQueue = True, Queue.Queue(), Queue.Queue()

		firstTreeNodesQueue.Add(firstTree)
		secondTreeNodesQueue.Add(secondTree)

		#Performs a BFS traversal along the firstTree and secondTree arguments,
		#and compares the nodes to determine whether the arguments are equal.
		while output and not secondTreeNodesQueue.IsEmpty():

			currentNodeFirstTree, currentNodeSecondTree = firstTreeNodesQueue.Remove().data, secondTreeNodesQueue.Remove().data

			if not currentNodeFirstTree == currentNodeSecondTree:
				output = False
				continue

			#Adds nodes to be examined for equality.
			if not currentNodeSecondTree.leftChild == None:
				secondTreeNodesQueue.Add(currentNodeSecondTree.leftChild)
			if not currentNodeSecondTree.rightChild == None:
				secondTreeNodesQueue.Add(currentNodeSecondTree.rightChild)
			if not currentNodeFirstTree.leftChild == None:
				firstTreeNodesQueue.Add(currentNodeFirstTree.leftChild)
			if not currentNodeFirstTree.rightChild == None:
				firstTreeNodesQueue.Add(currentNodeFirstTree.rightChild)


		return output



#A class that represents a binary tree data structure.
class BinaryTree(object):

	#A method that performs initialisation.
	#If the data argumenet is not provided, the binary tree
	#data structure remains empty.
	def __init__(self, data = None):

		self.root = BinaryTreeNode(data)


	#A method that prints the binary tree data structure
	def PrintBinaryTree(self):

		if self.root.data == None:
			print("Empty binary tree.")
		else:
			self.root.PrintInOrder(self.root)


	#A method that returns a new binary tree data structure, that represents 
	#a minimal binary search tree, in accordance with the listOfSortedElements
	#argument.
	def CreateMinimalBinarySearchTree(self, listOfSortedElements):

		#Creates a brand new binary tree data structure.
		minimalBinarySearchTree = BinaryTree()

		#Builds the minimal binary search tree utilising the recursive method
		#CreateMinimalBinarySearchTree of the BinaryTreeNode object.
		minimalBinarySearchTree.root = self.root.CreateMinimalBinarySearchTree(listOfSortedElements, 0, len(listOfSortedElements) - 1)

		return minimalBinarySearchTree


	#A method that returns a list of lists that contain the nodes at
	#each depth level.
	def ListOfDepths(self):

		listOfDepths, currentDepth = [], []

		if not self.root == None:
			currentDepth.append(self.root)

		while len(currentDepth) > 0:
			listOfDepths.append(currentDepth)
			previousDepth = currentDepth
			currentDepth = []
			#previousDepth is a list of the nodes from the upper depth.
			for parent in previousDepth:
				if not parent.leftChild == None:
					currentDepth.append(parent.leftChild)
				if not parent.rightChild == None:
					currentDepth.append(parent.rightChild)

		return listOfDepths


	#A method that checks whether the binary tree data structure is balanced.
	def IsBalanced(self):

		return self.root.IsBalanced(self.root)


	#An improved version of the method above, the method utilises an
	#auxiliary method that brings down the runtime to O(n) + O(h),
	#where n is the number of nodes contituting the binary tree, and
	#h is the tree's height.
	def IsBalancedImproved(self):

		output = True
		try:
			self.root.ComputeHeightBinaryTreeRecursiveAndCheckTreesBalance(self.root)
		except UnbalancedTreeException:
			output = False

		return output


	#A method that checks whether the binary tree data structure is
	#a binary search tree data structure.
	def IsBinarySearchTree(self):

		output = True

		if not self.root.data == None:

			try:
				output = self.root.IsBinarySearchTree(self.root)
			except NotABinarySearchTreeException:
				output = False

		return output


	#A method that finds and returns the first common ancestor of the 
	#given arguments firstNode and secondNode.
	def FirstCommonAncestorFirstVersion(self, firstNode, secondNode):

		output = None

		#Checks for direct ancestor relation.
		if self.root.IsAncestorOf(firstNode, secondNode):
			output = firstNode.parent
		elif self.root.IsAncestorOf(secondNode, firstNode):
			output = secondNode.parent
		#Neither nodes are ancestors of one another, finds the
		#first common ancestor.
		else:
			#Computes the difference in depths between the two nodes.
			deltaDepths = firstNode.ComputeDepthBinaryTree(firstNode) - secondNode.ComputeDepthBinaryTree(secondNode)

			#Initialises the deeper and the shallower nodes.
			deeperNode = firstNode if deltaDepths > 0 else secondNode
			shallowerNode = secondNode if deltaDepths > 0 else firstNode
			deltaDepths = abs(deltaDepths)

			#"Goes" up the subtree rooted at the deeper node
			#to match the depth of the other node.
			while deltaDepths > 0:
				deeperNode = deeperNode.parent
				deltaDepths -= 1

			#"Goes" up the adequate subtrees until arriving at the first common ancestor.
			while not shallowerNode == deeperNode:
				shallowerNode, deeperNode = shallowerNode.parent, deeperNode.parent

			output = shallowerNode

		return output


	#A method that finds and returns the first common ancestor of the 
	#given arguments firstNode and secondNode.
	def FirstCommonAncestorSecondVersion(self, firstNode, secondNode):

		output = None

		#Checks for direct ancestor relation.
		if self.root.IsAncestorOf(firstNode, secondNode):
			output = firstNode.parent
		elif self.root.IsAncestorOf(secondNode, firstNode):
			output = secondNode.parent
		else:
			#Looks for a sibling node that the subtree rooted at it,
			#includes the secondNode argument, and thus the parent of
			#this node is the first common ancestor.
			siblingNode = firstNode.parent.GetOtherChild(firstNode)
			firstNode = firstNode.parent
			while not self.root.IsAncestorOf(siblingNode, secondNode):
				siblingNode = firstNode.parent.GetOtherChild(firstNode)
				firstNode = firstNode.parent

			output = firstNode

		return output


	#A method that finds and returns the first common ancestor of the 
	#given arguments firstNode and secondNode.
	def FirstCommonAncestorThirdVersion(self, firstNode, secondNode):

		output = None

		#Checks for direct ancestor relation.
		if self.root.IsAncestorOf(firstNode, secondNode):
			output = firstNode.parent
		elif self.root.IsAncestorOf(secondNode, firstNode):
			output = secondNode.parent
		else:
			currentNode = self.root
			while currentNode.IsAncestorOf(currentNode, firstNode) and currentNode.IsAncestorOf(currentNode, secondNode):
				if currentNode.leftChild.IsAncestorOf(currentNode.leftChild, firstNode) and currentNode.leftChild.IsAncestorOf(currentNode.leftChild, secondNode):
					currentNode = currentNode.leftChild
				elif currentNode.rightChild.IsAncestorOf(currentNode.rightChild, firstNode) and currentNode.rightChild.IsAncestorOf(currentNode.rightChild, secondNode):
					currentNode = currentNode.rightChild
				else:
					break
			output = currentNode

		return output


	#An Auxiliary method that "weaves" two given lists, while maintaining
	#the order between elements in each list.
	#Note that the output is being added to the results argument,
	#which is initially an empty list.
	def WeaveLists(self, firstList, secondList, results, prefix):

		#One of the lists is empty. Appends any remaining elements
		#to a deep copy of the prefix list, and appends the resulting
		#list to the results list.
		if len(firstList) == 0 or len(secondList) == 0:
			result = copy.deepcopy(prefix)
			result += firstList
			result += secondList
			results.append(result)
			return

		#Removes the first element in the firstList argument, appends this 
		#element to the prefix argument and recurses. Upon return from the
		#recursive call, prepends the former mentioned element back to the
		#firstList argument. 
		firstListHead = firstList.pop(0)
		prefix.append(firstListHead)
		self.WeaveLists(firstList, secondList, results, prefix)
		prefix.pop()
		firstList.insert(0, firstListHead)

		#Removes the first element in the secondList argument, appends this 
		#element to the prefix argument and recurses. Upon return from the
		#recursive call, prepends the former mentioned element back to the
		#secondList argument. 
		secondListHead = secondList.pop(0)
		prefix.append(secondListHead)
		self.WeaveLists(firstList, secondList, results, prefix)
		prefix.pop()
		secondList.insert(0, secondListHead)


	#A method that returns a list of lists, where each list includes
	#an ordered sequence of nodes that could be used to create the binary
	#search tree data structure which called this method.
	def BinarySearchTreeSequences(self, node):

		result = []

		if node == None:
			result.append([])
			return result

		#Creats a prefix list, and appends the current node to it.
		prefix = []
		prefix.append(node)

		#Recurse left.
		leftBinarySearchTreeSequences = self.BinarySearchTreeSequences(node.leftChild)
		#Recurse right.
		rightBinarySearchTreeSequences = self.BinarySearchTreeSequences(node.rightChild)

		#Iterate through the left and right lists, and "weave" them together.
		for leftList in leftBinarySearchTreeSequences:
			for rightList in rightBinarySearchTreeSequences:
				weavedList = []
				self.WeaveLists(leftList, rightList, weavedList, prefix)
				result += weavedList

		return result


	#A method that checks whether the secondTree argument is a subtree
	#of the calling binary tree data structure.
	#Note that the method assumes neither tree is empty.
	def IsSubtree(self, secondTree):

		output, immediateNeighboursQueue = False, Queue.Queue()

		immediateNeighboursQueue.Add(self.root)

		#Performs a BFS traversal from the calling BinaryTree object's root,
		#searches for an occurance of the secondTree argument.
		while not immediateNeighboursQueue.IsEmpty():
			currentNode = immediateNeighboursQueue.Remove().data
			if self.root.AreTreesEqual(currentNode, secondTree):
				output = True
				break
			if not currentNode.leftChild == None:
				immediateNeighboursQueue.Add(currentNode.leftChild)
			if not currentNode.rightChild == None:
				immediateNeighboursQueue.Add(currentNode.rightChild)

		return output


	