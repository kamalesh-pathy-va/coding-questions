'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Input: s = "abc", t = "ahbgdc"
Output: true

Input: s = "axc", t = "ahbgdc"
Output: false
'''


def solution(s, t):
	out_str = ""
	index = 0
	for i in s:
		while index < len(t):
			if i == t[index]:
				out_str += i
				index += 1
				break
			index += 1

	if s == out_str:
		return True

	return False

def main():
	print(solution(input(), input())) # s and t is taken as input and passed to solution

if __name__ == '__main__':
	main()