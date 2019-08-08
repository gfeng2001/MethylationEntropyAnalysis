module load numpy
set -x
mkdir -p JPJSD
#echo "started Analysis" | mail -s "JPJSD info" gfeng2001@gmail.com
#echo "started Analysis" | mail -s "JPJSD info" hayan.lee@stanford.edu
for c in M Y 21 22 18 20 13 15 14 X 16 19 9 17 8 12 11 10 4 6 5 7 3 2 1; do
#for c in 9 17 8 12 11 10 4 6 5 7 3 2 1; do
  date  
  echo chr$c
  #./JP0803.py chr$c 100 10 2> JPJSD/chr$c.jp.bed
  ./JPAnalysis.py JPJSD/chr$c.jp.bed > JPJSD/chr$c.jp.info.bed
  #echo "chr$c" | mail -s "JPJSD" gfeng2001@gmail.com
  #echo "chr$c" | mail -s "JPJSD" hayan.lee@stanford.edu
done;
echo "finished Analysis" | mail -s "JPJSD info" gfeng2001@gmail.com
echo "finished Analysis" | mail -s "JPJSD info" hayan.lee@stanford.edu
date

