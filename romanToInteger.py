'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
Given a roman numeral, convert it to an integer.

Input: s = "III"
Output: 3

Input: s = "LVIII"
Output: 58

Input: s = "MCMXCIV"
Output: 1994
'''

def romanToInt(s):
    rMap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    num = 0
    greatest = 0
    for i in s[::-1]:
        if rMap[i] >= greatest:
            greatest = rMap[i]
            num += rMap[i]
        else:
            num -= rMap[i]

    return num

print(romanToInt("MCMXCIV"))