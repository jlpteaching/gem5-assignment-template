# The gem5 assignment template repository

This repository is set up so that you can easily use it as a template repository for gem5-based assignments.

This repo contains all of the "general" requirements for gem5-based assignments.
For each assignment, you should create a *fork* of this repository with the template code needed for that particular assignment.

This repository can be used in Codespaces to provide a complete development environment for students to work on the assignments.

## Assignments

The assignment text can be found in the `assignment.md` file in subdirectories of the `assignments` directory.
Each assignment is structured as a single *research question* for which the students must develop hypotheses, design experiments, and analyze results.
Below is the list of assignments in order of increasing difficulty:

- *Getting started*: A simple assignment to get students started with gem5. This will introduce the students to how to use gem5, codespaces, etc.
- *ISA vs Technology*: This assignment compares the performance difference of x86, Arm, and RISC-V ISAs on a simple matrix multiplication workload. The performance is compared across ISAs and between 1 GHz and 4 GHz. The goal is to use the Iron Law of Performance to explain the results.
- *Pipelining*: This assignment compares the performance of an in-order CPU with different pipeline widths, latencies, and depths. The goal is to understand the impact of the pipeline on performance.
- *Out of Order CPU*: This assignment digs into how different parameters of an out-of-order CPU, including width, ROB size, and the number of physical registers, impact performance. This assignment uses a variety of workloads to showcase the differences in how these parameters impact performance.
- *Blocked matrix-multiply*: This assignment uses blocked matrix multiply to show the importance of algorithm design on the performance of caches. It reinforces the AMAT calculation and the impact of cache size on performance.
- *Virtual memory*: (Coming soon) This assignment will explore the impact of virtual memory on performance.
- *False sharing*: This assignment looks at the impact of false sharing on performance. It uses a simple parallel workload, shows 6 different implementations, and asks the students to figure out why the performance is different.

## Using this to create assignments

1. Fork this repository to an assignment-specific repository (e.g., "assignment-1-template") under your classroom organization. This fork can be public or private.
2. Move the following files to the root of the repository.
   1. The `assignment.md` file to `README.md` in the root of the repository.
   2. The `questions.md` file.
   3. The `components` directory.
3. Delete the assignments directory.

## Using codespaces

I'll fill this in soon.
