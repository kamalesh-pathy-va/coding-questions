/*
Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’.
The length of the string is variable. The task is to find the minimum
number of ‘*’ or ‘#’ to make it a valid string. The string is considered
valid if the number of ‘*’ and ‘#’ are equal. The ‘*’ and ‘#’ can be at
any position in the string.
Note : The output will be a positive or negative integer based on
number of ‘*’ and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0  -> number of * and # are equal
*/

#include <iostream>

using namespace std;

main()
{
	string s;
	cin >> s;
	int no_of_star = 0;
	int no_of_hash = 0;
	int i = 0;
	while(s[i] != '\0')
	{
		if (s[i] == '*')
			no_of_star++;
		else
			no_of_hash++;
		i++;
	}

	cout << no_of_star - no_of_hash;
	return 0;
}