'''
The Binary number system only uses two digits, 0 and 1 and number system can
be called binary string. You are required to implement the following function:

int OperationsBinaryString(char* str);

The function accepts a string str as its argument. The string str consists
of binary digits eparated with an alphabet as follows:

– A denotes AND operation
– B denotes OR operation
– C denotes XOR Operation
You are required to calculate the result of the string str, scanning the string
to right taking one opearation at a time, and return the same.

Note:
-> No order of priorities of operations is required
-> Length of str is odd
-> If str is NULL or None (in case of Python), return -1

Input:
1C0C1C1A0B1

Output:
1
'''

def OperationsBinaryString(in_str):
	str_len = len(in_str)
	if str_len == 0:
		return -1
	prev_val = int(in_str[0])
	for i in range(1, str_len-1):
		if in_str[i] == 'a':
			prev_val &= int(in_str[i+1])
		elif in_str[i] == 'b':
			prev_val |= int(in_str[i+1])
		elif in_str[i] == 'c':
			prev_val ^= int(in_str[i+1])

	return prev_val

def main():
	print(OperationsBinaryString(input().lower()))

if __name__ == '__main__':
	main()
