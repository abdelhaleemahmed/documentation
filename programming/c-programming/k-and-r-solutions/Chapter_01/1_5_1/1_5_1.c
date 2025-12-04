/*
Coder: ahmed abdel haleem
e-mail: ahmedhal@gmail.com
Date:25-5-2008
K&R.
1.5.1: File Copying.
page: 16.
*/
#include <stdio.h>
main(){
	int c;
	
	c = getchar();
	while (c != EOF){
		putchar(c);
		c = getchar();
	}
}
