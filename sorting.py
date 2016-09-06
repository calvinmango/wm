# Sort.py
# Team Shamrock
#
# Project 1: A Battle of Sorts
# The purpose of this program is to test and compare the speed of the insertion 
# sort and and selection sort. 
# 
# The sorting algorithms are tested on three different types of arrays
# (increasing order, decreasing order, random order) of five different lengths 
# (1000 ints, 2500 ints, 5000 ints, 7500 ints, 10000 ints).  Each test is
# timed and the results are printed to the screen. One run of the program will
# generate and print a total of 30 timings. 

import time
import random
import pprint
import sys

def make_list(n, kind= 'random', dist=None):
	"""
	This function creates arrays to be sorted using the insertion and
	selection sort methods.
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
	

def insertion_sorted(a):
	"""
	This function sorts an array (a) using insertion sort. Starting with
	the value in a[1] , the value of the current cell is compared to the
	value in previous cell and swapped if it is less than the value it is
	compared to.
	"""	
	a = list(a)
	for i in range(len(a)):
		for j in range(i, 0, -1):
			if a[j - 1] <= a[j]:
				break
			a[j - 1], a[j] = a[j], a[j -1]
	return a

def selection_sorted(a):
	"""
	This function sorts an array (a) using selection sort. Each cell is 
	checked for the lowest value in the array. After the minimum is 
	found, it is moved to the earliest open cell in the array. The rest of
	the unsorted array is then searched for the new minimum and so on until
	the array is fully sorted.
	"""	
	a = list(a)
	for j in range(len(a)):
		min = a[j]
		for i in range(j, len(a)):
			if a[i] < min:
				min, a[i] = a[i], min
		a[j] = min
	return a
	
def main():
	"""
	The sorting functions are tested. 30 timings are printed according
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
