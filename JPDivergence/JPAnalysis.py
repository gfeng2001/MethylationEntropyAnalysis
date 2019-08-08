#!/usr/bin/env python

import sys

def main():
  fn = sys.argv[1]
  with open(fn) as lines:
    for l in lines:
      i = l.strip().split()
      if float(i[3])>0 and float(i[4])>float(i[3]) and float(i[5])>float(i[4]):
          print l.strip()

if __name__ == "__main__":
  main()

