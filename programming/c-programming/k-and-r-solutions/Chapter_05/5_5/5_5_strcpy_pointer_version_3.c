/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
5.5: Character Pointers and Functions.
Page: 106
Date: 18 - 06 - 2008.
*/
/* strcpy: copy t to s; pointer version 3 */
void strcpy(char *s, char *t)
{
	while(*s++ = *t++) /* note the difference between *s++ and (*s)++  */
		;
}
