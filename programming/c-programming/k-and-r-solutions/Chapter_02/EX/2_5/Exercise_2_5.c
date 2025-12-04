/*
Coder: Ahmed abdel haleem.
e-mail: ahmedhal@google.com.
k&R.
EX: Write the function any(s1,s2), which returns the first location in the string s1 where any character from the string s2 occurs, or -1 if s1 contains no chars from s2.
Date: 5 - 6 - 2008.
Page: 48.
*/
#include<stdio.h>
#define MAXLINE 100

void squeeze(char [], char []);
void getline(char [], int);

main()
{
	signed res = 0;
	char sa[MAXLINE];
	char sb[MAXLINE];
	
	getline(sa, MAXLINE);
	getline(sb,MAXLINE);
	
	printf("\ns1 contains : %s \n",sa);
	printf("s2 contains : %s \n",sb);
	
	res = any(sa,sb);
	if (res >= 0)
		printf("first locations in string a contains characters from string b is: %d\n",res);
	else
		printf("string a contains no characters from string b.\n");
}

/* Same logic which we use in multiplication table */

int any(char s1[], char s2[])
{
	int i , j;
	
	for (j = 0; s2[j] != '\0'; j++)
	for(i = 0; s1[i] != '\0'; i++)
		if (s1[i] == s2[j] )
			return (i+1);
	return -1;
}

/*A littile enhanced version of GETLINE depend on INCREMENT AND DECREMENT OPERATORS rules */
void getline(char line[], int lim)
{
	int c,i;
	
	c = 0;
	for (i = 0; i < lim -1 && ((c = getchar()) != EOF) && c != '\n'; ++i )
		line[i] = c;
	if (c == '\n')
		line[i++] = '\n';
	line[i] = '\0';
}
