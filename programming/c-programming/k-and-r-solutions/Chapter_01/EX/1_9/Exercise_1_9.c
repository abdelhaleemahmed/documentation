/*
coder: ahmed abdel haleem
Date:26-5-2008
K&R.
EX: 1-8, Copy input to output replace each string of one or more balnks with a single blank.
Page: 20.
*/
#include <stdio.h>

#define IN 1
#define OUT 0

int main(){

	int c,state;
	
	c = 0;
	state = OUT;
	while ((c = getchar()) != EOF )
	{
		if (c == ' ')
		{
			if (state == OUT)
			{
				state = IN;
				putchar(c);
			}	
		}
		
		if (c != ' ')
		{
			putchar(c);
			if (state == IN)
				state = OUT;			
		}
	
	}
	return 0;
}
