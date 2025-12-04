/*
coder: ahmed abdel haleem
Date:26-5-2008
K&R.
EX: 1-13, Print histogram of the length of words in program input.
Page: 24.
*/
#include <stdio.h>

#define MAX 100
#define IN 1
#define OUT 0

main()
{
	int c,i,j,state,hist[MAX];
	
	c = 0;
	state = OUT; 
	for (i = 0; i < MAX; i++) 
		hist[i] = 0;
	i = 0; 
		
	while ((c = getchar()) != EOF )	
	{
		if (c == ' ' || c == '\t' || c == '\n') {
			if (state == IN){ 
				state = OUT;
				i++;
			}
		}
		else {
			++hist[i];
			state = IN;
		}
	}
		
	for (j = 0; j <= i; j++ ){
		//printf (" %02d |",j);
		while (hist[j] > 0) {	
			putchar('#');
			--hist[j];
		}
		putchar('\n');
	}
}

void print_blanks(char s[])
{
		if( c == '\t' )
			printf("\\t");
		else if( c == '\b' )
			printf("\\b");
		else if( c == '\\')
			printf( "\\\\" );
		else putchar(c);
}
