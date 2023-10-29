import copy

#A class that represents a node of a singly linked list data structure.
class SinglyLinkedListNode(object):

	#A method that performs initialisation.
	#Assumes that if the data argument isn't provided, so is nextNode argument.
	def __init__(self, data = None, nextNode = None):

		self.data = data
		self.nextNode = nextNode



#A class that represents a node of a doubly linked list data structure.
class DoublyLinkedListNode(object):

	#A method that performs initialisation.
	#Assumes that if the data argument isn't provided, so are nextNode and previousNode arguments.
	def __init__(self, data = None, nextNode = None, previousNode = None):

		self.data = data
		self.nextNode = nextNode
		self.previousNode = previousNode



#A base class that represents a linked list data structure.
class LinkedList(object):

	#A method that performs initialisation.
	#If the head argument isn't provided, the linked list data structure remains empty. 
	def __init__(self, head = None):

		self.head = head
		self.tail = head
		self.iterationIndex = 0


	#A method that returns the concatenation of two LinkedList objects.
	#Note that the returned LinkedList is a new object, and no changes are made
	#to the original two LinkedList objects.
	def __add__(self, other):

		concatenatedList = LinkedList()

		selfDeepCopy = copy.deepcopy(self)
		selfDeepCopy.tail.nextNode = copy.deepcopy(other.head)

		concatenatedList.head = selfDeepCopy.head
		concatenatedList.tail = copy.deepcopy(other.tail)

		return concatenatedList


	#A method that defines equality between two LinkedList objects.
	def __eq__(self, other):
		
		output, currentNodeSelf, currentNodeOther = True, self.head, other.head

		while output and (not currentNodeSelf == None) and (not currentNodeOther == None):
			if not currentNodeSelf.data == currentNodeOther.data:
				output = False
			currentNodeSelf, currentNodeOther = currentNodeSelf.nextNode, currentNodeOther.nextNode

		return output


	#A method that returns the number of elements in the LinkedList object.
	def __len__(self):

		return self.Size()


	#A method that adds (some) sequence functionality to the LinkedList
	#object.
	def __getitem__(self, index):

		if self.iterationIndex >= self.Size():
			self.iterationIndex = 0
			raise IndexError
		else:
			output = self.GetAt(self.iterationIndex)
			self.iterationIndex += 1
			return output


	#A method that returns true if a linked list data structure is empty. 
	def IsEmpty(self):

		return self.head == None


	#A method that prints the linked list data structure to the screen.
	def PrintList(self):

		currentNode = self.head

		if currentNode == None:
			print("Empty list.", end = "")
		else:
			while not currentNode == None:
				print(currentNode.data, end = ", ")

				currentNode = currentNode.nextNode


	#A method that returns the size of the linked list data structure.
	def Size(self):

		currentNode, size = self.head, 0

		while not currentNode == None:
			size += 1
			currentNode = currentNode.nextNode

		return size


	#A method that returns true if the given element argument is included
	#in the linked list data structure.
	def IsInList(self, element):

		currentNode, output = self.head, False

		while not currentNode == None and not output:
			if currentNode.data == element:
				output = True
			currentNode = currentNode.nextNode 

		return output


	#A method that returns an adequate node if the given data argument is included in the
	#linked list data structure.
	def FindNode(self, data):

		currentNode, output = self.head, None

		while not currentNode == None and output == None:
			if currentNode.data == data:
				output = currentNode
			currentNode = currentNode.nextNode

		return output


	#A method that returns the node at given index argument.
	#If index is out of range, None is returned.
	def GetAt(self, index):

		output = None

		if index in range(0, self.Size()):
			currentNode, currentNodeIndex = self.head, 0
			while not currentNodeIndex == index:
				currentNode, currentNodeIndex = currentNode.nextNode, currentNodeIndex + 1
			output = currentNode

		return output


#A class that represents a singly linked list data structure.
class SinglyLinkedList(LinkedList):

	#A method that adds an element to the front end of the singly linked list
	#data structure.
	def AddElementFront(self, data):

		newHead = SinglyLinkedListNode(data, self.head)

		if self.IsEmpty():
			self.tail = newHead
		self.head = newHead


	#A method that adds an element to the back end of the singly linked list
	#data structure.
	def AddElementBack(self, data):

		newTail = SinglyLinkedListNode(data)

		if self.IsEmpty():
			self.head = newTail
		else:
			self.tail.nextNode = newTail
		self.tail = newTail


	#A method that removes and returns the element at the front end of the singly linked
	#list data strucutre.
	def PopElementFront(self):

		output = None

		if self.Size() == 1:
			output = self.head
			self.head = None
			self.tail = None
		elif self.Size() > 1:
			output = self.head
			self.head = self.head.nextNode

		return output


	#A method that removes the adequate node if the given data argument is
	#included in the singly linked list data structure.
	def RemoveElement(self, data):

		currentNode, previousNode = self.head, None

		while not currentNode == None:
			if currentNode.data == data:
				if self.Size() == 1:
					self.head = None
					self.tail = None
				else:
					if currentNode == self.head:
						self.head = self.head.nextNode
					elif currentNode == self.tail:
						previousNode.nextNode = None
						self.tail = previousNode
					else:
						previousNode.nextNode = currentNode.nextNode
			previousNode = currentNode
			currentNode = currentNode.nextNode


	#A method that removes an adequate node, if the node argument is part
	#of the singly linked list data structure.
	def DeleteMiddleNode(self, node):

		currentNode = self.head

		while not currentNode == None:
			if currentNode.nextNode.data == node.data:
				currentNode.nextNode = node.nextNode
				break
			currentNode = currentNode.nextNode



#A class that represents a doubly linked list data structure.
class DoublyLinkedList(LinkedList):

	#A method that adds an element to the front end of the doubly linked list
	#data structure.
	def AddElementFront(self, data):

		newHead = DoublyLinkedListNode(data, self.head)

		if self.IsEmpty():
			self.tail = newHead
		else:
			self.head.previousNode = newHead
		self.head = newHead


	#A method that adds an element to the back end of the doubly linked list
	#data structure.
	def AddElementBack(self, data):

		newTail = DoublyLinkedListNode(data)

		if self.IsEmpty():
			self.head = newTail
		else:
			newTail.previousNode = self.tail
			self.tail.nextNode = newTail
		self.tail = newTail


	#A method that removes and returns the element at the front end of the doubly linked
	#list data strucutre.
	def PopElementFront(self):

		output = None

		if self.Size() == 1:
			output = self.head
			self.head = None
			self.tail = None
		elif self.Size() > 1:
			output = self.head
			self.head.nextNode.previousNode = None
			self.head = self.head.nextNode

		return output


	#A method that removes and returns the element at the back end of the doubly linked
	#list data strucutre.
	def PopElementBack(self):

		output = None

		if self.Size() == 1:
			output = self.tail
			self.tail = None
			self.head = None
		elif self.Size() > 1:
			output = self.tail
			self.tail.previousNode.nextNode = None
			self.tail = self.tail.previousNode

		return output


	#A method that removes the adequate node if the given data argument is
	#included in the doubly linked list data structure.
	def RemoveElement(self, data):

		currentNode, previousNode = self.head, None

		while not currentNode == None:
			if currentNode.data == data:
				if self.Size() == 1:
					self.head = None
					self.tail = None
				else:
					if currentNode == self.head:
						self.head.nextNode.previousNode = None
						self.head = self.head.nextNode
					elif currentNode == self.tail:
						previousNode.nextNode = None
						self.tail = previousNode
					else:
						previousNode.nextNode = currentNode.nextNode
						currentNode.nextNode.previousNode = previousNode 
			previousNode = currentNode
			currentNode = currentNode.nextNode


