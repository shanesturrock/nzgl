load 'common.gnu'
load 'defs.gnu'

set out 'io.eps'

set xlabel "Runtime [h] 00:01:25"
set ylabel "I/O MiB/s"
set yrange [0.005:2000]
set logscale y
set ytics ("10^{-3}" 0.001, "10^{-2}" 0.01, "10^{-1}" 0.1, "10^{0}" 1, "10^{1}" 10, "10^{2}" 100, "10^{3}" 1000)

plot      '4.13.Butterfly.sum' using 1:(fm*($23+$24)) title "Butterfly" ls 1
