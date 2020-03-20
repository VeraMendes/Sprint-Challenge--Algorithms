#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime for this block is equal to O(n). `a` value increases as we loop through while. As a = `a + n * n` and we are comparing it to `n * n * n`, at some point the first value will catch up with the last one and that will happen in a linear rate, when this happens, the loop will stop. If n is a negative value, it will stop in the first iteration. 


b) Looking at this block of pseudocode, the final runtime will be O(n*m). Looking separately into the lines of code: 1st, 3rd, 5th and 6th line are constant time. When looking into the for function and while function we have to understand the logic. The first for loop will increase as n increases in a relation 1:1. Considering the while loop, `m`, it will run inside the for loop while j < n starting at 1 but j is increasing twice bigger than the normal rate so this makes the while runtime quite insignificant, which in fact makes the runtime pretty similar to O(n). 

c) The time complexity of this block of pseudocode is O(n). The first two lines of code inside the function are constant time, but the last line is calling the whole function as many times as n and will run for a linear time until bunnies are down to 0 where our base case is and where our function will stop. 

## Exercise II

###### building with n floors = sorted array
###### b number of eggs
###### f floor or higher, egg gets broken

I am looking for an efficient algorithm to minimize breaking eggs, if I iterate one by one, I will get a good portion broken, but if I try to implement `binary search`, instead of a runtime of O(n), I am able to get in the worst case scenario a maximum runtime of `O(log n)` as we keep dividing the amount of n where we are looking in.

I am trying to find the lowest floor where egg still gets broken as `f floor`, any floor below will not get the egg broken, any floor above will get the egg broken. 

We can see the building as a sorted array of numbers that increases 1 by 1, arr. Dividing total n in half, we can check if dropping one egg, will it break? 
If yes, then `f floor` is in the inferior half, so we divide again in half the inferior half and keep checking and dividing until we find `f floor`. 
If no, then `f floor` is in the superior half, so we divide again in half the superior half and keep checking and dividing until we find `f floor`.

start with: `n // 2`
then:
`f floor = (high_floor_in_interval_search - low_floor_in_interval_search) // 2 + low_floor_in_interval_search`
drop egg and keep checking the value. 
We keep checking the result until we come to the smallest interval possible, as we want to find the exact floor where the situation changes for egg_break vs egg_no_break possibility.
