/*
Coder: ahmed abdel haleem ahmed.
e-mail: ahmedhal@gmail.com
K&R.
Date: 6-6-2008.
Page: 49.
*/

/* getbits: get n bits of x that beings at position p. We assume that bit position 0 is at the right end and that n and p are sensible positive numbers.  */
unsigned getbits(unsigned x, int p, int n)
{
	return (x >> (p+1-n)) & ~(~0 << n);
}
