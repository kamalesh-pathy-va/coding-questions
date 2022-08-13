/*
For the problem statement check out the python implemention
of this problem in this repo with the same file name as this
("printNoOfChar.py").

NOTE: Compiled with GCC compiler with C++11
*/

#include <bits/stdc++.h>

using namespace std;

bool isdigit(char c)
{
	if (c >= 48 && c <= 57)
		return true;
	return false;
}

bool isalpha(char c)
{
	if (c >= 97 && c <= 97+25)
		return true;
	return false;
}

main()
{
	string the_input;
	string str;
	string num;
	int is_num = 0;

	cin >> the_input;
	the_input += 'a';
	int i=0;
	while(the_input[i] != '\0')
	{
		if (isalpha(the_input[i]))
		{
			if (is_num)
			{
				for (int j=0; j<stoi(num); j++)
					cout << str;
				str = "";
				num = "";
				is_num = 0;
			}
			str += the_input[i];
		}
		else if (isdigit(the_input[i]))
		{
			num += the_input[i];
			is_num = 1;
		}

		i++;
	}
	return 0;
}