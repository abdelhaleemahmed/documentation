/*
Coder: ahmed abdel haleem.
e-mail: ahmedhal@gmail.com
K&R.
3.5: Loops - while and for.
Page: 61.
*/
/* 
The structure of the program reflects the form of the input:
	skip white space, if any
	get sign, if any
	get integer part and convert it
Each step does its part, and leaves things in a clean state for the next. The whole process terminates on the first character that could not be part of a number.
 */
#include <ctype.h>

/* atoi: convert s to integer; version */
int atoi(char s[])
{
	int i, n ,sign;
	
	for (i = 0; isspace(s[i]); i++) /* ski[ white space */
		;
	sign = (s[i] == '-') ? -1 : 1;
	if (s[i] == '+' || s[i] == '-') /* Skip sign */
		i++;
	for (n = 0; isdigit(s[i]); i++)
		n = 10 * n + (s[i] - '0');
	return sign * n;
}

/*
The standerd library provides a more elaborate function STRTOL for conversion of strings to long integers; see section  of Appendix B.
*/
