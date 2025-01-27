# Assignment 2 Questions

Name:
Email:
Student ID:

**IMPORTANT** Do not reformat this file!
Put your answers below each question.
Use markdown formatting.

## [25 points] How to reproduce the results

### Explanation of the script

### Script to run

### Parameters to script (if any)

### Commands used to gather data

#### Commands used for Step II

```shell

```

#### Commands used for Step III

```shell

```

```shell

```

```shell

```

## [75 points] Questions

### [10 points] Step I: Write down your hypotheses

1. For the DAXPY's assembly code, identify the ROI. In your report, copy the assembly code segment corresponding to the code between `m5_work_begin` and `m5_work_end`.

2. For the ROI of this workload, what percentage of instructions do you think will be integer, floating point, and memory operations? Explain your reasoning.

3a.Estimate how the performance will change under the following condition: If the latency of integer operations are increased from 1 to 6 cycles, but the system is pipelined.

3b.Estimate how the performance will change under the following condition: If the latency of floating point operations are increased from 6 to 12 cycles, but the system is pipelined.

3c.Estimate how the performance will change under the following condition: If the issue latency is increased from 1 to 2 cycles, but the operation latency is unchanged (1 cycle for integer and 6 cycles for floating point operations).

### [20 points] Step II: Get preliminary data on the instruction mix

1. For the ROI of this workload, what percentage of instructions are integer, floating point, and memory operations? Explain your reasoning.

2a.Estimate how the performance will change under the following condition: If the latency of integer operations are increased from 1 to 6 cycles, but the system is pipelined.

2b.Estimate how the performance will change under the following condition: If the latency of floating point operations are increased from 6 to 12 cycles, but the system is pipelined.

2c.Estimate how the performance will change under the following condition: If the issue latency is increased from 1 to 2 cycles, but the operation latency is unchanged (1 cycle for integer and 6 cycles for floating point operations).

### [15 points] Step III: Developing and running the experiments

1a. For each experiment, what is changing in the system compared to the baseline when changing the latency of integer operations.

1b. For each experiment, what is changing in the system compared to the baseline when changing the latency of floating point operations.

1c. For each experiment, what is changing in the system compared to the baseline when changing the issue latency.

2a. What is the performance change for changing the latency of integer operations.

2b. What is the performance change for changing the latency of floating point operations.

2c. What is the performance change for changing the issue latency.

### [30 points] Research questions:

1. Does changing the latency of the integer operations, floating point operations, or the issue latency have a bigger impact on the performance of the system?

2. Are these changes the main factor in the performance of the system for the DAXPY workload? If not, what other factors might be affecting the performance of the system?

### [25 points] Next steps

1. Change the clock to be higher (e.g., 4 GHz). How does a higher clock affect the answers to the two research questions?
