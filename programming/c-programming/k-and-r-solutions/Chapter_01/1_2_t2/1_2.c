/*
Coder: ahmed abdel haleem
e-mail: ahmedhal@gmail.com
Date:25-5-2008
K&R.
1.2: Variables and arithmetic Expressions.
page: 12
*/
#include <stdio.h>

/*print Fahrenheit-Celsius table
	for fahr = 0, 20, ..., 3000; floating-point version */
	
main()
{
	float fahr, celsius;
	int lower, upper, step;
	
	lower = 0; /* lower limit of temperature table */
	upper = 300; /* upper limit  */
	step = 20; /* step size */
	
	fahr = lower;
	while (fahr <= upper) {
		celsius = (5.0/9.0) * (fahr - 32.0);
		printf ("%3.0f %6.1f\n",fahr, celsius);
		fahr = fahr + step;
	}
}
