# Research Plan for Gilbert

## 1. Background training

## 1.1. SCG4 account set up
Alex Chekholko <chekh@stanford.edu>

- [x] SUnetID
- [x] dual authentication
- [x] vpn (https://uit.stanford.edu/service/vpn/)
- [x] scg4

## 1.2. Jupyter Python
- [x] kmer counting in E.coli (<a href="K-mer Counting.ipynb">link</a>) Gilbert
- [ ] [matplotlib](http://matplotlib.org/users/pyplot_tutorial.html)
- [ ] [Markdown tutorial](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)


## 1.3. Literatures
- [ ] [BSMAP: whole genome bisulfite sequence MAPping program](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-10-232)
- [ ] [MOABS: model based analysis of bisulfite sequencing data](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2014-15-2-r38)


# 2. Projects

## 2.1. Project 1 : Uniq k-mer counting
### 2.1.1. Theory
* The concept of K-mer
* Biology
  * DNA-seq
  
### 2.2.1. Implementation
* Input : E.coli genome
* Output 
  * The number of uniq kmers given various K

## 2.2. Project 2 : Select microsatellites candidate region using entropy 
### 2.2.1. Theory
* Information thoery
  * Entropy
* Biology
  * microsatellites
  * Tandem repeat

### 2.2.1. Implementation
* input : E.coli genome, K-mer
* output : Entropy given K-mer and position
  * graph1 : position (x-axis) vs. entropy (y-axis) (K=15,30,60), for the first ~160bp
  * graph1 : position (x-axis) vs. entropy (y-axis) (K=15,30,60), for the whole genome, hint : sampling
  * The min and max entropy -> extract sequence K bp before and after window.
  * graph2 : histogram of entropy given K=10, x-axis is entropy.
  * graph3 : average of enropy for K=4..28


## 2.3. todo
* Project 2
  * add entropy theory with formular, google 'latex' 
  * graph1: add legend
  * graph2: remove black edge
  * graph3: add point marker, filled circle. 

* Summarize BSMAP
  * methylation 
  * How does Bisulfite sequencing work
  * the algorithm of BSMAP
  

## 2.3. DMR

