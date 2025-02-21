# Virtual Memory Assignment Questions

Name: Email: Student ID:

**IMPORTANT** Do not reformat this file! Put your answers below each question.
Use markdown formatting.

## [25 points] How to reproduce the results

### Explanation of the script

### Script to run

### Parameters to script (if any)

### Commands used to gather data

#### Commands used for Step I (SE vs FS comparison)

Please put one command per designated line.

```shell

```

```shell

```

```shell

```

```shell

```

#### Commands used for Step III (Basic Performance Analysis)

```shell

```

```shell

```

#### Commands used for Step IV (Design Space Exploration)

```shell

```

```shell

```

```shell

```

```shell

```

## [75 + 10 points] Questions

### [20 points] Step I: SE vs FS Comparison

1. What is the difference in the number of instructions simulated between SE and
   FS modes for each workload? Why does it vary?

2. What is the difference in the number of TLB misses between SE and FS modes
   for each workload? Why does it vary?

3. What is the difference in IPC between SE and FS modes for each workload?

4. What are the differences in PTW memory accesses and dptw cache accesses in SE
   and FS modes? What can you conclude about page table walks in SE mode by
   looking at these statistics?

### [15 points] Step II: Hypothesis - Understanding the Virtual Memory System

1. What do you expect to happen to performance as you increase the TLB size?
   Why?

2. What do you expect to happen to performance as you increase the page walk
   cache size? Why?

3. Do you expect increasing the TLB size to have a larger impact on performance
   than increasing the page walk cache size? Why or why not? Use AMAT to justify
   your answer.

### [15 points] Step III: Basic Performance Analysis

1. What is the TLB miss rate for each workload?

2. What is the average page walk latency for each workload, i.e., what is the
   the AMAT of a TLB miss?

3. What percentage of execution time is spent handling TLB misses? (Hint:
   compare the performance of SE mode and FS mode to get an approximation of the
   time spent handling TLB misses.)

### [10 points] Step IV: Design Space Exploration

1. For each workload, what is the performance impact of:
   - Doubling the TLB size (16 to 32 entries)
   - Using the large page walk cache configuration

### [25 points] Research Question

Should we allocate area to a TLB or to the page walk cache? Assume that the area
difference of the larger TLB and the larger page walk cache is the same. (This
is approximately true for the configurations we are using since the TLB will be
fully associative and requires a lower access time.)

### [10 points] Next Steps (Required 201A, Extra Credit 154B)

1. How would your conclusions change if the workloads used huge pages (2MB)
   instead of regular 4KB pages?

2. What are the characteristics of the workloads which cause the performance
   impact of address translation to be different between the two workloads?
