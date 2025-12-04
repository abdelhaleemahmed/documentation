/*
Coder: ahmed abdel haleem ahmed.
e-mail: ahmedhal@gmail.com
Date: 7-6-2008
K&R.
Page: 58
*/

/*binsearch: find x in v[0] <= v[1] <= ... <= v[n-1] */

/* also known as: Comparison searching

Do man 3 binsearch */

int binsearch(int x, int v[], int n)
{
	int low,high,mid;

	low = 0;
	high = n -1;
	while(low <= high){
		mid = (low+high)/2;
		if(x< v[mid])
			high = mid -1;
		else if (x > v[mid])
			low = mid +1;
		else	/*found match*/
			return mid;
	}
	return -1; /* no match */
}
