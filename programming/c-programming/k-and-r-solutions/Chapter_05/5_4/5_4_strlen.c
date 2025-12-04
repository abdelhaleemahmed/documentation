/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
5.4: Address Arithmetic.
Page: 101
Date: 18 - 06 - 2008.
*/
/* Version of strlen depend on pointers arithmetic facts  */

/* strlen: return length of string s */

int strlen()
{
	char *p = s;
	
	while (*p != '\0')
		p++;
	return p - s;
}
