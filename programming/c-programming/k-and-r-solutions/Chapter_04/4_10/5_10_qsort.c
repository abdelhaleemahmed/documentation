/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmail.com
K&R.
4.10: Recursion.
Page: 87 - 88.
Date: 19 - 06 - 2008.
*/
/* Another good example of recursion is quicksort., a sorting algorithm developed by C. A. R. Hoare in 1962. Given an array, one element is chosen and the others are paritioned into two subsets - those less than the partition 
element and those greater than or equal to it. The same process is then applied recursively to the two subsets. When a subset has fewer than two elements, it doesn't need any sorting; this stops the recursion
 */

 /* qsort: sort v[left] . . . v[right] into increasing order */
 void qsort(int v[], int left, int right)
 {
	int i, last;
	void swap(int v[], int left, int right);
	
	if (left >= right)		/* do nothing if array contains */
		return;				/* fewer than two elements */
	swap(v, left, (left+right)/2);	/* move partition element */
	last = left;					/* to v[0] ( we sort base on this one)  */
	for (i = left + 1; i <= right; i++)	/* partition */
		if (v[i] < v[left])
			swap (v, ++last, i);
	swap (v, left, last);			/* restore partition elem */
	qsort(v, left, last-1);
	qsort(v, last+1, right);
 }
 
 /* swap: interchange v[i] and v[j] */
 void swap(int v[], int i, int j)
 {
	int temp;
	
	temp = v[i];
	v[i] = v[j];
	v[j] = temp;
 }
