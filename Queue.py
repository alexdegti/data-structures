from List import SinglyLinkedListNode, SinglyLinkedList
import copy

#A class that represents a queue data structure.
#Implemented utilising a singly linked list data structure.
class Queue(object):

	#A method that performs initialisation.
	#If beginning is not provided, the new Queue object remains empty.
	def __init__(self, beginning = None):

		if not beginning == None:
			beginning = SinglyLinkedListNode(beginning)
			self.queue = SinglyLinkedList(beginning)
		else:
			self.queue = SinglyLinkedList()


	#A method that returns true if one queue data structure equals another one.
	#Note that the comparison is defined by singly linked list data structure's equality.
	def __eq__(self, other):

		return self.queue == other.queue


	#A method that adds an element to the queue data structure.
	def Add(self, data):

		self.queue.AddElementBack(data)


	#A method that returns a copy of the element at the beginning of the
	#queue data structure.
	def Peek(self):

		return copy.deepcopy(self.queue.head)


	#A method that returns the element at the beginning of the
	#queue data structure.
	def Remove(self):

		if self.queue.Size() == 1:
			self.queue.tail = None
			
		output, self.queue.head = self.queue.head, self.queue.head.nextNode

		return output


	#A method that returns true if the queue data structure is empty.
	def IsEmpty(self):

		return self.queue.Size() == 0


	#A method that prints the queue data structure to the screen.
	def PrintQueue(self):

		if self.IsEmpty():
			print("Empty queue.")
		else:
			self.queue.PrintList()


