#!/bin/bash

sizes=(big little)
benchmarks=(matmul)

for size in "${sizes[@]}"
    do for benchmark in "${benchmarks[@]}"
        do
        gem5/build/ALL/gem5.opt -re --outdir=results_new_2/$size/$benchmark run.py $size $benchmark &
    done
done

