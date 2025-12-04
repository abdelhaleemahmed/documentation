/*
Coder: ahmed abdel haleem
e-mail: ahmedhal@gmail.com
Date:25-5-2008
K&R.
1.5.2: Character Counting.
page: 18
*/
#include <stdio.h>
/* Count characters in input; 1st version */
main(){
	long nc;
	
	nc = 0;
	while (getchar() != EOF)
		++nc;
	printf("%ld\n", nc);
}
