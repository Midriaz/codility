# Pascal triangle: solution
This is a 100% score solution to Nickel 2018 Codility challenges.
The task can be found on 
[the official website](https://app.codility.com/programmers/challenges/nickel2018/).

[The solution's report](https://app.codility.com/demo/results/trainingQEAVH7-HKF/).

If you try to build the whole triangle step by step by calculating 
the next level, it will be slow, and you will fail the performance test. We need something fast. 

My idea is simple. Let's look at an example of a possible triangle:
```
0 1 0 0 0 1 0 0 1
 1 1 0 0 1 1 0 1
  1 1 0 1 1 1 1
   1 1 1 1 1 1
    1 1 1 1 1
     1 1 1 1
      1 1 1
       1 1
        1
```

As you can see, nulls (which are False), form their triangles inside the big triangle 
(let's call them "ZERO Triangles").
So what we need to do, is just calculate the number of elements in the big triangle,
and then subtract the number of elements in "ZERO Triangles".  
