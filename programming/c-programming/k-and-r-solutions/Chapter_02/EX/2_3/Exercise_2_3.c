/*
Coder: ahmed abdel haleem ahmed.
e-mail: ahmehal@gmail.com
Date:5-6-2008
EX: 2.3: Write htoi(x), including an optional 0x or 0X.
Page:46
*/
/*
Note: htoi(s) is fully functional but hte way in which I call it is the problem, and the sole purpose of the program is to test htoi(s) , so you hav e to exit the program using (ctrl + c) or to replace [while] with [if].
*/
#include<stdio.h>
#define MAXLINE 100

int htoi(char []);
int getline(char [], int);

int main()
{
	int len, re;
 	char line[MAXLINE];
 
	re = len = 0;
	/*while*/if((len = getline(line, MAXLINE)) > 0)
	 {
		re = htoi(line);
        if (re != 0)
			printf("In decimal %d \n",re);
        else
        	printf("IT sames that wasn't a valid hex digit try again.\n");
	 }
	return 0;
}

int htoi(char s[])
{
	int i;
	
	i = 0;
	while(s[i] == '0' || s[i] == 'x' || s[i] == 'X')
			++i;
	for(; s[i] != '\0'; i++)
	 {
		if(isdigit(s[i]))
			return (s[i] - '0');
		else if(s[i] >= 'A' && s[i] <= 'F')
			return (s[i] - '7');
		else if (s[i] >= 'a' && s[i] <= 'f' )
			return (s[i] - 'W');
	 }
	return 0;
}

int getline(char s[], int lim)
{
	int i,c;
	
	for(i = 0; i < lim-1 && ((c = getchar()) != EOF) && c != '\n'; ++i)
		s[i] = c;
	if (c = '\n')
	{
		s[i] = c;
		++i;
	}
	s[i] = '\0';
	return i;
}
