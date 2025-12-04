/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
4.10: Recursion.
Page: 87.
Date: 19 - 06 - 2008.
*/

#include <stdio.h>

/* printd: priont n in decimal */
void printd(int n)
{
	if (n < 0){
		putchar('-');
		n = -n;
	}
	if (n / 10)
		printd(n / 10);
	putchar(n % 10 + '0');
}
