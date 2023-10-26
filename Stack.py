from List import SinglyLinkedListNode, SinglyLinkedList
import copy

#A class that represents a stack data structure.
#Implemented utilising a singly linked list data structure.
class Stack(object):

	#A method that performs initialisation.
	#If top is not provided, the new Stack object remains empty.
	def __init__(self, top = None):

		if not top == None:
			top = SinglyLinkedListNode(top)
			self.stack = SinglyLinkedList(top)
		else:
			self.stack = SinglyLinkedList()


	#A method that returns true if one stack data structure equals another one.
	#Note that the comparison is defined by singly linked list data structure's equality.
	def __eq__(self, other):

		return self.stack == other.stack


	#A method that adds an element to the stack data structure.
	def Push(self, data):

		self.stack.AddElementFront(data)


	#A method that returns a copy of the element at the top of the
	#stack data structure.
	def Peek(self):

		return copy.deepcopy(self.stack.head)


	#A method that removes and returns the element at the top of
	#the stack data structure.
	def Pop(self):

		if self.stack.Size() == 1:
			self.stack.tail = None

		output, self.stack.head = self.stack.head, self.stack.head.nextNode

		return output


	#A method that returns true if the stack data structure is empty.
	def IsEmpty(self):

		return self.stack.Size() == 0


	#A method that prints the stack data structure to the screen.
	def PrintStack(self):

		if self.IsEmpty():
			print("Empty stack.")
		else:
			self.stack.PrintList()


	#A method that sorts the stack data structure.
	def Sort(self):

		#An empty stack is already sorted.
		#if not self.stack.IsEmpty():
		if not self.IsEmpty():

			#An auxiliary stack that will be eventually sorted.
			auxiliaryStack = Stack()
			auxiliaryStack.Push(self.Pop().data)

			#Pops elements from the stack, and places them in their appropriate
			#position inside the auxiliary stack.
			while not self.IsEmpty():
				element = self.Pop()
				#Searches for the right position in the auxiliary stack.
				while (not auxiliaryStack.IsEmpty()) and (element.data < auxiliaryStack.Peek().data):
					self.Push(auxiliaryStack.Pop().data)
				auxiliaryStack.Push(element.data)

			#Moves the sorted elements back to the original stack.
			while not auxiliaryStack.IsEmpty():
				self.Push(auxiliaryStack.Pop().data)


		