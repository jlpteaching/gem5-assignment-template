# Assignment 3 Questions

**IMPORTANT** Do not reformat this file!
Put your answers below each question.
Use markdown formatting.

## [25 points] How to reproduce the results

### Explanation of the script

### Script to run

### Parameters to script (if any)

### Commands used to gather data
List all the commands that you have used to do all the required experiments.
```sh
gem5 ...
```

## [75 points] Questions

### [10 points] Step 1: Choose your configurations

1. What are the configurations you are going to run?

### [20 points] Step 2: Run your experiments

1. What is the speedup of each configuration over the "little" core? Present your results in a table as described in the assignment.

### [40 point] Step 3: Analyze your results and answer the research question

1. What is the biggest bottleneck in the performance of the original processor? The width, the number of physical registers, or the reorder buffer size? Use your data to support your answer.

2. Using the `board.get_processor().get_area_score()` method, calculate the area of each configuration. What is the area-efficient design?

### [5 + 25 points] Step 4: Workload analysis

1. Describe which workload is affected more by each parameter of your configuration.

2. [Required 201A, extra credit 154B] Use the application's source code, the resulting assembly code, or other information to explain why each workload is more sensitive to a particular parameter.
