#!/usr/bin/env python3

import time
import random
from pprint import pprint
import sys

def make_list(n, dist=None, kind='random'):
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

class timed_call:
	def __init__(self, func):
		self.func = func
		self.timings = []
	def __call__(self, *args, **kwargs):
		epoch = time.clock()
		result = self.func(*args, **kwargs)
		self.timings.append(time.clock() - epoch)
		return result

@timed_call
def insertion_sorted(a):
	a = list(a)
	for i in range(len(a)):
		for j in range(i, 0, -1):
			if a[j - 1] <= a[j]:
				break
			a[j - 1], a[j] = a[j], a[j -1]
	return a

@timed_call
def selection_sorted(a):
	a = list(a)
	for j in range(len(a)):
		least = a[j]
		for i in range(j + 1, len(a)):
			if a[i] >= least:
				break
			least, a[i] = a[i], least
		a[j] = least
	return a

def main():
	timings = {}

	for kind in ['random', 'increasing', 'decreasing']:
		for n in [1000, 2500, 5000, 7500, 10000]:
			a = make_list(n, kind=kind)
			for _ in range(5):
				selection_sorted(a)

			timings['selection-%s-%i' % (kind, n)] = selection_sorted.timings
			print('selection', kind, n, sum(selection_sorted.timings)/len(selection_sorted.timings), file=sys.stderr)
			selection_sorted.timings = []

			for _ in range(5):
				insertion_sorted(a)

			timings['insertion-%s-%i' % (kind, n)] = insertion_sorted.timings
			print('insertion', kind, n, sum(insertion_sorted.timings)/len(insertion_sorted.timings), file=sys.stderr)
			insertion_sorted.timings = []

	for name, timings in sorted(timings.items()):
		print(name)
		print(timings)
		print(sum(timings)/len(timings))

if __name__ == '__main__':
	main()

