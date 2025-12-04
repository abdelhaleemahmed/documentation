/*
squeeze: delete all c from s.
k&R.
Page: 47.
Date: 5-6-2008
 */

/* THis one depend on the same logic which we use on multiplication table even the NULL character was a NEW LINE in the same place */
void squeeze(char s1[], char s2[])
{
	int i , j,l;

	for (l = 0; s2[l] != '\0'; l++){
	for(i = j = 0; s1[i] != '\0'; i++){
		if (s1[i] != s2[l])
			s1[j++] = s1[i];
	}
	s1[j] = '\0';
	}
}
