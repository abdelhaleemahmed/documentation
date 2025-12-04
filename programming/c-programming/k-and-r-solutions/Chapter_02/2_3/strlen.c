
/* strlen: return length of s
Page: 39
Date: 5-6-2008.
*/
int strlen(char [])
{
    int i;

    i = 0;
    while (s[i] != '\0')
	++i;
    return i;
}