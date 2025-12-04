/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
5.5: Character Pointers and Functions.
Page: 105
Date: 18 - 06 - 2008.
*/
/* strcpy: copy t to s; array subscript version */
void strcpy()
{
	int i;
	
	i = 0;
	while((s[i] = t[i]) != '\0')
		i++;
}
