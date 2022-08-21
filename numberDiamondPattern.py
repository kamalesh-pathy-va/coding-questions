'''
Given a value of 'n', print the following number pattern in diamond pattern

Input:
4

Output:
            1
        4      4
    9      9      9
16      16      16      16
    12      12      12
        6      6
            2
'''

num = int(input())
max_len = 2 * num - 1

spacers = "  "

out_list = [spacers] * max_len

mid = int(max_len//2)

for i in range(num):
	for j in range(mid-i, mid+i+1, 2):
		out_list[j] = str((i+1)**2)
	print(spacers.join(out_list))
	out_list = [spacers] * max_len

for i in range(num-1,0,-1):
	for j in range(mid-(i-1), mid+(i), 2):
		out_list[j] = str(i * (i + 1))
	print(spacers.join(out_list))
	out_list = [spacers] * max_len

