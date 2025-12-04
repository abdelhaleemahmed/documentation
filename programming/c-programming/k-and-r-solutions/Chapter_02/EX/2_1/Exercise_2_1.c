/*
Coder: Ahmed abdel haleem.
Date: 1 - 6 -2008
e-mail: ahmedhal@gmail.com
Ex: 2.1; Write a program to determine the ranges of char, short, int, and long variables, both signed and unsigend.
Page: 36.
*/
#include<stdio.h>
#include<limits.h>

main()
{
	printf("\n\t\t Signed Values\n\n");
	printf("signed char MINI:  %d\n",SCHAR_MIN);
	printf("signed char MAX:   %d\n", SCHAR_MAX);
	printf("sined int MINI: %d\n",INT_MIN);
	printf("signed int MAX: %d\n",INT_MAX);
	printf("signed short MAX: %d \n",SHRT_MAX);
	printf("signed short MINI: %d \n",SHRT_MIN);
	printf("signed long MINI: %d\n",LONG_MAX);
	printf("signed long MAX: %d\n",LONG_MIN);
	
	printf("\n\t\t Unsigned Values\n\n");
	printf("unsigned char MINI:%d\n", CHAR_MIN);
	printf("unsigned char MAX: %d\n",UCHAR_MAX);
	printf("unsigned int MINI: %d\n",0);
	//printf("unsigned int MAX: %d\n",0x7fffffff);
	printf("unsigned short MAX: %d \n",USHRT_MAX);
	printf("unsigned long MAX: %d\n",ULONG_MAX);
	
	/*print values using calculations */

	return 0;
}
