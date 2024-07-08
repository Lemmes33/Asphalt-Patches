Road Repair Problem

This repository contains a solution to the Road Repair problem, where we need to find the minimum number of patches required to repair all the potholes in a road consisting of N segments.

Problem Statement

The road is represented by a string S of length N, where each segment S[K] can either contain a pothole (denoted by 'X') or be a good segment (denoted by '.'). The road fixing machine can patch over three consecutive segments at once with asphalt and repair all the potholes located within each of these segments. Good or already repaired segments remain good after patching them.

Task

Write a function solution(S) that, given a string S of length N, returns the minimum number of patches required to repair all the potholes in the road.

Examples

Given S = ".X..X", the function should return 2. The road fixing machine could patch, for example, segments 0-2 and 2-4.
Given S = "X.XXXXX.X.", the function should return 3. The road fixing machine could patch, for example, segments 0-2, 3-5 and 6-8.
Given S = "XX.XXX..", the function should return 2. The road fixing machine could patch, for example, segments 0-2 and 3-5.
Given S = "XXXX", the function should return 2. The road fixing machine could patch, for example, segments 0-2 and 1-3.
Assumptions

N is an integer within the range [3..100,000]
string S is made only of the characters '.' and/or 'X'
Solution

The solution is implemented in the solution.js file. It uses a greedy approach to find the minimum number of patches required. The idea is to iterate through the string S and count the number of consecutive 'X's. Whenever we encounter a sequence of three or more 'X's, we increment the patch count and reset the sequence count.

Time Complexity

The time complexity of the solution is O(N), where N is the length of the string S.

Space Complexity

The space complexity of the solution is O(1), as we only use a constant amount of space to store the patch count and sequence count.

How to Run

To run the solution, simply execute the solution.js file with a JavaScript interpreter, such as Node.js. You can pass the input string S as an argument to the solution function.

For example:

Edit
Copy code
node solution.js ".X..X"
This should output 2, which is the minimum number of patches required to repair all the potholes in the road.