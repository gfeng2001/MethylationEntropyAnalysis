#!/usr/bin/env python

import div
import sys

#f1 = open("/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/JP.G.bed")
#f2 = open("/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/JP9.G.bed")
#f3 = open("/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/JP6B.G.bed")
#f4 = open("/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/JPAdenoCa.G.bed")

def make_dictionary(c, s, e):

	fn1 = "/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/chr/JP/JP.G." + c + ".bed"
	f1 = open(fn1)
	fn2 = "/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/chr/JP9/JP9.G." + c + ".bed"
	f2 = open(fn2)
	fn3 = "/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/chr/JP6B/JP6B.G." + c + ".bed"
	f3 = open(fn3)
	fn4 = "/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/chr/JPAdenoCa/JPAdenoCa.G." + c + ".bed"
	f4 = open(fn4)

	d1 = {} #key is start, value is ratio
	d2 = {}
	d3 = {}
	d4 = {}

	for l in f1:
		if l.startswith('#'):
			pass
		else:
			#print l
			ele = l.strip().split()
			if int(ele[1]) < s:
				continue
			if int(ele[2]) > e:
				break
			#print "f1: ", ele[0:4]
			d1[int(ele[1])] = float(ele[3])
	
	for l in f2:
		if l.startswith('#'):
			pass
		else:
			#print l
			ele = l.strip().split()
			if int(ele[1]) < s:
				continue
			if int(ele[2]) > e :
                       		break
			#print "f2: ", ele[0:4]
               		d2[int(ele[1])] = float(ele[3])

	for l in f3: 
                if l.startswith('#'):
                        pass
                else:
                        #print l
                        ele = l.strip().split()
                        if int(ele[1]) < s:
                                continue
                        if int(ele[2]) > e :
                               	break 
                       	#print "f3: ", ele[0:4]
                       	d3[int(ele[1])] = float(ele[3])

	for l in f4: 
                if l.startswith('#'):
                        pass
                else:
                        #print l
                        ele = l.strip().split()
			if int(ele[1]) < s:
                                continue
                        if int(ele[2]) > e :
                                break 
                        #print "f4: ", ele[0:4]
                        d4[int(ele[1])] = float(ele[3])
	
	all_pos =  set(d1.keys()) | set(d2.keys()) | set(d3.keys()) | set(d4.keys())
 
  	epsilon = 0.0001
 
 	for p in all_pos :
    		if p not in d1.keys() or abs(d1[p])<0.0005: d1[p] = epsilon
    		if p not in d2.keys() or abs(d2[p])<0.0005: d2[p] = epsilon
    		if p not in d3.keys() or abs(d3[p])<0.0005: d3[p] = epsilon
    		if p not in d4.keys() or abs(d4[p])<0.0005: d4[p] = epsilon

	return d1, d2, d3, d4

def compute(c, s, e, l, sh):
	r = make_dictionary(c, s, e)
	h = int((e-l-s)/sh)+1
	for i in range(s, e-l+sh, sh):
		X = [k for k in r[0].keys() if i<=k<=i+l]
		d1 = {}
		d2 = {}
		d3 = {}
		d4 = {}
		for x in X:
			d1[x] = r[0][x]
			d2[x] = r[1][x]
			d3[x] = r[2][x]
			d4[x] = r[3][x]
		jsd1 = div.JSD(d1, d2)
		jsd2 = div.JSD(d1, d3)
		jsd3 = div.JSD(d1, d4)
			 
		print "{}:{}-{}\t{:.2f}\t{:.2f}\t{:.2f}".format( c, i, i+l, jsd1, jsd2, jsd3 )
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
