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
	state = OUT; /* Initial state we are out, so we have no new words yet!. */
	for (i = 0; i < MAX; i++) /* Grant it is blank */
		hist[i] = 0;
	i = 0; /* We use i, so it is value is #, reset it to remove some pain, we relay on it to keep track of array index */
		
	while ((c = getchar()) != EOF )	
	{
		if (c == ' ' || c == '\t' || c == '\n') {
			if (state == IN){ /* are we IN ?, great, so we got NEW  WORD, PERFECT, KEEP ON */
				state = OUT;
				i++;
			}
		}
		else { /* Non blank value, so what is it, hah, a word of course !!!. */
			++hist[i];
			state = IN;
		}
	}
	
	 /* Did we got them all, GREAT, then let us print the valable histogram */
	for (j = 0; j <= i; j++ ){
		while (hist[j] > 0) {
			putchar('#');
			--hist[j];
		}
		putchar('\n');
	}
}
