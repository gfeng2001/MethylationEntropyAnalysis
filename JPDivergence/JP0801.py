#!/usr/bin/env python

import sys
import datetime
import numpy as np
  
def make_matrix(c):

  fn = ["/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/chr/JP/JP.G." + c + ".bed", "/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/chr/JP9/JP9.G." + c + ".bed", "/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/chr/JP6B/JP6B.G." + c + ".bed", "/srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/chr/JPAdenoCa/JPAdenoCa.G." + c + ".bed"]
 
  allpos = set()
  for i in range(0, 4):
    print >> sys.stderr,"before f" + str(i), datetime.datetime.now()
    pos = []
    #met = []
    with open(fn[i]) as lines:
      for l in lines:
        if l.startswith('#'):
          pass
        else:
          ele = l.strip().split()
          pos.append(int(ele[1]))
          #met.append(float(ele[3]))
    
    if i == 0:
      allpos.update(pos)
      print len(allpos)
    else:
      allpos &= set(pos)
      print len(allpos)

  w, h = len(allpos), 4
  F = [[0.0 for x in range(w)] for y in range(h)]
  for i in range(0, 4):
    print >> sys.stderr,"before 2nd iteration of f" + str(i), datetime.datetime.now()
    with open(fn[i]) as lines:
      for l in lines:
       if l.startswith('#'):
         pass
       else:
         ele = l.strip().split()
         if int(ele[1]) in allpos:
           F[i].append(float(ele[3]))

  #F1 [F1==0] = 0.0005
  M = [[0.0 for x in range(w)] for y in range(h-1)]
  M[0] = np.divide(np.add(F[0], F[1]), 2)
  M[1] = np.divide(np.add(F[0], F[2]), 2)
  M[2] = np.divide(np.add(F[0], F[3]), 2)
  print >> sys.stderr,"before return", datetime.datetime.now()
  return F, M, allpos

def compute(c, l, sh):
  F, M, allpos = make_matrix(c)

  for i in range(min(allpos), max(allpos)-l+1, sh):
    F1 = F[]
    M1 = M[]
    #print >> sys.stderr, F, F.nonzero()
    jsd1 = np.sum((F[0,:]*np.log(F[0,:]/M[0,:])+F[1,:]*np.log(F[1,:]/M[0,:]))/2)
    jsd2 = np.sum((F[0,:]*np.log(F[0,:]/M[1,:])+F[2,:]*np.log(F[2,:]/M[1,:]))/2)
    jsd3 = np.sum((F[0,:]*np.log(F[0,:]/M[2,:])+F[3,:]*np.log(F[3,:]/M[2,:]))/2)

    print >> sys.stderr, "{}:{}-{}\t{:.2f}\t{:.2f}\t{:.2f}".format( c, i, i+l, jsd1, jsd2, jsd3 )
  return

def main():
  chrNumber = sys.argv[1]
  length = int(sys.argv[2])
  shift = int(sys.argv[3])
  #print("here")
  compute(chrNumber, length, shift)

if __name__ == "__main__":
    main()



