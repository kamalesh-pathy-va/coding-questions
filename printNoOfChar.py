'''
Given a string, we need to decode the string, see the
example to understand the problem. The numbers in the
input string will be natural numbers.

Input:
a1c3
Output:
accc

Input:
a5b10
Output:
aaaaabbbbbbbbbb

Input:
a2b3cd4z10
Output:
aabbbcdcdcdcdzzzzzzzzzz

'''

the_input = input()+'a'
# The below for loop will execute till
# the length of the input, but according 
# to my logic it needs one more iteration
# so added a character

char = ""
num = ""
is_num = False

for i in range(len(the_input)):
	if the_input[i].isalpha():
		if is_num:
			print(char*int(num), end='')
			char = ""
			num = ""
			is_num = False
		char += the_input[i]
	elif the_input[i].isdigit():
		num += the_input[i]
		is_num = True

