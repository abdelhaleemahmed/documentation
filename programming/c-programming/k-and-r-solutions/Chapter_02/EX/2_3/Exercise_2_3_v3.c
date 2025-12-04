/*
Coder: ahmed abdel haleem ahmed.
e-mail: ahmehal@gmail.com
Date:5-6-2008
EX: 2.3: Write htoi(x), including an optional 0x or 0X.
Page:46
*/
#include<stdio.h>

#define MAXLINE 100
#define base16 16

int htoi(const char []);
int getline(char [], int);
int power(int , int );

int main()
{
	char line[MAXLINE];
	int len,re;
	
	len = 0;
	re = 0;
	if((len = getline(line, MAXLINE)) > 0)
	{
		re = htoi(line);
		printf("indecimal %d\n",re);
	}
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

int htoi(const char s[])
{
	int i,j,value,h;
	
	i = value = h = 0;
	while(s[i] == '0' || s[i] == 'x' || s[i] == 'X')
			++i;
	
	for(j = 0; s[j] != '\0'; ++j);
	
	for(--j; j >= i; --j)
	 {
		if(isdigit(s[j]))
		{
			value = value + ((s[j] - '0') * power(base16,h));
			h++;
		}
		else if(s[j] >= 'A' && s[j] <= 'F')
		{
			value = value + ((s[j] - '7') * power(base16,h));
			++h;
		}
		else if (s[j] >= 'a' && s[j] <= 'f' )
		{
			value = value + ((s[j] - 'W') * power(base16,h));
			++h;
		}
	 }
	return value;
}

int power(int base,int n)
{
	int i, p;
	
	p = 1;
	for(i = 1; i <= n; ++i)
		p = p * base;
	return p;
}
