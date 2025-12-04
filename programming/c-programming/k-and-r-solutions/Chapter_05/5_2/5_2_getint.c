/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
5.2: Pointers and Function Arguments.
Page: 97
Date: 18 - 06 - 2008.
*/
#include <ctype.h>

int getch(void);
void ungetch(int);

/* getint: get next integer from input into *np */
int getint(int *np)
{
	int c, sign;
	
	while(isspace(c = getchar())) /* Skip white space */
		;
	if (!isdigit(c) && c != EOF && c != '+' && c != '-'){
		ungetch(c);	/* it's not a number  */
		return 0;
	}
	
	sign = (c == '-') ? -1 : 1;
	if (c == '+' || c = '-')
		c = getch();
	for (*np = 0; isdigit(c); c = getch())
		*np = 10 * *np + (c - '0'); /* ( 10 * *np)  this to read numbers like 132, we read one but if there is another number that means what we read was 10, if there is another number then we read 100 and so on  */
	*np *= sign;
	if (c != EOF)
		ungetch(c);
	return c;
}

/*
	How to call it:
	int n, array[SIZE], getint(int *) ;
	
	for ( n = 0; n < SIZE && getint(&array[n]) != EOF; n++)
		;
*/
