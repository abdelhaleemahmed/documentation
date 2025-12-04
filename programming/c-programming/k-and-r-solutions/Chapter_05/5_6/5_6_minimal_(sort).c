/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
5.6: Pointers arrays; Pointers to Pointers.
Page: 107 - 110.
Date: 18 - 06 - 2008.
*/

/* A program that will sort a set of text lines into alphabetic order, a stripped-down version of the UNIX program sort */

/* The sorting process has three steps:
	1- Read all the lines of input.
	2- Sort them.
	3- Print them in order.
*/
#include <stdio.h>
#include <string.h>

#define MAXLINES 5000		/* max #lines to be sorted  */

char *lineptr[MAXLINES];	/* Pointers to text lines */

int readlines(char *lineptr[], int nlines);
void writelines(char *lineptr[], int nlines);

void qsort(char *lineptr[], int left, int right);

/* Sort input lines */
main()
{
	int nlines;		/* number of input lines read */
	
	if((nlines = readlines(lineptr, MAXLINES)) >= 0){
		qsort(lineptr, 0, nlines-1);
		writelines(lineptr, nlines);
		return 0;
	}else {
		printf("error: input too big to sort\n");
		return 1;
	}
}


#define MAXLEN 1000 /* max length of any input line */
int getline(char [], int);

#define ALLOCSIZE 10000 /* size of available space */

static char allocbuf[ALLOCSIZE]; /* storage for alloc  */
static char *allocp = allocbuf; /* next free position */
char *alloc(int);

/* Readlines: readinput lines */
int readlines(char *lineptr[], int maxlines)
{
	int len, nlines;
	char *p, line[MAXLEN];
	
	nlines = 0;
	while((len = getline(line, MAXLEN)) > 0)
		if (nlines >= maxlines || (p = alloc(len)) == NULL)
			return -1;
		else {
			line[len -1] = '\0'; /* delete newline */
			strcpy(p, line);
			lineptr[nlines++] = p;
		}
	return nlines;
}

char *alloc(int n) /* return pointer to n characters */
{
	if (allocbuf + ALLOCSIZE - allocp >= n) { /* It fits */
		allocp += n;
		return allocp -n; /* pld p */
	}else /* not enough room */
		return 0;
}

/* writelines: write output lines */
void writelines(char *lineptr[], int nlines)
{
	int i;
	
	for (i = 0; i < nlines; i++)
		printf("%s\n", lineptr[i]);
}
/*
OR YOU CAN WRIT IT AS:
 Writelines: write output lines.
void writelines(char *lineptr[], int nlines)
{
	while (nlines-- > 0)
		printf("%s\n", *lineptr++);
}
*/

/* getline: read line into s, return length, (from section 1.9) */
int getline(char s[], int lim)
{
	int c,i;
	
	for(i=0; i<lim-1 && (c = getchar()) != EOF && c != '\n';++i)
		s[i] = c;
	if (c == '\n'){
		s[i++] = c;
	}
	
	s[i] = '\0';
	return i;
}

/* qsort: sort v[left] ... v[right] int increasing order */
void qsort(char *v[], int left, int right)
{
	int i, last;
	void swap(char *v[], int i, int j);
	
	if(left >= right)			/* do nothing if array contains fewer than two elements */
		return;
	swap(v, left, (right + left)/2);
	last = left;
	for (i = left+1; i <= right; i++)
		if (strcmp(v[i], v[left]) < 0)
			swap(v, ++last, i);
	swap(v, left, last);
	qsort(v, left, last-1);
	qsort(v, last+1, right);
}

/* swap: interchange v[i] and v[j]  */
void swap(char *v[], int i, int j)
{
	char *temp;
	
	temp = v[i];
	v[i] = v[j];
	v[j] = temp;
}
