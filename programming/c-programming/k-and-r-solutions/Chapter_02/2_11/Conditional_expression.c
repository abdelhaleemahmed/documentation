/*
Coder: ahmed badel haleem.
Date:7-6-2008.
K&R.
Page: 52.
*/
/* Some neat tricks with conditional expressions */
for (i = 0; i < n; i++)
	printf("%6d%c", a[i], (i%10 = 9 || i==n-1) ? '\n' : ' ');

/* A newline is printed after every tenth element, and after the n-th. All other elements are followed by one blank. This might look tricky, but it's more compact than the equivalent if-else */

printf("You have %d item%s.\n", n, n==1 ? "" : "s" );

