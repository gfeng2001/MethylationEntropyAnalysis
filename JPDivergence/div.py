#!/usr/bin/env python

import numpy as np

def KLD(d1, d2):
	s = 0.0
	
	for k in set(d1.keys()) | set(d2.keys()):
		if k in d1:
			p1 = d1[k]
		else:
			p1 = 0.00001
	
		if k in d2:
			p2 = d2[k]
		else:
			p2 = 0.00001

		s += p1*np.log(p1/p2)	
	
	return s

def JSD(d1, d2):
	m = {}

	for k in d1:
		m[k] = d1[k]
	for k in d2:
		if k in d1:
			m[k] += d2[k]
		
		else:
			m[k] = d2[k]

	for k in m:
		m[k] /= 2

	return (KLD(d1, m) + KLD(d2, m))/2	
