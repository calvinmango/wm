#RoyalFrankincense

class Linked_List:
	
	class _Node:
		
		def __init__(self, val=None, after=None, before=None):
			
			self._value = val
			self._next = None
			self._prev = None

			assert after is None or before is None

			if after is not None:
				self._next = after._next
				self._prev = after
				after._next._prev = self
				after._next = self

			if before is not None:
				self._next = before
				self._prev = before._prev
				before._prev._next = self
				before._prev = self

		def _unlink(self):
			#Unlinks names from elements for efficiency
			_prev = self._prev
			_next = self._next

			if _next is not None:
				self._next._prev = _prev
				self._next = None

			if _prev is not None:
				self._prev._next = _next
				self._prev = None

		def __iter__(self):
			#enumerates sublist starting from self
			#skips first element if it is a head sentinial
			if self._prev is None:
				self = self._next
				if self is None:
					return

			while self._next is not None:
				_next = self._next
				yield self
				self = _next

		def __repr__(self):
			_prev = '0x%x' % id(self._prev) if self._prev is not None else 'None'
			_next = '0x%x' % id(self._next) if self._next is not None else 'None'
			return '_Node(_value=%r, prev=%s, next=%s)' % (self._value, _prev, _next)

	def __init__(self):
		self._head = self._Node()
		self._tail = self._Node()
		self._head._next = self._tail
		self._tail._prev = self._head

	def __len__(self):
		#Uses count to iterate through the list and find the length
		count = 0
		for _ in self._head:
			count += 1
		return count
	

	def append_element(self, val):
		#Appends elements to the end of linked list, before the tail
		self._Node(val, before=self._tail)

	def _node_at(self, index):
		if not isinstance(index, int):
			raise IndexError('indicies must be integers not %s' % index.__class__.__name__)

		count = 0
		for node in self._head:
			if count == index:
				return node
			count += 1

		raise IndexError('index out of range')

	def insert_element_at(self, val, index):
		#Inserts element at index before the node located at that index
		self._Node(val, before=self._node_at(index))

	def remove_element_at(self, index):
		#Removes node at a specific index from linked list
		node = self._node_at(index)
		node._unlink()
		return node._value

	def get_element_at(self, index):
		#Returns the value of a node at a specific index
		return self._node_at(index)._value

	def __iter__(self):
		for node in self._head:
			yield node._value

	def __str__(self):
		#Returns formated list for printing
		temp = ', '.join(str(value) for value in self)
		if temp == '':
			return '[ ]'
		else:
			return '[ %s ]' % temp

def should_throw(code, errs, _locals=None):
	#In order to keep the program running after flagging an error, 
	#should_throw uses try/except to catch error and return nothing
	try:
		exec(code, globals(), _locals)
	except errs:
		return
	except:
		raise AssertionError('raised the wrong kind of exception')
	raise AssertionError('did not raise an exception')


if __name__ == '__main__':

	#Test Case 1
	#Test every function and if it correctly alters linked list
	l_list = Linked_List()
	l_list.append_element(101)
	l_list.append_element(102)
	l_list.append_element(103)
	l_list.append_element(104)
	l_list.append_element(105)
	print("List L: ",l_list)
	print("Length of list L: ", l_list.__len__())
	print()
	
	l_list.append_element(106)
	print("List L after append: ",l_list)
	print("Length of list L: ", l_list.__len__())
	print()
	
	l_list.insert_element_at(111, 3)
	print("List L after insert element: ",l_list)
	print("Length of list L: ", l_list.__len__())	
	print()
	
	l_list.remove_element_at(4)
	print("List L after remove: ",l_list)
	print("Length of list L: ",l_list.__len__())
	print()
	
	print("Test of printing each value in list L:")
	for val in l_list:
		print(val)
	print()
	
	#Test Case 2
	#Larger linked list, testing accuracy of element removal and insertion
	m_list = Linked_List()
	for i in range(0,20):
		m_list.append_element(i)
	print("List M: ", m_list)
	print("Length of List M: ",m_list.__len__())
	print()
	
	m_list.remove_element_at(0)
	print("List M after remove at index 0 : ", m_list)
	print("Length of List M: ",m_list.__len__())
	print()
	
	m_list.insert_element_at(55,0)
	print("List M after insert at index 0: ", m_list)
	print("Length of List M: ", m_list.__len__())
	print()
	
	m_list.remove_element_at(15)
	print("List M after remove at index 15 : ", m_list)
	print("Length of List M: ",m_list.__len__())
	print()
	
	m_list.insert_element_at(1000,15)
	print("List M after insert at index 15: ", m_list)
	print("Length of List M: ", m_list.__len__())
	print()
	
	print("Element at index 15 for list M: ",m_list.get_element_at(15))
	print()
	
	print("Element at index 5 for list M: ",m_list.get_element_at(5))
	print()	
	
	print("Element at index 0 for list M: ",m_list.get_element_at(0))
	print()	
	
	should_throw('m_list.remove_element_at(105)', IndexError)
	print("List M after invalid index(105): ", m_list)
	print("Length of List M after invalid index: ", m_list.__len__())
	print()	
	
	#Test Case 3
	#Empty linked list, calls should_throw to recognized error and allow
	#program to recognize that
	g_list = Linked_List()
	print("List G: ", g_list)
	print("Length of list G: ", g_list.__len__())
	print()
	
	should_throw('g_list.remove_element_at(1000)', IndexError)
	print("List G after invalid index(1000): ", g_list)
	print("Length of list G: ", g_list.__len__())
	print()
	
	should_throw('g_list.insert_element_at(2,0)', IndexError)
	print("List G after inserting at invalid index: ",g_list)
	print("Length of list G: ", g_list.__len__())
	print()
	
	should_throw('g_list.get_element_at(0)', IndexError)
	print("List G after getting element at invalid index: ",g_list)
	print("Length of list G: ", g_list.__len__())
	print()	

