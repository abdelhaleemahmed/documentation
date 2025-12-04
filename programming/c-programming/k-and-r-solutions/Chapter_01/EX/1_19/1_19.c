/*
Coder: ahmed abdel haleem.
e-mail: ahmedhal@gmail.com
Date: 30-5-2008
k&R.
EX: 1-19; Write a function reverse(s) that reverse the character string s. Use it to wirte a program that reverse its input a line at a time.
Page: 31
*/
/*Reverse Function:
#define MAXLINE 100

void reverse(char []);

void reverse(char s[])
{
	int i,n = 0;
	char tmp[MAXLINE];
		
	for(i = 0; s[i] != '\0'; ++i)
		tmp[i] = s[i];
		
	for(--i; i >= 0; --i)
		{
		s[n] = tmp[i];
		n++;
		}

	s[n] = '\n';
	n++;
	s[n] = '\0';
}
*/
#include <stdio.h>
#define MAXLINE 100

int getline (char [], int );
void reverse(char []);

main()
 {
	
	int len = 0;
	char line[MAXLINE];

	while ((len = getline(line, MAXLINE)) > 0 )
	{
		reverse(line);
		printf ("%s", line);
	}
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

void reverse(char s[])
{
	int i,n = 0;
	char tmp[MAXLINE];
		
	for(i = 0; s[i] != '\0'; ++i)
		tmp[i] = s[i];
		
	for(--i; i >= 0; --i)
		{
		s[n] = tmp[i];
		n++;
		}

	s[n] = '\n';
	n++;
	s[n] = '\0';
}
