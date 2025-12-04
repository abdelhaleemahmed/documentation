/*
Coder: Ahmed abdel haleem.
e-mail: ahmedhal@google.com.
k&R.
EX: Write alternate version of squeeze(s1,s2) that deletes each character in s1 that matches any character in the string s2.
Date: 5 - 6 - 2008.
Page: 48.
*/
#include<stdio.h>
#define MAXLINE 100

void squeeze(char [], char []);
void getline(char [], int);

main()
{
	char sa[MAXLINE];
	char sb[MAXLINE];
	
	getline(sa, MAXLINE);
	getline(sb,MAXLINE);
	
	printf("\ns1 contains : %s \n",sa);
	printf("s2 contains : %s \n",sb);
	
	squeeze(sa,sb);
	printf("%s \n",sa);
}

/* THis one depend on the same logic which we use on multiplcation table even the NULL character was a NEW LINE in the same place */
void squeeze(char s1[], char s2[])
{
	int i , j,l;
	
	for (l = 0; s2[l] != '\0'; l++){
	for(i = j = 0; s1[i] != '\0'; i++){
		if (s1[i] != s2[l])
			s1[j++] = s1[i];
	}
	s1[j] = '\0';
	}
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
