'''
A frog hops 20cm in the first hop, 10cm in the second hop, 5cm in the third hop.
After three hops, the frog rests for a while and then again follows the same hopping
pattern.

calculate the total distance travelled by the frog (in cm) for the provided number of 
hops. Exactly 4 number of hops will be provided to the program (one number per line) as
per the below example.

Input format: input consists of arbitrary number of values, each corresponding to a
			  particular case.
Constraints: 1 <= number of jumps <= 10^6
			 Number of cases can never exceed 10^5
Output: Print an integer in each line, corresponding to each case.
'''

for _ in range(4):
	i = int(input())
	val = 0
	q = i // 3
	val = 35*q
	r = i % 3
	if r == 1:
		val += 20
	elif r == 2:
		val += 30

	print(val)