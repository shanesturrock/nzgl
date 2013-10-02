load 'common.gnu'
load 'defs.gnu'

set out 'ram.eps'

set xlabel "Runtime [h] 00:01:25"
set ylabel "RAM usage GiB"
set yrange [0:]

plot      '4.13.Butterfly.sum' using 1:(fg*$11) title "Butterfly"  ls 1
