/*
Coder: ahmed abdel haleem.
e-mail: ahmedhal@gmail.com
Date: 7-6-2008
K&R.
Page: 50
*/
/* bitcount: count 1 bits in x */
/* Note that we use OCTAL numbering system becaus we need to manipulate bits and we can't use binary!! right. it same that this is normal but .. */

int bitcount(unsigned x)
{
	int b;

	for (b = 0; x != 0; x >= 1 )
		if(x & 01)
			b++;
	return b;
}
