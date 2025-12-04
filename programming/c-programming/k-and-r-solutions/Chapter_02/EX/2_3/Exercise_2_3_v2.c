/*
Coder: ahmed abdel haleem ahmed.
e-mail: ahmehal@gmail.com
Date:5-6-2008
EX: 2.3: Write htoi(x), including an optional 0x or 0X.
Page:46
*/
#include<stdio.h>
#include<math.h>

#define MAXLINE 100
#define base 16

int htoi(char );
int getline(char [], int);
//int power(int base, int n);

int main()
{
	int i,indc,h,len,re,pw;
	char line[MAXLINE];
	
	indc = h = len = 0;
	if((len = getline(line, MAXLINE)) > 0)
		for(i = 0; line[i] != '\n' && line[i] != '\0'; ++i);
		for (--i; i >= 0 ; i--)
		{
			indc = indc + (htoi(line[i]) * pow(base,h));
			h++;
		}
	printf("\nindecimal %d\n",indc);
}

int htoi(char s)
{

	if(isdigit(s))
		return (s - '0');
	else if(s >= 'A' && s <= 'F')
		return (s - '7');
	else if (s >= 'a' && s <= 'f' )
		return (s - 'W');
	
	return 0;
}

int getline(char line[], int lim)
{
	int i,c;
	
	for(i = 0; i < lim-1 && ((c = getchar()) != EOF) && c != '\n'; ++i)
		line[i] = c;
	if (c = '\n')
	{
		line[i] = c;
		++i;
	}
	line[i] = '\0';
	return i;
}

/* Power: rise base to n-th power; n >= 0 
int power(int base, int n)
{
	int i, p;
	
	p = 1;
	for(i = 1; i <= n; ++i)
		p = p * base;
	return p;*/
