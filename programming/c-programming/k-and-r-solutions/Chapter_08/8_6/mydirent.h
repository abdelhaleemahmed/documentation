/*
Coder: ahmed abdel haleem.
E-mail: ahmedhal@gmil.com
K&R.
8.6: Example - Listing Directories.
Date: 25 - 06 - 2008
*/
#include <sys/dir.h>

/* #define NAME_MAX 14 */ /* Longest filename component; */
					/* System-dependent */



typedef struct mydiren{			/* portable directory entry: */
	long ino;				/* inode number */
	char name[NAME_MAX+1];  /* name + '\0' terminator */
} myDirent;

typedef struct mydr{			/* minimal DIR: no buffering, etc. */
	int fd;					/* file descriptor for directory */
	myDIRent d;				/* the directory entry */
} myDIR;

myDIR *myopendir(char *dirname);
myDirent *myreaddir(myDIR *dfd);
void myclosedir(myDIR *dfd);


/* int fstat(in fd, struct stat *);*/

/* opendir: open a directory for readdir calls */
myDIR *myopendir(char *dirname)
{
	int fd;
	struct stat stbuf;
	myDIR *dp;
	
	if ((fd = open(dirname, O_RDONLY, 0)) == -1 || fstat(fd, &stbuf) == -1 || (stbuf.st_mode & S_IFMT) != S_IFDIR || (dp = (myDIR *)malloc(sizeof(myDIR))) == NULL)
		return NULL;
	dp->fd = fd;
	return dp;
}

/* closedir: close directory opend by opendir */
void myclosedir(myDIR *dp)
{
	if (dp){
		close(dp->fd);
		free(dp);
	}
}

/*readdir: read directory entries in sequence  */
myDirent *myreaddir(myDIR *dp)
{
	struct direct dirbuf;		/* Local directory structure */
	static myDirent d;			/* return: portable structure */
	
	while(read(dp->fd, (char *)&dirbuf, sizeof(dirbuf)) == sizeof(dirbuf)){
		if (dirbuf.d_ino == 0)	/* slot not in use */ /* What is this and why?. */
			continue;
		d.ino = dirbuf.d_ino;
		strncpy(d.name, dirbuf.d_name, DIRSIZE);
		d.name[DIRSIZE] = '\0'; /* ensure termination */
		return &d;
	}
	return NULL;
}
