#!/usr/bin/env python3

import unittest
from Deque import Deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):

  def setUp(self):
    self._deque = Deque()
    self._stack = Stack()
    self._queue = Queue()
    
    
#Deque Tests:
    
  def test_empty_deque_string(self):
    self.assertEqual('[ ]', str(self._deque))
    
  def test_nonempty_deque_string(self):
    self._deque.push_front(5)
    self._deque.push_back(7)
    self.assertEqual('[ 5, 7 ]', str(self._deque))
    
  def test_len_empty_deque(self):
    self.assertEqual(0, len(self._deque))
    
  def test_len_nonempty_deque(self):
    self._deque.push_front(6)
    self._deque.push_back(45)
    self.assertEqual(2, len(self._deque))
    self._deque.pop_back()
    self.assertEqual(1, len(self._deque))
    
  def test_push_front_empty(self):
    self._deque.push_front(99)
    self.assertEqual('[ 99 ]', str(self._deque))
  
  def test_push_front_one(self):
    self._deque.push_front(4)
    self._deque.push_front(54)
    self.assertEqual('[ 54, 4 ]', str(self._deque))    
    
  def test_pop_front_empty(self):
    with self.assertRaises(IndexError):
      self._deque.pop_front()
    self.assertEqual('[ ]', str(self._deque))
    
  def test_pop_front_one(self):
    self._deque.push_front(89)
    self.assertEqual(89, self._deque.pop_front())
    self.assertEqual('[ ]', str(self._deque))
    
  def test_pop_front_three(self):
    self._deque.push_front(70)
    self._deque.push_front(44)
    self._deque.push_front(6)
    self.assertEqual(6, self._deque.pop_front())
    self.assertEqual('[ 44, 70 ]', str(self._deque))
  
  def test_peek_front_empty(self):
    with self.assertRaises(IndexError):
      self._deque.peek_front()
    self.assertEqual('[ ]', str(self._deque))
    
  def test_peek_front_one(self):
    self._deque.push_front(89)
    self.assertEqual(89, self._deque.peek_front())
    self.assertEqual('[ 89 ]', str(self._deque))
    
  def test_peek_front_three(self):
    self._deque.push_front(70)
    self._deque.push_front(44)
    self._deque.push_front(6)
    self.assertEqual(6, self._deque.peek_front())
    self.assertEqual('[ 6, 44, 70 ]', str(self._deque))

  def test_push_back_empty(self):
    self._deque.push_back(99)
    self.assertEqual('[ 99 ]', str(self._deque))
  
  def test_push_back_one(self):
    self._deque.push_back(4)
    self._deque.push_back(54)
    self.assertEqual('[ 4, 54 ]', str(self._deque))
  
  def test_pop_back_empty(self):
    with self.assertRaises(IndexError):
      self._deque.pop_back()
    self.assertEqual('[ ]', str(self._deque))
    
  def test_pop_back_one(self):
    self._deque.push_back(89)
    self.assertEqual(89, self._deque.pop_back())
    self.assertEqual('[ ]', str(self._deque))
    
  def test_pop_back_three(self):
    self._deque.push_back(70)
    self._deque.push_back(44)
    self._deque.push_back(6)
    self.assertEqual(6, self._deque.pop_back())
    self.assertEqual('[ 70, 44 ]', str(self._deque))
  
  def test_peek_back_empty(self):
    with self.assertRaises(IndexError):
      self._deque.peek_back()
    self.assertEqual('[ ]', str(self._deque))
    
  def test_peek_back_one(self):
    self._deque.push_back(89)
    self.assertEqual(89, self._deque.peek_back())
    
  def test_peek_back_three(self):
    self._deque.push_back(70)
    self._deque.push_back(44)
    self._deque.push_back(6)
    self.assertEqual(6, self._deque.peek_back()) 
    
    
#Queue Tests:

  def test_empty_queue_string(self):
    self.assertEqual('[ ]', str(self._queue))
    
  def test_nonempty_queue_string(self):
    self._queue.enqueue(33)
    self._queue.enqueue(5)
    self.assertEqual('[ 33, 5 ]', str(self._queue))
    
  def test_len_empty_queue(self):
    self.assertEqual(0, len(self._queue))
    
  def test_nonempty_queue(self):
    self._queue.enqueue(4)
    self._queue.enqueue(8)
    self.assertEqual(2, len(self._queue))
    self.assertEqual('[ 4, 8 ]', str(self._queue))
    self._queue.dequeue()
    self.assertEqual(1, len(self._queue))
    self.assertEqual('[ 8 ]', str(self._queue))
    
  def test_empty_dequeue(self):
    with self.assertRaises(IndexError):
      self._queue.dequeue()
    self.assertEqual('[ ]', str(self._queue))


#Stack Tests:

  def test_empty_stack_string(self):
    self.assertEqual('[ ]', str(self._stack))
  
  def test_nonempty_stack_string(self):
    self._stack.push(9)
    self.assertEqual('[ 9 ]', str(self._stack))
    
  def test_len_empty_stack(self):
    self.assertEqual(0, len(self._stack))
    
  def test_len_nonempty_stack(self):
    self._stack.push(8)
    self._stack.push(0)
    self.assertEqual(2, len(self._stack))
    
  def test_push(self):
    self._stack.push(7)
    self.assertEqual('[ 7 ]', str(self._stack))
    self._stack.push(55)
    self.assertEqual('[ 55, 7 ]', str(self._stack))
    self._stack.push(3)
    self.assertEqual('[ 3, 55, 7 ]', str(self._stack))
    
  def test_pop(self):
    self._stack.push(9)
    self._stack.push(2)
    pop_val = self._stack.pop()
    self.assertEqual('[ 9 ]', str(self._stack))
    self.assertEqual(2, pop_val)
    self.assertEqual(9, self._stack.pop())
    self.assertEqual('[ ]', str(self._stack))
    
  def test_peek(self):
    self._stack.push(2)
    self._stack.push(1)
    self.assertEqual(1, self._stack.peek())
    self.assertEqual('[ 1, 2 ]', str(self._stack))
    
    
                    

if __name__ == '__main__':
  unittest.main(exit = False)
