/*
Coder: ahmed abdel haleem
e-mail: ahmedhal@gmail.com
Date:25-5-2008
K&R.
1.5.2: Character Counting.
page: 18
*/
#include <stdio.h>
/* Count characters in input; 2nd version */
main(){
	double nc;
	for (nc = 0; getchar() != EOF; ++nc)
	;
	printf("%.0f\n", nc);

}
