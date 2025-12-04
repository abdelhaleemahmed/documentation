/*
Coder: ahmed abdel haleem
e-mail: ahmedhal@gmail.com
Date: 25-5-2008
K&R.
1.3;Ex: The For statement.
print fahr -> celsuis in reverse order.
page: 14
*/

/* NOTE: Comment out, one portion each time, and recompile */

#include <stdio.h>
/* While loop */
/*
main()
{
	float celsius;
	int fahr,lower,upper,step;

	lower = 0; // Lower limit 
	upper = 300; // Upper limit
	step = 20; // Step size 
	
	fahr = upper;
	while (fahr >= lower){
		celsius = (5.0/9.0)*(fahr -32);
		printf ("%3d %6.1f\n",fahr,celsius);
		fahr = fahr - step;
	}
}
*/


/* For loop */

main(){
	int fahr;
	for (fahr = 0; fahr <= 300; fahr +=20)
		printf("%3d %6.1f\n",fahr,((5.0/9.0)*(fahr -32)));
}
