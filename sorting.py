#!/usr/bin/env python3

import os
import time
import random

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

def clone_list(a):
	return [elm for elm in a]

def selection_sort(a):
	pass

def main():
	a = make_list(100)
	selection_sort(a)
	print(a)

if __name__ == '__main__':
	main()

