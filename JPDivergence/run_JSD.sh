

e=`tail -n1 /srv/gsfs0/projects/snyder/hayanlee/projects/FAP/pipeline/04_moabs/chr/JP6B/JP6B.G.chr11.bed | awk '{print $3}'`
echo $e
#./JPDivergence.py chr11:707500-$e 100 10
./JPDivergence.py chr11:707500-709500 100 10 > small.jsd
