/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
5.10: Command-line Arguments.
Page: 116.
Date: 19 - 06 - 2008.
*/

#include <stdio.h>
#include <string.h>
#define MAXLINE 1000

int getline(char line[], int max);

/* find: print lines that match pattren from 1st arg*/
main(int argc, char *argv[])
{
	char line[MAXLINE];
	int found = 0;
	
	if (argc != 2)
		printf("Usage: find pattern\n");
	else
		while (getline(line, MAXLINE) > 0)
			if (strstr(line, argv[1]) != NULL){
				printf("%s", line);
				found++;
			}
	return found;
}

/* getline: read line into s, return length, (from section 1.9) */
int getline(char line[], int lim)
{
	int c,i;
	
	for(i=0; i<lim-1 && (c = getchar()) != EOF && c != '\n';++i)
		line[i] = c;
	if (c == '\n'){
		line[i++] = c;
	}
	
	line[i] = '\0';
	return i;
}
