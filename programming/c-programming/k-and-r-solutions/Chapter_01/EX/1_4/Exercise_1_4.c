/*
Coder: ahmed abdel haleem
e-mail: ahmedhal@gmail.com
Date:25-5-2008
K&R.
1.2, EX: Variables and arithmetic Expressions.
page: 13

write a program to print the correspoinding Celsius to Fahrenheit table.
F = (9/5) C + 32
*/
#include <stdio.h>

main()
{
	float fahr, celsius;
	int lower, step, upper;

	lower = 0;   /* Lower Temp limit */
	upper = 100; /* Upper limit */
	step = 20;   /*Step size*/
	
	printf("cels fahr\n");
	
	celsius = lower;
	while(celsius <= upper){
		fahr = ((9.0/5.0) * celsius )+ 32;
		printf ("%3.0f %3.0f\n",celsius, fahr);
		celsius = celsius + step;
	}
}
