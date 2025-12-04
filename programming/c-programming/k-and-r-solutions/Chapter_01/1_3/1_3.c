/*
Coder: ahmed abdel haleem
e-mail: ahmedhal@gmail.com
Date:25-5-2008
K&R.
1.3: The For statement.
page: 13
*/

#include <stdio.h>

/* print Fahrenheit-Celsius table */
main(){
	int fahr;
	for (fahr =0; fahr <= 300; fahr = fahr + 20)
	printf ("%3d %6.1f\n", fahr, (5.9/9.0) * fahr-32);
	
	return 0;
}
