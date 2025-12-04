/*
Coder: ahmed abdel haleem ahmed.
e-mail: ahmedhal@gmail.com
K&R.
Date: 6-6-2008.
Page: 49.
*/
/*
GETBITS ANALYSIS; BY: Ahmed abdel  haleem.
(Note: this is worng i assume bit ZERO at left but K&R assume it is at right,but the calculations is right even you assume it is
at left an what all we said is valid)

(x = 25; p = 4; n = 3)
01234567
00011001
result = 6
_______________________
(x = 9; p = 4; n = 3)
01234567
00001001
result = 2
_______________________
(x = 7; p = 4; n = 3)
01234567
00000111
result = 1
_______________________
(x = 7; p = 3; n = 4)
01234567
00000111
result = 1 (wrong result ?.) it gives me 7!!!.
_______________________
(x = 7; p = 6; n = 3)
01234567
00001111
result = 7 (wrong also it gives me ZERO)
_________________________________________
(x = 15; p = 6; n = 3)
01234567
00001111
result = 0 (wrong also it gives me ZERO)
__________________________________________
(x = 15; p = 5; n = 3)
01234567
00001111
result = 7 (wrong also it gives me ONE)
___________________________________________

It sames that, we must not give it (p + n) >=8 and aslo (p+1-n < number of decimal digits)
for example tha last test (x = 15; p = 5; n = 3) if we set (n = 2) this will satisfy the
first condition but (p + 1 - n) = (5 + 1 - 2) = 4; 15 -> 00001111 so the decimal digits
are 1111 = 4 digits, which is equal to the previous equation, we will get a wrong result.

How it works:
Let us take this example, which it satisfy the condtitions we defined:

(x = 7; p = 4; n = 3)
01234567
00000111
result = 1
-----------------------------------------------
a-> x >> (p+1-n) -> x >> 2 (so x = 00000001)

b-> (~0 << n) -> 100; ~(~0 << n) -> 011

(a) & (b) -> 1; (which is the right result).
.
*/
#include<stdio.h>
unsigned getbits(unsigned x, int p, int n);

main()
{
	unsigned x = 15; /* 00000111*/
	int p = 4;
	int n = 3;
	int y = 0;

	printf("x %d\n",x);
	y = getbits(x,p,n);
	printf("value of x %d \n",y);

	return 0;
}

/* getbits: get n bits of x that beings at position p. We assume that bit position 0 is at the right end and that n and p are sensible positive numbers.  */
unsigned getbits(unsigned x, int p, int n)
{
	return (x >> (p+1-n)) & ~(~0 << n);
}
