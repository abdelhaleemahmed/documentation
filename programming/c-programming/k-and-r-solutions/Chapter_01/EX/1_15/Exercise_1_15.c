/*
coder: ahmed abdel haleem
e-mail: ahmedhal@gmail.com
Date:27-5-2008
K&R.
EX: 1-15, Rewrite tempreature program of section 1.2 to use a function for conversion.
Page: 27.
*/
#include <stdio.h>

int to_celsius(int );

/* Print fahrenheit-Celsius table
	for fahr = 0, 20, ..., 3000 */
main()
{	
	float fahr, celsius;
	int lower, upper, step;
	
	lower = 0;
	upper = 300;
	step = 20;
	
	fahr = lower;
	while(fahr <= upper){
		celsius = to_celsius(fahr);
		printf(" %3.0f %6.1f\n", fahr, celsius);
		fahr = fahr + step;
	}
}

int to_celsius(int f)
{
	return (5.0 / 9.0) * (f - 32.0);
}
