/*
Coder: ahmed abdel halem.
e-mail: ahmedha@gmail.com
K&R.
3.7: Break and continue.
Page:64.
Date: 11 - 6 - 2008.
*/
/* trim: remove trailing blanks, tabs, newlines */
int trim(char [])
{
	int n;
	
	for (n = strlen(s)-1; n >= 0; n-- )
		if (s[n] != ' ' && s[n] != '\t' && s[n] != '\n')
			break;
		s[n+1] = '\0';
		return n;
}
