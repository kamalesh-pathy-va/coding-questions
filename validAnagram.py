'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
'''

# 58ms 16.9MB
# def isAnagram(s, t):
#         if len(s) != len(t):
#             return False
#         alpha = {}
#         for i in range(len(s)):
#             if s[i] in alpha:
#                 alpha[s[i]] += 1
#             else:
#                 alpha[s[i]] = 1
#             if t[i] in alpha:
#                 alpha[t[i]] -= 1
#             else:
#                 alpha[t[i]] = -1

#         for i in alpha:
#             if alpha[i] != 0:
#                 return False

#         return True



# 52ms 17.6MB
def isAnagram(s, t):
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        for i in range(len(s)):
            if s[i] != t[i]:
                return False

        return True