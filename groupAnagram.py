'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
'''

def groupAnagrams(strs):
    words = {}
    for i in strs:
        sorted_str = "".join(sorted(i))
        if sorted_str in words:
            words[sorted_str].append(i)
        else:
            words[sorted_str] = [i]
    output = []
    for i in words:
        output.append(words[i])

    return output


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))