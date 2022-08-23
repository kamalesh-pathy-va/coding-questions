'''
Given a string consisting of lowercase english alphabets,
reverse only the vowels present in it and print the resulting string.

Input: 
S = "practice"
Output: prectica
Explanation: The vowels are a, i, e
Reverse of these is e, i, a.
'''
string = list(input())

vowels = 'aeiou'

found_vowels = []

for i in range(len(string)):
	if string[i] in vowels:
		found_vowels.append(string[i])
		string[i] = 0

for i in range(len(string)):
	if string[i] == 0:
		string[i] = found_vowels.pop()

print("".join(string))