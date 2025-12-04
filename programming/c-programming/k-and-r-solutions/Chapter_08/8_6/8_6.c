/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmil.com
K&R.
8.6: Example - Listing Directories.
Date: 25 - 06 - 2008
*/
#include <stdio.h>
#include <string.h>
#include <sys/syscall.h>
#include <fcntl.h>			/* flags for read and write */
#include <sys/types.h>		/* typdefs */
#include <sys/stat.h>		/* structure returned by stat */
#include "mydirent.h"		/* since GNU C ext have the same header */

void fsize(char *);

/* Print file sizes */
main(int argc, char **argv)
{
	if (argc == 1)		/* default: current directory */
		fsize(".");
	else
		while(--argc >0)
			fsize(*++argv);
	return 0;
}

/* int stat(char *, struct stat *); */
void mydirwalk(char *, void(*fcn)(char *));

/* fsize: print size of file "name" */
void fsize(char *name)
{
	struct stat stbuf;
	
	if (stat(name, &stbuf) == -1){
		fprintf(stderr, "fsize: can't access %s", name);
		return;
	}
	if((stbuf.st_mode & S_IFMT) == S_IFDIR)
		mydirwalk(name, fsize);
	printf("%8ld %s\n", stbuf.st_size, name);
}

#define MAX_PATH 1024

/* dirwalk: apply fcn to all files in dir */
void mydirwalk(char *dir, void(*fcn)(char *))
{
	char name[MAX_PATH];
	myDirent *dp;
	myDIR *dfd;
	
	if((dfd = myopendir(dir)) == NULL){
		fprintf(stderr, "dirwalk: can't open %s\n", dir);
		return;
	}
	while ((dp = myreaddir(dfd)) != NULL){
		if (strcmp(dp->name, ".") == 0 || strcmp(dp->nme, ..) == 0)
			continue;	/* Skip self and parent */
		if (strlen(dir) + strlen(dp->name) + 2 > sizeof(name))
			fprintf(stderr, "mydirwalk: name %s %s too long\n", dir, dp->name);
		else {
			sprintf(name, "%s/%s", dir, dp->name);
			(*fcn)(name);
		}
	}
	closedir(dfd);
}


