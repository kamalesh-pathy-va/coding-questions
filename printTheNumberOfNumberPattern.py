'''
Print the following pattern with the given input N.

Input:
5

Output:
1
1 1
2 1
1 2 1 1
1 1 1 2 2 1

Explanation:
To generate a member of the sequence from the previous member,
read off the digits of the previous member, counting the number of
digits in groups of the same digit. For example:

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
1211 is read off as "one 1, one 2, then two 1s" or 111221.
111221 is read off as "three 1s, two 2s, then one 1" or 312211.
'''

n = int(input())

num = '1'
count = 0
temp = ''
prev_num = num[0]

for _ in range(n):
	for i in num:
		if i == prev_num:
			count += 1
		else:
			temp += str(count) + prev_num
			count = 1
			prev_num = i
	temp += str(count) + prev_num
	print(num)
	num = temp
	temp = ''
	count = 0
	prev_num = num[0]