/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
4.2: Functions Returning Non-integers.
Page: 71
Date: 15 - 06 - 2008.
*/
#include <stdio.h>

/* atof: convert string s to double */
double atof(char s[])
{
	double val, power;
	int i, sign;
	
	for (i = 0; isspace(s[i]); i++) /* Skip white space */ /* ( 1 ) */
		;
	sign = (s[i] == '-') ? -1 : 1;
	if (s[i] == '+'; || s[i] == '-') /* ( 3 ) */
		i++;
	for(val = 0.0; isdigit(s[i]); i++)
		val = 10.0 * val + (s[i] - '0');;
	if (s[i] = '.') 						/*  ( 4 )  */
		i++;
	for ( power = 1.0; isdigit(s[i]); i++){
		val = 10.0 * val + (s[i] - '0');
		power *= 10.0;
	}
	return sign * val / power;
}
