A stack is an extrememly popular data structure in computer science. From solving the Tower of Hanoi to basically helping all programming languages to execute in the order we specify, its extremely powerful. We are going to explore this data structure in more detail in this programming exercise. 

Just like every other data structure the stack organizes data in a certain way. The stack is a last in first out data structure i.e. whatever you add to the stack last is the first that you can access or remove. 

You won't be able to access an element in the stack unless you gave removed all the elements above it. Usually a stack is not inifinite, nor does it grow. A stack (S) is always initialized with a fixed size (MAX_SIZE). You can add upto MAX_SIZE number of elements. A stack should normally be able to store any type of data but for the sake of ease of implementation we will assume the stack holds strings.

A stack lets you perform the following operations on it
1) Initialize a stack with certain fixed size
2) push - Add an element to the stack 
3) peek - Query the top element of the stack 
4) pop - Remove the top most element of the stack and return it 
5) clear - Clear the stack/removes all the elements from the stack

Things to think about
1) What happens when we try to add an element to the stack and it's full
2) What happens when we try to remove an element from an empty stack
3) What happens if we query the top element from the stack and it's empty

In stack.py, you are given empty functions for the stack. Implement these functions and run the file. If the tests pass proceed to solve the problems from leetcode

Finally, solve the problems below from leetcode


If you are stuck for more than 30 minutes with the problem, instead of looking at the solution try these steps in order
* Explain the problem to yourself
* Take a sample input and according to the problem, what should be the output. Take few more and play around
* Imagine you had the freedom to solve the problem any way you want, can you think of a solution? If so think about it and see if you can use the data structure we discuessed to optimize it. You can also code up the solution and submit on leetcode. If it passes, you have found a new/different way of solving the problem
* If you are stuck on the solution, explain the solution to yourself and see if you can get yourself unstuck

If you have tried the above steps and you aren't able to figure it out look at the solution online or read one of the posts in leetcode 


https://leetcode.com/problems/valid-parentheses/
https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

