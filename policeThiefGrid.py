'''
You are given a grid of size NxN that has the following specifications:

Each cell in the grid contains either a policeman or a thief.
A policeman can only catch a thief if both of them are in the same row.
Each policeman can only catch one thief.
A policeman cannot catch a thief who is more than K units away from the policeman.

Write a program to find the maximum number of thieves that can be caught in the grid.

Input format
First line: Two space-separated integers N and K
Next N lines: N space-separated characters (denoting each cell in the grid)

Output format
Print the maximum number of thieves that can be caught in the grid.
'''

n, k = [int(x) for x in input().split()]
matrix = []
for i in range(n):
	matrix.append(input().split())

count = 0

for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		for x in range(k,0,-1):
			if j+x > n-1:
				continue

			if matrix[i][j] == 'T' and matrix[i][j+x] == 'P':
				count += 1
				matrix[i][j] = 0
				matrix[i][j+x] = 0
			elif matrix[i][j] == 'P' and matrix[i][j+x] == 'T':
				count += 1
				matrix[i][j] = 0
				matrix[i][j+x] = 0

print(count)


'''
This question was asked in Virtusa NeuralHack international hackathon on their platform this passed 4/5
test cases couldn't figure out that one edge case where it failed, if anyone knows please mail me to
asokankamalesh@gmail.com
'''