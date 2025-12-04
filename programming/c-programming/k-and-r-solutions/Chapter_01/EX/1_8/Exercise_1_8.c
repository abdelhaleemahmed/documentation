/*
coder: ahmed abdel haleem
Date:26-5-2008
K&R.
EX: 1-8, Count balnks, tabs, and newlines.
Page: 20.
*/
#include <stdio.h>

main(){

	int c;
	int nb,nt,nl;
	
	nb = nt = nl = 0;
	
	while((c = getchar()) != EOF){
		if (c == ' ')
			nb++;
		if (c == '\t')
			nt++;
		if (c == '\n')
			nl++;
	}
	
	printf (" Number of blanks: %d\n Number of tabs: %d\n Number of lines: %d\n",nb,nt,nl);
}
