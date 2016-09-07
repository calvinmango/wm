#!/bin/env python3

"""Sort.py
Team Shamrock

Project 1: A Battle of Sorts
The purpose of this program is to test and compare the speed of the insertion
sort and and selection sort. 

The sorting algorithms are tested on three different types of arrays
(increasing order, decreasing order, random order) of five different lengths 
(1000 ints, 2500 ints, 5000 ints, 7500 ints, 10000 ints).  Each test is
timed and the results are printed to the screen. One run of the program will
generate and print a total of 30 timings. 
"""

import time
import random
import pprint
import sys

#if __name__ == '__main__':
#	class timed_call:
#		def __init__(self, func):
#			self.func = func
#			self.timings = []
#		def __call__(self, *args, **kwargs):
#			epoch = time.clock()
#			result = self.func(*args, **kwargs)
#			self.timings.append(time.clock() - epoch)
#			return result
#else:
#	timed_call = lambda x: x

def make_list(n, kind='random', dist=None):
	"""make_list creates arrays of n elements to be sorted using the
	insertion and selection sort methods.
	"""	
	if kind == 'random':
		if dist is None:
			dist = (0, n)
		return [random.randint(dist[0], dist[1]) for _ in range(n)]
	elif kind == 'increasing':
		return list(range(n))
	elif kind == 'decreasing':
		return list(range(n))[::-1]
	else:
		raise ValueError('Unknown kind: %r' % kind)

#@timed_call
def insertion_sort(a):
	"""insertion_sort sorts an array (a) using insertion sort. Starting with
	the value in a[1] , the value of the current cell is compared to the
	value in previous cell and swapped if it is less than the value it is
	compared to.
	"""	
	for i in range(len(a)):
		for j in range(i, 0, -1):
			if a[j - 1] <= a[j]:
				break
			a[j - 1], a[j] = a[j], a[j -1]

#@timed_call
def selection_sort(a):
	"""selection_sort sorts an array (a) using selection sort. Each cell is
	checked for the lowest value in the array. After the minimum is 
	found, it is moved to the earliest open cell in the array. The rest of
	the unsorted array is then searched for the new minimum and so on until
	the array is fully sorted.
	"""	
	for j in range(len(a)):
		min = a[j]
		for i in range(j, len(a)):
			if a[i] < min:
				min, a[i] = a[i], min
		a[j] = min

def insertion_sorted(a):
	a = list(a)
	insertion_sort(a)
	return a

def selection_sorted(a):
	a = list(a)
	selection_sort(a)
	return a

#if __name__ == '__main__':
#	timings = {}
#
#	for kind in ['random', 'increasing', 'decreasing']:
#		for n in [1000, 2500, 5000, 7500, 10000]:
#			a = make_list(n, kind=kind)
#			for _ in range(5):
#				selection_sorted(a)
#
#			timings['selection-%s-%i' % (kind, n)] = selection_sort.timings
#			print('selection', kind, n, sum(selection_sort.timings)/len(selection_sort.timings), file=sys.stderr)
#			selection_sort.timings = []
#
#			for _ in range(5):
#				insertion_sorted(a)
#
#			timings['insertion-%s-%i' % (kind, n)] = insertion_sort.timings
#			print('insertion', kind, n, sum(insertion_sort.timings)/len(insertion_sort.timings), file=sys.stderr)
#			insertion_sort.timings = []
#
#	for name, timings in sorted(timings.items()):
#		print(name)
#		print(timings)
#		print(sum(timings)/len(timings))

def main():
	"""The sorting functions are tested. 30 timings are printed according
	to the program specifications. Each array created is timed twice, once
	with insertion sort, once with selection sort. 
	"""
	# Increasing 1000
	array = make_list(1000, 'increasing')

	start = time.clock()
	insertion_sorted(array)
	end = time.clock()

	
	print('One Thousand Increasing Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()
	
	print('One Thousand Increasing Selection: ' + '{:.20f}'.format(end-start))
	print()
	
	
	# Decreasing 1000
	array = make_list(1000, 'decreasing')

	start = time.clock()
	insertion_sorted(array)
	end = time.clock()
	
	print('One Thousand Decreasing Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()
	
	print('One Thousand Decreasing Selection: ' + '{:.20f}'.format(end-start))
	print()
	
	
	# Random 1000
	array = make_list(1000, 'random')

	start = time.clock()
	insertion_sorted(array)
	end = time.clock()
	
	
	print('One Thousand Random Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()
	
	print('One Thousand Random Selection: ' + '{:.20f}'.format(end-start))
	print()
	
	
	# Increasing 2500
	array = make_list(2500, 'increasing')
	
	start = time.clock()
	insertion_sorted(array)
	end = time.clock()
	
	print('Two Thousand Five Hundred Increasing Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()	
	
	print('Two Thousand Five Hundred Increasing Selection: ' + '{:.20f}'.format(end-start))
	print()
	
	
	# Decreasing 2500
	array = make_list(2500, 'decreasing')
	
	start = time.clock()
	insertion_sorted(array)
	end = time.clock()
	
	print('Two Thousand Five Hundred Decreasing Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()
	
	print('Two Thousand Five Hundred Decreasing Selection: ' + '{:.20f}'.format(end-start))
	print()
	
	
	# Random 2500
	array = make_list(2500, 'random')
	
	start = time.clock()
	insertion_sorted(array)
	end = time.clock()

	print('Two Thousand Five Hundred Random Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()
	
	print('Two Thousand Five Hundred Random Selection: ' + '{:.20f}'.format(end-start))
	print()
	
	
	# Increasing 5000
	array = make_list(5000, 'increasing')
	
	start = time.clock()
	insertion_sorted(array)
	end = time.clock()	
	
	print('Five Thousand Increasing Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()
	
	print('Five Thousand Increasing Selection: ' + '{:.20f}'.format(end-start))
	print()
	
	
	# Decreasing 5000
	array = make_list(5000, 'decreasing')
	
	start = time.clock()
	insertion_sorted(array)
	end = time.clock()	
	
	print('Five Thousand Decreasing Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()
	
	print('Five Thousand Decreasing Selection: ' + '{:.20f}'.format(end-start))
	print()
	
	
	# Random 5000
	array = make_list(5000, 'random')
	
	start = time.clock()
	insertion_sorted(array)
	end = time.clock()	

	print('Five Thousand Random Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()
	
	print('Five Thousand Random Selection: ' + '{:.20f}'.format(end-start))
	print()
	
	
	# Increasing 7500
	array = make_list(7500, 'increasing')
	
	start = time.clock()
	insertion_sorted(array)
	end = time.clock()	
	
	print('Seven Thousand Five Hundred Increasing Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()
	
	print('Seven Thousand Five Hundred Increasing Selection: ' + '{:.20f}'.format(end-start))
	print()
	
	
	# Decreasing 7500
	array = make_list(7500, 'decreasing')
	
	start = time.clock()
	insertion_sorted(array)
	end = time.clock()	
	
	print('Seven Thousand Five Hundred Decreasing Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()
	
	print('Seven Thousand Five Hundred Decreasing Selection: ' + '{:.20f}'.format(end-start))
	print()
	
	
	# Random 7500
	array = make_list(7500, 'random')
	
	start = time.clock()
	insertion_sorted(array)
	end = time.clock()	

	print('Seven Thousand Five Hundred Random Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()
	
	print('Seven Thousand Five Hundred Random Selection: ' + '{:.20f}'.format(end-start))
	print()
	
	
	# Increasing 10000
	array = make_list(10000, 'increasing')
	
	start = time.clock()
	insertion_sorted(array)
	end = time.clock()	

	print('Ten Thousand Increasing Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()
	
	print('Ten Thousand Increasing Selection: ' + '{:.20f}'.format(end-start))
	print()
	
	
	# Decreasing 10000
	array = make_list(10000, 'decreasing')
	
	start = time.clock()
	insertion_sorted(array)
	end = time.clock()	

	print('Ten Thousand Decreasing Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()
	
	print('Ten Thousand Decreasing Selection: ' + '{:.20f}'.format(end-start))
	print()
	
	
	# Random 10000
	array = make_list(10000, 'random')
	
	start = time.clock()
	insertion_sorted(array)
	end = time.clock()	

	print('Ten Thousand Random Insertion: ' + '{:.20f}'.format(end-start))
	
	start = time.clock()
	selection_sorted(array)
	end = time.clock()
	
	print('Ten Thousand Random Selection: ' + '{:.20f}'.format(end-start))
	print()

if __name__ == '__main__':
	main()

