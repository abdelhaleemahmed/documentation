/*
coder: ahmed abdel haleem
e-mail: ahmedhal@gmail.com
Date:29-5-2008
K&R.
EX: 1-17, write a program to printall lines that are longer than 80..
Page: 31.
*/
#include <stdio.h>
#define MAXLINE 1000

int getline(char [] , int ,int );

main()
 {
	int len, c, start = 0;
	char line80[MAXLINE];

	while((c = getchar()) != EOF )
	 {
		
		line80[start] = c;
		start++;
		if((len = getline(line80, MAXLINE, start)) > 80 )
		{
			printf("%s", line80);
			start = 0;
		}
		else start = 0;
	 }
 }

int getline(char s[], int lim, int st)
 {
	int c,i;
	
	for(i = st; i<lim-1 && (c = getchar()) != EOF && c != '\n'; i++)
		s[i] = c;
	if (c == '\n'){
		s[i] = c;
		++i;
	}
	s[i] = '\0';
	
	return i;
 }
