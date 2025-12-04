/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
5.5: Character Pointers and Functions.
Page: 106
Date: 18 - 06 - 2008.
*/
/* strcmp: return <0 if s<t, 0 if s==t, >0 if s>t */
int strcmp (char *s, char *t)
{
	int i;
	
	for ( i = 0;s[i] == t[i]; i++ )
		if (s[i] == '\0')
			return 0;
	return s[i] - t[i];
}
