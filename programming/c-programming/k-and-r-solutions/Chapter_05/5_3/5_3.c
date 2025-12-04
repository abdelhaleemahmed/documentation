/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
5.3: Pointers and Arrays.
Page: 99
Date: 18 - 06 - 2008.
*/

/* strlen: return length of string. */

int strlen(char *s){
	int n;
	
	for (n = 0; *s != '\0'; s++)
		n++;
	return n;
}
