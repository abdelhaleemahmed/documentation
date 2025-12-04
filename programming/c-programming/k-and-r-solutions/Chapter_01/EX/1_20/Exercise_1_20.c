/*
coder: ahmed abdel haleem.
e-mail:ahmedhal@gmail.com
Date: 31-5-2008.
K&R;EX: Write a program detab that replaces tabs in the input with the proper number of blanks to space to the next tab stop.
Page: 34.
*/
#include <stdio.h>
#define MAXLINE 100
#define TABSTOP 4

int getline(char [], int);
int detab(char [], int);

main()
{
	int c,len = 0,t = 0;
	char line[MAXLINE];
	
	while((len = getline(line, MAXLINE)) > 0)
	{
		t = detab(line, TABSTOP);
		printf("number of tabs = %d\n", t);
	}

	return 0;
}

int getline(char line[], int limit)
{
	int c,i;
	
	for (i = 0; i < limit-1 && (c = getchar()) != EOF && c != '\n'; ++i)
		line[i] = c;
	if(c = '\n'){
		line[i] = c;
		++i;
	}
	line[i] = '\0';
	
	return i;
}

int detab(char line[], int tabs)
{
	/* Replace tabs with spaces when you print it */
	int n = 0,ntabs = 0;
	while(line[n] != '\0')
	{
		if (line[n] == '\t'){
			ntabs++;
			for(; tabs > 0; --tabs)
				putchar(' ');
		}
		else putchar(line[n]);
		++n;
	}
	return ntabs;
}
