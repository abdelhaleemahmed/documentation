/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
5.7: Multi-dimensional Arrays
Page: 111
Date: 18 - 06 - 2008.
*/

/* Year to day and day to year conversion */

static char daytab[2][13] = {
	{0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30},
	{0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30}
};

/* day_of_year: set day of year from month & day */
int day_of_year(int year, int month, int day)
{
	int i, leap;
	
	leap = year%4 == 0 && year%100 != 0 || year%400 == 0;
	for (i = 1; i < month; i++)
		day += daytab[leap][i];
	return day;
}

/* month_day: set month, day from day of year  */
void month_day(int year, int yearday, int *pmonth, int * pda)
{
	int i, leap;
	
	leap = year%4 == 0 && year%100 != 0 || year%400 == 0;
	for ( i = 1; yearday > daytab[leap][i]; i++)
		yearday -= daytab[leap][i];
	*pmonth = i;
	*pday = yearday;
}
