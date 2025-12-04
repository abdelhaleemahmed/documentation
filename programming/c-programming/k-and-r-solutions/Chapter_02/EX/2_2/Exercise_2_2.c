/*
Coder: ahmed abdel haleem.
Date: 1 - 6 -2008.
e-mail: ahmedhal@gmail.com.
EX: 2-2; write a loop equivalent to the for loop a bove without using && or ||. ( for i=0;i<lim-1&& ( c = getchar() ) != '\n' && c != EOF ; ++i ) s[ i] = c;
Page: 42.
*/
for(i = 0; i < lim-1; ++i)
{
	if ((c = getchar()) != '\n')
		if (c != 'EOF')
			s[i] = c;
}

