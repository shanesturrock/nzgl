load 'common.gnu'
load 'defs.gnu'

set out 'cpu.eps'

set xlabel "Runtime [h] 00:01:25"
set ylabel "Core Utilization"
set yrange [0:ncpu]

plot      '5.13.Butterfly.sum' using 1:($19/100) title "Butterfly" ls 1
