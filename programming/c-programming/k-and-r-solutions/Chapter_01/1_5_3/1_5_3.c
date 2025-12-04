/*
Coder: ahmed abdel haleem
e-mail: ahmedhal@gmail.com
Date:25-5-2008
K&R.
1.5.3:Line Counting.
page: 19
*/
#include <stdio.h>
/*
The standard library ensures that an input text stream appears as a sequence of lines. each terminated by a newline. Hence, Counting line is just counting newlines.
*/
/* Count lines in input */

main(){
	int c, nl;
	
	nl = 0;
	while ((c = getchar()) != EOF)
		if ( c == '\n')
			++nl;
	printf ("%d\n", nl);
}
