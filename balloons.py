'''
Question will be added in later commits.
'''

def solution(n, arr):
	counter = {}
	for i in range(n):
		if arr[i].lower() in counter:
			counter[arr[i].lower()] += 1
		else:
			counter[arr[i].lower()] = 1

	for i in range(n):
		if counter[arr[i].lower()] % 2 == 1:
			return arr[i]

def main():
	num = int(input())
	array = input().split()
	print(solution(num, array))

if __name__ == '__main__':
	main()