'''
Given a number n, the task is to find the remainder when n is divided by 11.
The input number may be very large.
Since the given number can be very large, you can not use n % 11.

Input: str = 13589234356546756
Output: 6

Input: str = 3435346456547566345436457867978
Output: 4

input: str = 121
Output: 0
'''

def solution(num_str):
	odd = 0
	even = 0
	for i in range(len(num_str)):
		if (i+1) % 2 == 0:
			even += int(num_str[i])
		else:
			odd += int(num_str[i])

	return abs(odd-even)

def main():
	print(solution(input()))

if __name__ == '__main__':
	main()