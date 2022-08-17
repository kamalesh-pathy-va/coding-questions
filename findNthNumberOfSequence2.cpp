/*
Given a value of N, find the Nth element of the following sequence
1 2 10 37 101 226 442 785 ...

Explanation is a part of solution (This will not be provided):
1 -> 1
1 + 1^3 -> 2
2 + 2^3 -> 10
10 + 3^3 -> 37
37 + 4^3 -> 101
and so on...

*/

#include <iostream>

using namespace std;

int solution(int n)
{
	int ans = 1;
	for(int i=1; i<n; i++)
		ans += i*i*i;
	return ans;
}

main() 
{
	int n;
	cin >> n;
	cout << solution(i);
	return 0;
}