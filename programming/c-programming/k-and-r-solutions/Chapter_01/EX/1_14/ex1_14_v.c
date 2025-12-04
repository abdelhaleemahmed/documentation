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
	
	int c,i,biggest,chars[MAX];
	
	c = biggest = 0;
	for (i = 0; i < MAX; i++)
		chars[i] = 0;
		
	while ((c = getchar()) != EOF)
	{
		if (c >= 'a' && c <= 'z')
		{
			i = c - 'a';
			++chars[i];
			if (chars[i] > biggest)
				biggest = chars[i];
		}
	}
	
	while(biggest > 0){
		printf("%02d |",biggest);
		for (i = 0; i < MAX; i++)
		{
			if (chars[i] == biggest)
			{
				putchar('#');
				--chars[i];
			}
			else
				putchar(' ');	
		}
		putchar('\n');
		--biggest;
	}
	
	/* Some stupid work again */
	printf("   +");
	for(i = 0; i < MAX; i++)
		putchar('-');
	putchar ('\n');
	printf("    ");
	for(i = 'a'; i <= 'z'; i++)
		putchar(i);
}
