/*
Coder: ahmed abdel halem.
e-mail: ahmedha@gmail.com
K&R.
3.6: Loops - Do-while.
Page:64.
Date: 10 - 6 - 2008.
*/
/* itoa: convert n to characters in s */

void itoa(int n, char [])
{
	int i, sign;
	
	if((sign = n) < 0) /* record sign */
		n = -n;			/* make n positive */
	i = 0;
	do {				/* generate digits in reverse order */
		s[i++] = n % 10 + '0';	/* get next digit */
	} while ((n /= 10) > 0); /* delete it */
	
	if(sogn < 0)
		s[i++] = '-';
	s[i] = '\0';
	reverse(s);
}

/* 
Function itoa, which converts a number to a character string (the inverse of atoi). The job is slightly more complectaed than might be though at first, because the easy methods of generating the digits generate them in the wrong order.
 We have chosen to generate the string backwards, then reverse it.
 */
