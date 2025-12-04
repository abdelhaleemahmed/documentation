/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
5.10: Command-line Arguments.
Page: 115.
Date: 19 - 06 - 2008.
*/

#include <stdio.h>

/* echo: command-line arguments; 1st version */
main(int argc, char *argv[])
{
	int i;
	
	for (i = 1; i < argc; i++)
		printf ("%s%s", *++argv, (argc > 1) ? " " : "");
	printf ("\n");
	return 0;
}
