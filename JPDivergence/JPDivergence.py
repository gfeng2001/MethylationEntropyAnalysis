#!/usr/bin/env python

import div
import sys

f1 = open("/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/JP.G.bed")
f2 = open("/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/JP9.G.bed")
f3 = open("/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/JP6B.G.bed")
f4 = open("/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/JPAdenoCa.G.bed")

def make_dictionary(c, s, e):

	d = {} #key is start, value is ratio
	d2 = {}
	d3 = {}
	d4 = {}

	for l in f1:
		if l.startswith('#'):
			pass
		else:
			#print l
			ele = l.strip().split()
			if ele[0] == c:
				if int(ele[1]) < s:
					continue
				if int(ele[2]) > e:
					break
				print "f1: ", ele[0:4]
				d[int(ele[1])] = float(ele[3])
	
	for l in f2:
		if l.startswith('#'):
			pass
		else:
			#print l
			ele = l.strip().split()
			if ele[0] == c:
				if int(ele[1]) < s:
					continue
				if int(ele[2]) > e :
                        		break
				print "f2: ", ele[0:4]
                		d2[int(ele[1])] = float(ele[3])

	for l in f3: 
                if l.startswith('#'):
                        pass
                else:
                        #print l
                        ele = l.strip().split()
			if ele[0] == c:
                        	if int(ele[1]) < s:
                                	continue
                        	if int(ele[2]) > e :
                                	break 
                        	print "f3: ", ele[0:4]
                        	d3[int(ele[1])] = float(ele[3])

	for l in f4: 
                if l.startswith('#'):
                        pass
                else:
                        #print l
                        ele = l.strip().split()
                        if ele[0] == c:
				if int(ele[1]) < s:
                                	continue
                        	if int(ele[2]) > e :
                                	break 
                        	print "f4: ", ele[0:4]
                        	d4[int(ele[1])] = float(ele[3])
	

	return d1, d2, d3, d4

def compute(c, s, e, l, sh):
	r = make_dictionary(c, s, e)
	h = int((e-l-s)/sh)+1
	for i in range(0, h):
		a = div.JSD(r[i])
		print "{}:{}-{}\t{:.2f}\t{:.2f}\t{:.2f}".format( c, s+sh*i, s+sh*i+l, jsd[0], jsd[1], jsd[2] )
	return

i =  sys.argv[1]
chrNumber = i.split(':')[0]
r = i.split(':')[1]

start = int(r.split('-')[0])
#end = int(i.split('-')[1])
end = int(r.split('-')[1])
length = int(sys.argv[2])
shift = int(sys.argv[3])

compute(chrNumber, start, end, length, shift)
