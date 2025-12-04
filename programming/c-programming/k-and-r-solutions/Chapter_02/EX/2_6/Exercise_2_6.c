/*
Coder: ahmed abdel haleem.
e-mail: ahmedhal@gmail.com
k&R.
Ex: 2.6;Write function setbits(x,p,n,y ) that returns x with the n bits that begin at position p set to the right most n bits of y, leaving th other bits unchanged.
Date: 6 - 6 - 2008.
Page: 49.
*/
#include<stdio.h>

unsigned setbits(int, int, int, int);

main()
{
	int x1, p1, n1, y1;
	unsigned result = 0;
	
	x1 = 8;
	p1 = 3;
	n1 = 3;
	y1 = 7;
	
	result = setbits(x1,p1,n1,y1);
	printf ("X value: %d \n",result);
}

unsigned setbits(int x, int p, int n, int y)
{
	unsigned int r1;
	
	r1  = (( y & ~(~0 << n)) << (n+p+1) ) >> ( p + 1);
	printf (" r1 is %d \n",r1);
	printf ("x is %d\t x & r1 equal %d \n",x,(x & ~r1));
	return ((~r1 & x) | r1);
}
/*
Execution:
TEST 1:
x = 16 = 10000 -> p = 4
y = 7 = 111 -------> n = 2
RESULT : 28. (right answer)

TEST 2:
x = 8 = 1000 -> p = 3
y = 7 = 111   ----> n = 3
RESULT: 11000
*/

/*main()
{
	int n = 2;
	int x;
	
	x = ~(~0 << n);
	
	printf("%d\n",x & 7);
	
	return 0;
} */
