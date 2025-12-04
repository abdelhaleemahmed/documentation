/*
coder: ahmed abdel haleem
e-mail: ahmedhal@gmail.com
Date:29-5-2008
K&R.
EX: 1-18, write a program to remove trailing blanks and tabs from each line of input, and to delete entirely blank lines.
Page: 31.
*/
#include <stdio.h>
#define MAXLINE 100
#define nlinenull 2

int getline (char [], int , int);
int removeblanks(char [], int );
void print_blanks(char []);

main()
 {
	
	int len, c, nlen ,start = 0;
	char line[MAXLINE];

	while((c = getchar()) != EOF )
	 {
		
		line[start] = c;
		start++;
		if((len = getline(line, MAXLINE, start)) > 0 )
		{
			printf("before removing blanks: ");
			print_blanks(line);
			
			nlen = removeblanks(line ,len);
			if ( nlen > 0 )
			{
				printf("%s", line);
				start = 0;
			}
			else start = 0;
		}
		
	 }

 }

 int getline(char s[], int lim, int st)
 {
	int c,i = 0;

	for (i = st && i < lim -1; (c = getchar()) != EOF && c != '\n'; ++i )
		s[i] = c;
	if (c = '\n')
	 {
		s[i] = '\n';
		i++;
	 }
	s[i] = '\0';
	return i;
 }
 
 int removeblanks(char s[], int l)
  {
	int i;
	
	for ( i = (l-=nlinenull); s[i] == ' ' ||  s[i] == '\t'; i--)
		;
	s[++i] = '\n';
	s[++i] = '\0';
	
	return i;
  }
 
 void print_blanks(char s[])
{
	int i = 0;
	while(s[i] != '\0' ){
		if( s[i] == '\t' )
			printf("\\t");
		else if( s[i] == '\b' )
			printf("\\b");
		else if( s[i] == '\\')
			printf( "\\\\" );
		else if(s[i] == ' ')
			printf("_");
		else putchar(s[i]);
		
		i++;
	}
}
 