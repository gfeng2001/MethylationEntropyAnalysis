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
- [ ] [Latex in Jupyter notebook](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Typesetting%20Equations.html)


## 1.3. Literatures
- [ ] [BSMAP: whole genome bisulfite sequence MAPping program](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-10-232)
- [ ] [MOABS: model based analysis of bisulfite sequencing data](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2014-15-2-r38)


# 2. Projects

## Project 1 : Uniq k-mer counting
### 2.1.1. Theory
* The concept of K-mer
* Biology
  * DNA-seq
  
### 2.2.1. Implementation
* Input : E.coli genome
* Output 
  * The number of uniq kmers given various K

## Project 2 : Select microsatellites candidate region using entropy 
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


## Project 3 : KL Divergence
### 2.3.1. Theory
* Information thoery
  * Entropy
* Biology
  * Methylation
  * Bisulfite sequencing
  * DMR (Differentially Methylated Region)
### 2.3.1. Implementation
* KL Divergence : <a href="KL divergence.ipynb">theory and practice</a>


## Project 4 : JSD for methylation data
### Software
#### JSD modification 
 1. Read 4 files
 2. make a set of positions for each
 3. get intersection of 4 sets
 4. make 2d array of 4x(num of shared positions)
 5. fill the 2d array
 6. compute JSD as we did
 
#### Hint
 * np.nan
 * np.full
 * np.array
 * np.fill
 
 
 
  
