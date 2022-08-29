'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the
order of characters. No two characters may map to the same character, but a character may map to itself.

Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "paper", t = "title"
Output: true
'''

def solution(s, t):
	if len(s) != len(t):
		return False

	mapping = {}

	for i in range(len(s)):
		if s[i] in mapping:
			if mapping[s[i]] == t[i]:
				continue
			else:
				return False
		else:
			mapping[s[i]] = t[i]

	new_mapping = dict([(value, key) for key, value in mapping.items()])

	if len(new_mapping) != len(mapping):
		return False

	return True

def main():
	s = input()
	t = input()
	print(solution(s, t))

if __name__ == '__main__':
	main()