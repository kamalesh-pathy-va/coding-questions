'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

Input: n = 1
Output: "1"

Input: n = 4
Output: "1211"
'''


def countAndSay(n):
    res = "1"
    for _ in range(n-1):
        count = 0
        i = 0
        current = res[0]
        output = ""
        while i < len(res):
            if res[i] == current:
                count += 1
            if res[i] != current:
                output += str(count) + current
                current = res[i]
                count = 1
            i += 1
        output += str(count) + current
        res = output
    return res


print(countAndSay(4))
