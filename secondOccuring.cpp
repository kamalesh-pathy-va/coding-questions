/*
Given a list of numbers find the second most repeating, first most repeating numbers and
concatenate togather to form a number.
If multiple number are repeting with equal number of times then choose the largest number

first line of input -> number of elements
next n lines of input -> n elements

Input:
10
12
2
36
10
217
36
5
36
15
10

Output:
1036

NOTE: Code is writen in a way that the logic can be used with C also.
*/

#include <bits/stdc++.h>

using namespace std;

main()
{
	int n;
	cin >> n;
	int arr[n];

	for(int i=0; i<n; i++)
		cin >> arr[i];

	int histo[n] = {0};
	int count = 0;

	for (int i=0; i<n; i++)
	{
		count++;
		for(int j=i+1; j<n; j++)
		{
			if(arr[i] == arr[j])
			{
				count++;
				arr[j] = INT_MIN; //INT_MIN is a predefined macro that is available in limits.h
			}
		}
		if (arr[i] != INT_MIN)
			histo[i] = count;
		count = 0;
	}

	int first_occur = INT_MIN;
	int second_occur = INT_MIN;
	int first_val = 0, second_val = 0;
	
	for(int i=0; i<n; i++)
	{
		if (histo[i] > first_occur)
		{
			second_val = first_val;
			second_occur = first_occur;
			first_val = arr[i];
			first_occur = histo[i];
		}
		else if (histo[i] > second_occur && histo[i] != first_occur)
		{
			second_occur = histo[i];
			second_val = arr[i];
		}
	}

	cout << second_val << first_val;
	return 0;
}