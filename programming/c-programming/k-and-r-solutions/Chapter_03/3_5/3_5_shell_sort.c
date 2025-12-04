/*
Coder: ahmed abdel haleem.
e-mail:ahmedhal@gmail.com.
K&R.
3.5: Loops - While and For.
Page: 62.
*/

/*
The following function is a Shell sort for sorting an array of integers. The basic idea of this sorting algorithm, which was invented
in 1959 by D.I. Shell, is that in early stages, far-apart elements are compared, rather than adjacent ones as in simpler interchanges
sorts. This tends to eliminate large amounts of disorder quickly, so later stages have less work to do. The interval between compared
elements is gradually decreased to one, at which point the sort effectively becomes an adjacent interchange method.
*/

/* shellsort: sort v[0]  ... v[n-1] into increasing order*/
void shellsort(int v[], int n)
{
	int gap, i, j, temp;

	for (gap = n/2; gap > 0; gap /= 2)
		for (j=i-gap; j>=0 && v[j]>v[j+gap]; j-=gap){
			temp = v[j];
			v[j] = v[j+gap];
			v[j+gap] = temp;
		}
}
