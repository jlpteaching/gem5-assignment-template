# Assignment 1 Questions

**IMPORTANT** Do not reformat this file!
Put your answers below each question.
Use markdown formatting.

## [25 points] How to reproduce the results

### Explanation of the script

### Script to run

### Parameters to script (if any)

### Example command to run the script

```shell
gem5
```

## [75 points] Questions

### [5 points each] Step I: Write down your hypotheses and experimental setup

1. When you change the ISA from RISC-V to x86, what do you expect to happen to the performance of the system? Use the Iron Law of Performance to justify your answer.

2. When you change the CPU frequency from 1GHz to 4GHz, what do you expect to happen to the performance of the system? Use the Iron Law of Performance to justify your answer.

3. When you change the CPU frequency from 1GHz to 4GHz, will the speedup from 1GHz to 4GHz be the same for all ISAs? Why or why not?

4. When you change the memory model from DDR3 to DDR4, what do you expect to happen to the performance of the system? Use the Iron Law of Performance to justify your answer.

### [5 points each] Step II: Investigating the impact of the ISA

1. What is the *performance* for matrix multiplication for each ISA?

2. Can you match the difference in performance to the Iron Law of Performance? Why or why not?

### [5 points each] Step III: Investigating the impact of the CPU and cache clock frequency

1. What is the speedup of the system when you change the CPU and cache frequency from 1GHz to 2GHz to 4GHz? Show the speedup for each ISA.

2. Does the Iron Law of Performance correctly predict the speedup for each ISA? Why or why not?

### [5 points each] Step IV: Investigating the impact of the memory model

1. What is the speedup of DDR4 and LPDDR5 memory models compared to DDR3? Show the speedup for each ISA.

2. What part of the Iron Law of Performance is most affected by changing the memory architecture?

### [25 points] Research question:

*For a simple CPU model (i.e., fixed microarchitecture), does ISA, memory, or technology make a bigger impact on system performance?*

### [10 points] Next steps

1. If the workload had a significantly better (lower) CPI, how would that change the results of the experiments? E.g., what would happen if the workload and microarchitecture supported a CPI of 0.25 (or 4 instructions per cycle)?
