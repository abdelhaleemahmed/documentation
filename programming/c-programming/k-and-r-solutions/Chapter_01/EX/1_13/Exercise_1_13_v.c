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
	int c,i,j,biggest,state,hist[MAX];
	
	c = 0;
	state = OUT; 
	for (i = 0; i < MAX; i++) 
		hist[i] = 0;
	i = j = biggest = 0;
			
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
			if (hist[i] > biggest)
				biggest = hist[i];
		}
	}
	
	//printf("%d\n",biggest);
	
	while (biggest > 0)
	{
		printf(" %02d | ",biggest);
		for (j = 0; j <= i; j++)
		{
			if (hist[j] == biggest){
			putchar('#');
			hist[j]--;
			}
			else 
				putchar(' ');	
		}
		putchar('\n');
		biggest--;
	}
	
	/* This is stupid some what but it works */
	printf ("    +");
	for (j = 0; j <= i; j++)
		putchar('-');
}
