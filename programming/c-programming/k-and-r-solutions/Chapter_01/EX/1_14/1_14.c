/*
Coder: ahmed abdel haleem
Date:27-5-2008
K&R.
EX: 1 -14; Print frequencies of different characters in input.
Page:24
*/
#include <stdio.h>
#define MAX 26


main(){
	
	int c,i,chars[MAX];
	
	c = 0;
	for (i = 0; i < MAX; i++)
		chars[i] = 0;
		
	while ((c = getchar()) != EOF)
	{
		if (c >= 'a' && c <= 'z')
		{
			i = c - 'a';
			++chars[i];
		}
	}
			
	for (i =0; i< MAX; i++)
	{
		printf("%c |",i + 'a');
		while (chars[i] > 0) {
			putchar('#');
			--chars[i];
		}
		putchar('\n');
	}
}
