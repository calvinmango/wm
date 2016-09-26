#!/usr/bin/env python3

class Linked_List:
	class _Node:
		def __init__(self, val=None, after=None, before=None):
			self._value = val

			assert after is None or before is None

			if after is not None:
				self._next = after._next
				self._prev = after
				after._next = self

				if self._next is not None:
					self._next._prev = self
			elif before is not None:
				self._next = before
				self._prev = before._prev
				before._prev = self

				if self._prev is not None:
					self._prev._next = self
			else:
				self._next = None
				self._prev = None

		def _unlink(self):
			if self._next is not None:
				self._next._prev = self._prev

			if self._prev is not None:
				self._prev._next = self._next

			self._next = None
			self._prev = None

		def __iter__(self):
			#skip first if it is a head sentinial
			if self._prev is None:
				self = self._next

			#enumerate the sublist starting from self
			while self is not None and self._next is not None:
				_next = self._next
				yield self
				self = _next

		def _skip(self, index):
			if not isinstance(index, int):
				raise IndexError('indicies must be integers not %s' % index.__class__.__name__)

			count = 0
			for node in self:
				if count == index:
					return node
				count += 1

			raise IndexError('index out of range')

		def __repr__(self):
			_prev = '0x%x' % id(self._prev) if self._prev is not None else 'None'
			_next = '0x%x' % id(self._next) if self._next is not None else 'None'
			return '_Node(_value=%r, prev=%s, next=%s)' % (self._value, _prev, _next)

	def __init__(self, items=None):
		self._head = self._Node()
		self._tail = self._Node(after=self._head)

		if items is not None:
			for item in items:
				self.append_element(item)

	def append_element(self, val):
		self._Node(val, before=self._tail)

	def insert_element_at(self, val, index):
		self._Node(val, before=self._head._skip(index))

	def remove_element_at(self, index):
		node = self._head._skip(index)
		node._unlink()
		return node._value

	def get_element_at(self, index):
		return self._head._skip(index)._value

	def __iter__(self):
		for node in self._head:
			yield node._value

	def __len__(self):
		count = 0
		for _ in self:
			count += 1
		return count

	def __str__(self):
		temp = ', '.join(str(value) for value in self)
		if temp == '':
			return '[ ]'
		else:
			return '[ %s ]' % temp

if __name__ == '__main__':
	def should_throw(code, errs, _locals=None):
		try:
			exec(code, globals(), _locals)
		except errs:
			return
		#except:
		#	raise AssertionError('raised the wrong kind of exception')
		raise AssertionError('did not raise an exception')

	l = Linked_List()
	l.append_element(101)
	l.append_element(102)
	l.append_element(103)
	l.append_element(104)
	l.append_element(105)
	l.remove_element_at(1)
	print(l)

