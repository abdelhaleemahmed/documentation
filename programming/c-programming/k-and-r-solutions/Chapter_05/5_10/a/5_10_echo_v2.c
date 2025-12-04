/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
5.10: Command-line Arguments.
Page: 115.
Date: 19 - 06 - 2008.
*/

# include <stdio.h>

/* echo: command-line arguments, 2nd version */
main(int argc, char *argv)
{
	while (--argc > 0)
		printf("%s%s", *++argv, (argc > 1) ? " " : "");
	printf ("\n");
	return 0;
}
