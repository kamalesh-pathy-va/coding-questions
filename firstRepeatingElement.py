'''
Given an array arr[] of size n, find the first repeating element.
The element should occurs more than once and the index of its first
occurrence should be the smallest.

Input:
n = 7
arr[] = {1, 5, 3, 4, 3, 5, 6}
Output: 2
Explanation: 
5 is appearing twice and 
its first appearence is at index 2 
which is less than 3 whose first 
occuring index is 3.

Input:
n = 4
arr[] = {1, 2, 3, 4}
Output: -1
Explanation: 
All elements appear only once so 
answer is -1.

Expected Time Complexity: O(n)
Expected Auxilliary Space: O(n)
'''

def solution(arr, n):
	val_count = {}
	for i in range(n):
		if arr[i] in val_count:
			val_count[arr[i]] += 1
		else:
			val_count[arr[i]] = 1

	for i in range(n):
		if val_count[arr[i]] >= 2:
			return i+1

	return -1

def main():
	num = int(input())
	array = [int(x) for x in input().split()]
	print(solution(array, num))

if __name__ == '__main__':
	main()