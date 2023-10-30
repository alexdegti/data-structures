from List import DoublyLinkedList

#A class that represents a hash table object.
#Implemented utilising Python's Lists, and a DoublyLinkedList object.
class HashTable(object):

	#A method that performs initialisation.
	def __init__(self, size = 23):

		self.size = size
		self.hashTable = []

		for _ in range(self.size):
			self.hashTable.append(DoublyLinkedList())


	#A method that returns the adequate hash code for a given key.
	def HashFunction(self, key):

		return key % self.size


	#A method that adds an element to the hash table data structure.
	def AddElement(self, keyValueTuple):

		self.hashTable[self.HashFunction(keyValueTuple[0])].AddElementBack(keyValueTuple)
			

	#A method that removes an element from the hash table persuant to the
	#given key argument.
	def RemoveElement(self, key):

		currentNode = self.hashTable[self.HashFunction(key)].head

		while not currentNode == None:
			if currentNode.data[0] == key:
				self.hashTable[self.HashFunction(key)].RemoveElement(currentNode.data)
				break
			currentNode = currentNode.nextNode		


	#A method that prints the hash table data structure to the screen.
	def PrintHashTable(self):

		for element in self.hashTable:
			element.PrintList()
			print()


