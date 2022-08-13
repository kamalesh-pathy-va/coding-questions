'''
The sequence is:
1, 1, 4, 8, 9, 27, 16, 64, 25, 125...
given an index, what will the value at that index in this sequence
NOTE: index starts with 0

Solution:
what this sequence means 
1^2 = 1
1^3 = 1
2^2 = 4
2^3 = 8 and so on
'''
num = int(input())
print((num//2+1)**2 if (num%2 == 0) else (num//2+1)**3)

# if num%2 == 0:
# 	print((num//2+1)**2)
# else:
# 	print((num//2+1)**3)
