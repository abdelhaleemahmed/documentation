/*
Coder: ahmed abdel haleem
e-mail: ahmedhal@gmail.com
Date:26-5-2008
K&R.
EX:1-12: a program to print one word per line.
page: 20
*/
#include <stdio.h>

#define IN 1
#define OUT 0

main(){
	int c,state;
	
	c = 0;
	state = OUT;
	while ((c = getchar()) != EOF){
		if (c == ' ' || c == '\t' || c == '\n' ){
			if (state == IN){
				state = OUT;
				putchar('\n');
			}
			}
			else{
				state = IN;
				putchar(c);
			}
	}
}
