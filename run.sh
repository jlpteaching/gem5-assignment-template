#!/bin/bash

cpu_types=(TimingSimpleCPU MinorCPU)
cpu_freqs=(1GHz 2GHz 4GHz)
memory_types=(DDR3_1600_8x8 DDR3_2133_8x8 LPDDR3_1600_1x32)

for cpu_type in "${cpu_types[@]}"
    do for cpu_freq in "${cpu_freqs[@]}"
        do for memory_type in "${memory_types[@]}"
            do
            gem5 -re --outdir=results/$cpu_type/$cpu_freq/$memory_type run.py $cpu_type $cpu_freq $memory_type
        done
    done
done
