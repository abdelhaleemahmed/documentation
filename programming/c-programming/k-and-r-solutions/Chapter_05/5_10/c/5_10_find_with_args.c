/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
5.10: Command-line Arguments.
Page: 117.
Date: 19 - 06 - 2008.
*/

#include <stdio.h>
#include <string.h>
#define MAXLINE 1000

int getline(char *line, int max);

/* find: print lines that match pattern from 1st arg */
main(int argc, char *argv[])
{
	char line[MAXLINE];
	long lineno = 0;
	int c, except = 0, number = 0, found = 0;
	
	while (--argc > 0 && (*++argv)[0] == '-')
		while (c = *++argv[0])
			switch (c) {
			case 'x':
				except = 1;
				break;
			case 'n':
				number = 1;
				break;
			default:
				printf("find: illegal option %c\n",c);
				argc = 0;
				found = -1;
				break;
			}
	if (argc != 1)
		printf ("Usage: find -x -n patteren\n");
	else
		while (getline(line, MAXLINE) > 0){
			lineno++;
			if ((strstr(line, *argv) != NULL) != except) {
				if (number)
					printf("%ld:", lineno);
				printf("%s",line);
				found++;
			}
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
