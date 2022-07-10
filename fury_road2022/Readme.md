# ScooterRoad: solution
This is a 100% score solution to Fury Road Challenge on Codility.
The task can be found on 
[the official website](https://app.codility.com/programmers/challenges/fury_road2022/).

[The solution's report](https://app.codility.com/cert/view/certNTU23Q-M3T5HUR7EGZDBA2Q/details/).

## The algorithm 
We start a ride on a scooter, and one time per travel can change to foot.
So we need to know if and when do this switch.

The idea of the algorithm is to calculate the time of travel by scooter on every road segment.
Simultaneously, the algorithm calculates the time of travel by foot on every reverse road segment.

Then in every segment, we compare how long it will take to continue traveling by scooter
and to continue traveling by foot.

The algorithm has optimal O(N) complexity and scores 100%.