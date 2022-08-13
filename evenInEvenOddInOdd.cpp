/*
Given a list of numbers, if there are equal numbers of even and odd numbers
in the list print "YES" and return the list with odd numbers in odd indices
and even numbers in even indices, else print "NO". 0 can be considered even
NOTE: index starts from 0

eg:
Input:
{1,5,6,8,7,2}
Output:
YES {6,1,8,5,2,7}

Input:
{9,0,3,5,2,1,6,4}
Output:
YES {0,9,2,3,6,5,4,1}

Input:
{6,1,3,2,7}
Output:
NO
*/

#include <iostream>

using namespace std;

main()
{
	int n;
	cin >> n;
	int arr[n];
	int even = 0;
	int odd = 1;
	int input;

	// Edge case if n = 1, we can't put the number in odd place
	if(n==1)
	{
		cin >> input;
		if(input % 2 == 0)
		{
			cout << "YES " << input;
			return 0;
		} else {
			cout << "NO";
			return 0;
		}
	}

	for(int i=0; i<n; i++)
	{
		cin >> input;
		if(input % 2 == 0)
		{
			arr[even] = input;
			even += 2;
		} else {
			arr[odd] = input;
			odd += 2;
		}
	}

	if(odd - even != 1)
	{
		cout << "NO";
		return 0;
	}

	cout << "YES ";
	for(int i=0; i<n; i++)
		cout << arr[i] << " ";

	return 0;

}