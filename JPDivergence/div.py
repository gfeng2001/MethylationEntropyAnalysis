#!/usr/bin/env python

import numpy as np

def KLD(d1, d2):
  s = 0.0
  
  for k in d1:
    p1 = d1[k]
    p2 = d2[k]
    s += p1*np.log(p1/p2)
  
  return s

def JSD(d1, d2, m):
  return (KLD(d1, m) + KLD(d2, m))/2
