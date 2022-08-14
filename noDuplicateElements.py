'''
No Duplicate Elements:
Given a list of numbers, we need to eleminate the duplicate elements
by modifying the elements according to the following conditions.
If the number of elements are even add 10 to every occurrence of that
element except the first occurrence.
If the number of elemnets are odd double every occurrence of that
element except the first occurrence.

Input:
{2,3,8,8,8,2,32,16,12}
Output:
{2,3,8,16,32,12,64,74,22}

Explanation:
{2,3,8,8,8,12,32,16,12}

{2,3,8,16,16,12,32,16,12}

{2,3,8,16,32,12,32,32,12}

{2,3,8,16,32,12,64,64,12}

{2,3,8,16,32,12,64,64,22}

{2,3,8,16,32,12,64,74,22}


Input:
{4,5,3,3,2,4,8,10,7,13}
Output:
{4,5,3,13,2,14,8,10,7,23}
'''

num_list = [int(x) for x in input().split()]

indices = []

for i in range(len(num_list)):
	for j in range(i+1, len(num_list)):
		if num_list[j] == num_list[i]:
			indices.append(j)

	len_indices = len(indices)
	if len_indices > 0:
		for j in range(i+1, len(num_list)):
			if num_list[j] == num_list[i]:
				if len_indices%2 != 0:
					num_list[j] += 10
				else:
					num_list[j] *= 2
	indices.clear()

print(num_list)