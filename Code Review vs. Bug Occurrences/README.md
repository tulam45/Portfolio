# CS563-Study-Project
Contains the evaluation programs used in the CS563 project

## R-Value
The `r_value` python program is a script python program that have the data of the `review_frequency, depth, reviewers_count, and bug occurences` to determine the correlation of the three variables.

## Cliff's Delta
The `cliff_delta` calculate the value of cliff to the comparision of reviewer vs bug occurence. 

## Review Depth
Using the `review_depth` program, fetch all **PRs** that fit within the range of time of a version release and calculate the depth of it. (Number of issue raise by reviewer / Numbers of commits)

## Review Frequency
Similar to the depth, the `review_frequency` follows the usage of <ins>GitHub API</ins> to fetch all the PRs and count how many distinct and in total of reviewers happen during that version release. 

## Bug Occurrence
To find bug occurrences in between each version release, we did the following through the GitHub's interface website that was provided:
1. `is:issue state:closed repo:samvera/hyrax closed:>=YYYY-MM-DD closed:<=YYYY-MM-DD` -> Finding the amount of tickets close during the period
2. `is:issue state:closed repo:samvera/hyrax closed:>=YYYY-MM-DD closed:<=YYYY-MM-DD label:bug` -> Finding the amount of tickets close during the period with bugs label
