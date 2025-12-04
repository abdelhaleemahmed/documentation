/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
5.8: Initialization of Pointer Arrays.
Page: 113.
Date: 18 - 06 - 2008.
*/

/* month_name: return name of n-th month */
char *month_name()
{
	static char *name[] = {
	"Illegal month",
	"January", "February", "March",
	"April", "May", "June",
	"July", "August", "September",
	"October", "November", "December"
	};
	
	return (n < 1 || n > 12) ? name[0] : name[n]; /* <--- Nice Code !!! */
}
