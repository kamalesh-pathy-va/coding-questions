'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]
'''


from itertools import product


def letterCombinations(digits):
    if len(digits) == 0:
        return []
    keyMap = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    output = []
    if len(digits) == 1:
        output = list(product(keyMap[digits]))
    elif len(digits) == 2:
        output = list(product(keyMap[digits[0]], keyMap[digits[1]]))
    elif len(digits) == 3:
        output = list(product(keyMap[digits[0]],
                      keyMap[digits[1]], keyMap[digits[2]]))
    elif len(digits) == 4:
        output = list(product(
            keyMap[digits[0]], keyMap[digits[1]], keyMap[digits[2]], keyMap[digits[3]]))

    return ["".join(x) for x in output]


print(letterCombinations('23'))
