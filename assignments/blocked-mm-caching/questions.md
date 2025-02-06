# Assignment 4 Questions

**IMPORTANT** Do not reformat this file!
Put your answers below each question.
Use markdown formatting.

Name:

Email:

Student ID:

## [25 points] How to reproduce the results

### Explanation of the script

### Script to run

### Parameters to script (if any)

### Commands used to gather data

## [75 points] Questions

### [25 points] Step I: Working set sizes

1. [8 points] What is the working set size for the matrix multiply application?

2. [8 points] For each of the three blocking configurations, what's the *active working set* for multiplying *one block*?

3. [9 points] Given your answers, for the "SmallCache" that is 16 KiB, which implementation do you think will perform the best?

### [25 points] Step II: Simulation and performance comparison

1. For `SmallCache`, which blocking scheme performs the best? Why?

### [25 points] Step III: Comparing cache size effects

1. [12 points] Which blocking schemes benefit the most from the larger cache?

2. [13 points] Why does the non-blocked implementation not benefit as much from the larger cache?

### [25 points] Next steps (required 201A, extra credit 154B): Running on native hardware

1. [7 points] What is the L1/L2/L3 size of the processor you're running on? (`lscpu` or `/proc/cpuinfo` and Google should help)

2. [7 points] Can you use the information about the cache sizes to predict the best-performing block scheme and size (assume a matrix size of 256)?

3. [7 points] Which blocking scheme and size exhibited the best performance? Why or why not?

4. [8 points] Is this the same as on gem5? Why or why not?
