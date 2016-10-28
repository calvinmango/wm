class Binary_Search_Tree:
	class _BST_Node:
		def __init__(self, value):
			self._value = value
			self._left = None
			self._right = None

		def insert(self, value):
			if value > self._value:
				if self._right is not None:
					self._right.insert(value)
				else:
					self._right = Binary_Search_Tree._BST_Node(value)
			elif self._value > value:
				if self._left is not None:
					self._left.insert(value)
				else:
					self._left = Binary_Search_Tree._BST_Node(value)
			else: # self._value == value
				raise ValueError('value %r already in the tree!' % value)

		def remove(self, value):
			if value > self._value:
				if self._right is None:
					raise KeyError('value %r is not in the tree' % value)
				self._right = self._right.remove(value)
			elif self._value > value:
				if self._left is None:
					raise KeyError('value %r is not in the tree' % value)
				self._left = self._left.remove(value)
			else: # self._value == value
				if self._left is None:
					return self._right
				elif self._right is None:
					return self._left
				else: # two children
					parent = None
					succ = self._right
					while succ._left is not None:
						parent = succ
						succ = succ._left

					self._value = succ._value

					if parent is None:
						self._right = succ._right
					else:
						parent._left = succ._right

					return self

		def in_order(self):
			values = []

			if self._left is not None:
				values.append(self._left.in_order())

			values.append(str(self._value))

			if self._right is not None:
				values.append(self._right.in_order())

			return ', '.join(values)

		def pre_order(self):
			values = []

			values.append(str(self._value))

			if self._left is not None:
				values.append(self._left.in_order())

			if self._right is not None:
				values.append(self._right.in_order())

			return ', '.join(values)

		def post_order(self):
			values = []

			if self._left is not None:
				values.append(self._left.in_order())

			if self._right is not None:
				values.append(self._right.in_order())

			values.append(str(self._value))

			return ', '.join(values)

		def height(self):
			pass #FIXME

	def __init__(self):
		self._root = None

	def insert_element(self, value):
		if self._root is None:
			self._root = Binary_Search_Tree._BST_Node(value)
		else:
			self._root.insert(value)

	def remove_element(self, value):
		if self._root is None:
			raise KeyError('value %r is not in the tree' % value)
		self._root = self._root.remove(value)

	def in_order(self):
		if self._root is None:
			return '[ ]'
		return '[ %s ]' % self._root.in_order()

	def pre_order(self):
		if self._root is None:
			return '[ ]'
		return '[ %s ]' % self._root.pre_order()

	def post_order(self):
		if self._root is None:
			return '[ ]'
		return '[ %s ]' % self._root.post_order()

	def get_height(self):
		
		# return an integer that represents the height of the tree.
		# assume that an empty tree has height 0 and a tree with one
		# node has height 1. This method must operate in constant time.
		pass # TODO replace pass with your implementation

	def __str__(self):
		return self.in_order()

if __name__ == '__main__':
	pass #unit tests make the main section unnecessary.

