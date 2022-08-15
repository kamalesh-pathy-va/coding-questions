/*
Given a list of numbers print the numbers if they are
perfect square

Input:
100 121 321 454 144 167
Output:
100
121
144
*/

#include <iostream>
#include <cmath>

using namespace std;

bool isPerfectSquare(int num)
{
	float ans = sqrt(num);
	ans *= 10;
	int q = ans / 10;
	float rem = ans - (q * 10);
	if (rem > 0)
		return false;
	return true;
}

main()
{
	int num_list [] = {100, 121, 321, 454, 144, 167}; // Inputs are hardcoded
	for (int i=0; i<6; i++)
		if (isPerfectSquare(num_list[i]))
			cout << num_list[i] << endl;
	return 0;
}