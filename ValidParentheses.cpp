/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
*/

#include <iostream>
#include <string.h>

using namespace std;

bool isValid(string str)
{
	char stack[str.size()];
	int top = -1;
	for (int i=0; i<str.size(); i++)
	{
		if (str[i] == '{' || str[i] == '[' || str[i] == '(')
			stack[++top] = str[i];
		else if (str[i] == '}')
		{
			if(top == -1)
				return false;
			if (stack[top] == '{')
				top--;
			else
				return false;
		}
		else if (str[i] == ']')
		{
			if(top == -1)
				return false;
			if (stack[top] == '[')
				top--;
			else
				return false;
		}
		else if (str[i] == ')')
		{
			if(top == -1)
				return false;
			if (stack[top] == '(')
				top--;
			else
				return false;
		}
	}

	if (top == -1)
		return true;

	return false;
}

int main()
{
	string str;
	cin >> str;
	cout << isValid(str);
	return 0;
}