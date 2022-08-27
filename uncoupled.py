'''
Find the only uncoupled integer in an array.

Problem Statement
Write a program that, given a list of integers as an argument to STDIN

n1, n2, n3, ..
Prints out the only uncoupled (unpaired) integer in the list to STDOUT.

Example 1:

Given the input

1, 2, 3, 1, 2
your program should output:

3
Example 2:

Given the input

1, 2, 3, 4, 5, 99, 1, 2, 3, 4, 5
your program should output:

99
'''

nums = [int(x) for x in input().split()]
count = {}

for i in nums:
	if i in count:
		count[i] += 1
	else:
		count[i] = 1

for i in count:
	if count[i] % 2 == 1:
		print(i)