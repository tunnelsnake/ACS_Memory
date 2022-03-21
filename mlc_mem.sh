#!/bin/bash

# Test Memory Performance:
# We aim to observe the tradeoff of throughput and latency
for STRIDE in 64 256
do
    # Run with -W2, -W3, -W4, -W5
    # W2: 
    # W3:
    # W4:
    # W5:
    for I in 2 3 4 5
    do
        echo "mlc --loaded_latency -W$I -l$STRIDE > output/mem_${I}_${STRIDE}.txt"
        mlc --loaded_latency -W$I -l$STRIDE > output/mem_${I}_${STRIDE}.txt
    done
done