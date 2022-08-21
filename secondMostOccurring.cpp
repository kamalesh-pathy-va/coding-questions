/*
Given a string as Input, find the second most occurring letter.
If multiple letters are occurring equal number of times then print the
largest letter in alphabetical order.
Input:
abcdaba

Output:
b

Input:
abcdabacd

Output:
d
*/
#include <bits/stdc++.h>

using namespace std;

main()
{
	string str;
	cin >> str;
	int histo[26] = {0};
	int i = 0;
	while(str[i] != '\0')
	{
		histo[str[i] - 97]++;
		i++;
	}

	int first_val = INT_MIN, second_val = INT_MIN;  //limits.h Library
	int first_index = -1, second_index = -1;

	for(int i=0; i<26; i++)
	{
		if(histo[i] > first_val)
		{
			second_val = first_val;
			second_index = first_index;
			first_val = histo[i];
			first_index = i;
		}
		else if (histo[i] >= second_val)
		{
			second_val = histo[i];
			second_index = i;
		}
	}

	cout << (char) (97 + second_index);
	return 0;
}