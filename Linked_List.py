#!/usr/bin/env python3

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
			if self._next is not None:
				self._next._prev = self._prev
				self._next = None

			if self._prev is not None:
				self._prev._next = self._next
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

	def __init__(self):
		self._head = self._Node()
		self._tail = self._Node()
		self._head._next = self._tail
		self._tail._prev = self._head

	def __len__(self):
		count = 0
		for _ in self._head:
			count += 1
		return count

	def append_element(self, val):
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
		self._Node(val, before=self._node_at(index))

	def remove_element_at(self, index):
		self._node_at(index)._unlink()

	def get_element_at(self, index):
		return self._node_at(index)._value

	def __iter__(self):
		for node in self._head:
			yield node._value

	def __str__(self):
		return '[%s]' % ', '.join(str(value) for value in self)

if __name__ == '__main__':
	l = Linked_List()
	l.append_element(101)
	l.append_element(102)
	l.append_element(103)
	l.append_element(104)
	l.append_element(105)
	print(str(l))

