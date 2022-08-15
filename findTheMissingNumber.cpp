/*
Given number of inputs N
and an array of N-1 elements from 1 to N with an element missing
the elements will not be in order.

NOTE: Give the effecient solution possible.

Input:
N no of elements
N-1 input elements on new line (because one is missing)

Output:
Return the missing element.

EX:
7	<- N
	__
3	 |
7	 |
6	 |	<- N-1 elements 
4	 |
1 	 |
5	__

2	<- output

10
9
1
6
4
7
8
2
3
10

5
*/

#include <iostream>

using namespace std;

main()
{
	int n;
	cin >> n;
	int actual_sum = 0;
	int x;
	for(int i=0; i < n-1; i++)
	{
		cin >> x;
		actual_sum += x;
	}

	int required_sum = n*(n+1)/2;
	cout << required_sum - actual_sum;
	return 0;
}