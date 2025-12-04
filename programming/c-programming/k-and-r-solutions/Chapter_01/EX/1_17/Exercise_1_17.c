/*
coder: ahmed abdel haleem
e-mail: ahmedhal@gmail.com
Date:28-5-2008
K&R.
EX: 1-17, write a program to printall lines that are longer than 80..
Page: 31.
*/
#include <stdio.h>
#define MAXLINE 1000

int getline(char [] , int);

main()
{
	int len, c;
	char line80[MAXLINE];

	while((c = getchar()) != EOF ) /*Stupid but simple, !!, and it will cost us one char, may be I should ( un-get it) before continue*/
	while((len = getline(line80, MAXLINE)) > 80 )
		printf("%s", line80);
}

int getline(char s[], int lim)
{
	int c,i;
	
	for(i=0; i<lim-1 && (c=getchar()) != EOF && c != '\n'; ++i)
		s[i] = c;
	if (c == '\n'){
		s[i] = c;
		++i;
	}
	
	s[i] = '\0';
	return i;
}
