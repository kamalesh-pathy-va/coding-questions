'''
Write a program to print the string in the following X pattern
The length of the string given will always be odd.

Input:
ODD

Output:
O D
 D 
O D

Input:
PROGRAM

Output:
P     M
 R   A
  O R  
   G   
  O R
 R   A 
P     M
'''

string = input()
str_len = len(string)
out_str = [" "]*str_len

for i in range(str_len):
	out_str[i] = string[i]
	out_str[str_len-1-i] = string[str_len-1-i]
	print("".join(out_str))
	out_str = [" "]*str_len