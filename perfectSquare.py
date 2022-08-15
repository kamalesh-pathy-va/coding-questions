'''
Given a list of numbers print the numbers if they are
perfect square

Input:
100 121 321 454 144 167
Output:
100
121
144
'''

def isPerfectSquare(num):
	ans = num**0.5
	ans*= 10
	rem = ans%10
	if rem > 0:
		return False
	return True

num_list = [int(x) for x in input().split()]
for i in num_list:
	if isPerfectSquare(i):
		print(i)
