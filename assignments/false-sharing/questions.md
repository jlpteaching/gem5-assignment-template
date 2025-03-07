# False Sharing Assignment Questions

Name: Email: Student ID:

**IMPORTANT** Do not reformat this file! Put your answers below each question.
Use markdown formatting.

## [25 points] How to reproduce the results

### Explanation of the script

### Script to run

### Parameters to script (if any)

### Commands used to gather data

```shell

```

## [50 points] Questions

### Question 1

For algorithm 1, does increasing the number of threads improve performance or hurt performance? Use data to back up your answer.

### Question 2

(a) For algorithm 6, does increasing the number of threads improve performance or hurt performance? Use data to back up your answer.

(b) What is the speedup when you use 2, and 4 threads.

### Question 3

(a) Using the data for all 6 algorithms, what is the most important optimization, chunking the array, using different result addresses, or putting padding between the result addresses?

(b) Speculate how the hardware implementation is causing this result. What is it about the hardware that causes this optimization to be most important?

### Question 4

(a) What is the speedup of algorithm 1 and speedup of algorithm 6 on *16 cores* as estimated by gem5?

(b) How does this compare to what you saw on the real system?

### Question 5

Which optimization (chunking the array, using different result addresses, or putting padding between the result addresses) has the biggest impact on the *hit ratio?*

Show the data you use to make this determination.
Discuss which algorithms you are comparing and why.

### Question 6

Which optimization (chunking the array, using different result addresses, or putting padding between the result addresses) has the biggest impact on the *read sharing?*

Show the data you use to make this determination.
Discuss which algorithms you are comparing and why.

### Question 7

Which optimization (chunking the array, using different result addresses, or putting padding between the result addresses) has the biggest impact on the *write sharing?*

Show the data you use to make this determination.
Discuss which algorithms you are comparing and why.

### Question 8

Let's get back to the question we're trying to answer. From [question 3](#question-3) above, "What is it about the hardware that causes this optimization to be most important?"

So:
(a) Out of the three characteristics we have looked at, the L1 hit ratio, the read sharing, or the write sharing, which is most important for determining performance?
Use the average memory latency (and overall performance) to address this question.

Finally, you should have an idea of what optimizations have the biggest impact on the hit ratio, the read sharing performance, and the write sharing performance.

So:
(b) Using data from the gem5 simulations, now answer what hardware characteristic *causes* the most important optimization to be the most important.

### Question 9

**NOTE**: This question is for 201A students **only**.

Run using a crossbar latency of 1 cycle and 25 cycles (in addition to the 10 cycles that you have already run).

As you increase the cache-to-cache latency, how does it affect the importance of the different optimizations?

You don't have to run all algorithms.
You can probably get away with just running algorithm 1 and algorithm 6.
