module load numpy
set -x
#./JP.py chr22 100 10 2> small.jp
echo "started" | mail -s "JPJSD" gfeng2001@gmail.com
for c in Y; do
  date  
  echo chr$c
  ./JP0725.py chr$c 100 10 2> JPJSD/chr$c.jp
  echo "chr$c" | mail -s "JPJSD" gfeng2001@gmail.com
done;
echo "done" | mail -s "JPJSD" gfeng2001@gmail.com
date

