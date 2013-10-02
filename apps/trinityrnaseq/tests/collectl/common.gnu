
set terminal postscript color eps "Times" 14 
#set termoption enhanced

set style data points

# ram and cpu
mypt1=7
mylw1=0
#myps1=0.3
myps1=0.6

set key below
set timefmt "%Y%m%d %H:%M:%S"
set xdata time
set format x "%k"
set xrange [*:*]
unset grid
set grid x
unset title
#set title "trinityrnaseq_r2013_08_14 4 /home/build/nzgl/apps/trinityrnaseq/tests/reads.left.fq" noenhanced
set title "trinityrnaseq_r2013_08_14 4 /home/build/nzgl/apps/trinityrnaseq/tests/reads.left.fq"

fm=1./(1024.0)
fg=1./(1024.0)/(1024.0)

#set multiplot layout 3,1
#set tmargin 0
#set tmargin 0.8
#set bmargin 0.8

#set tics nomirror scale 0.66
#set xtics scale 0

#myvertoffset=0.02

set style line 1 lw mylw1 pt mypt1 ps myps1
