'''
To find the factors of the numbers given in an array and to sort
the numbers in descending order according to the factors present in it.

Input:
8 2 3 12 16

Output:
12 16 8 2 3
'''

def factors(num):
	count = 0
	for i in range(1, num+1):
		if num % i == 0:
			count += 1
	return count

def solution(arr):
	values = []
	for i in arr:
		values.append(factors(i))

	for i in range(len(values)):
		for j in range(i+1, len(values)):
			if values[i] >= values[j]:
				temp = values[i]
				values[i] = values[j]
				values[j] = temp
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp


	return arr[::-1]

def main():
	result = solution([int(x) for x in input().split()])
	for i in result:
		print(i, end=" ")

if __name__ == '__main__':
	main()