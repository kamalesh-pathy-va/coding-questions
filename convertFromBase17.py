'''
Convert the given input to decimal, from base 17.

Input:
1a
Output:
27

Input:
23gf
Output:
10980
'''

def solution(in_str):
	rev = in_str[::-1]
	ans = 0
	for i in range(len(in_str)-1, -1, -1):
		if rev[i].isdigit():
			ans += int(rev[i]) * (17 ** i)
		elif rev[i].isalpha() and rev[i] >= 'a' and rev[i] <= 'g':
			ans += (ord(rev[i]) - 87) * (17 ** i)
	return ans

def main():
	print(solution(input().lower()))

if __name__ == '__main__':
	main()