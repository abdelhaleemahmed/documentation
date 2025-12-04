/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
5.10: Command-line Arguments.
Page: 116.
Date: 19 - 06 - 2008.
*/

# include <stdio.h>

/* echo: command-line arguments, 3rd version */
main(int argc, char *argv)
{
	while (--argc > 0)
		printf((argc > 1) ? "%s " : "%s",*++argv);
	printf ("\n");
	return 0;
}