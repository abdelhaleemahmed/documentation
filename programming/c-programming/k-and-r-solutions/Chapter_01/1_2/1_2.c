/*
Coder:Ahmed abdel haleem
e-mail: ahmedhal@gmail.com
Date:25-5-2008*
K&R.
1.2: variables and arithmetic Expressions.
page:9
*/
#include <stdio.h>

/*Print Fahrenheit-Celsius table
	for fahr = 0, 20, ... 300*/
	
main()
{
	int fahr, celsius;
	int lower, upper, step;
	
	lower = 0; /*lower limit of temperature table*/
	upper = 300; /*upper limit*/
	step = 20; /*step size*/
	
	fahr = lower;
	while(fahr <= upper){
		celsius = 5 * (fahr-32) / 9;
		printf("%d\t%d\n",fahr,celsius);
		fahr = fahr + step;
	}
}
