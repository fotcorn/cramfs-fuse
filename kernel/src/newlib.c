#include <sys/types.h>
#include <sys/stat.h>

#include <errno.h>
#undef errno
extern int errno;

#include "screen.h"

int write(int file, char *ptr, int len) {
	int i;
	for(i = 0; i < len; i++) {
		putch(*ptr);
		ptr++;
	}
	return len;
}

caddr_t sbrk(int incr) {
	//putint(incr);

	static char *heap_end = (char*)0x01000000;

	char *prev_heap_end;
	prev_heap_end = heap_end;

	heap_end += incr;
	return (caddr_t) prev_heap_end;
}

char *__env[1] = { 0 };
char **environ = __env;

int read(int file, char *ptr, int len) {
	return 0;
}

int close(int file) {
	return -1;
}

int lseek(int file, int ptr, int dir) {
    return 0;
}

int isatty(int file) {
	return 1;
}

int fstat(int file, struct stat *st) {
	st->st_mode = S_IFCHR;
	return 0;
}

int open(const char *name, int flags, int mode){
    return -1;
}

int stat(const char *file, struct stat *st) {
  st->st_mode = S_IFCHR;
  return 0;
}

clock_t times(struct tms *buf){
	return -1;
}

int unlink(char *name){
  errno=ENOENT;
  return -1;
}

int wait(int *status) {
  errno=ECHILD;
  return -1;
}

int link(char *old, char *new){
  errno=EMLINK;
  return -1;
}

int kill(int pid, int sig){
  errno=EINVAL;
  return(-1);
}

int getpid() {
  return 1;
}

int fork() {
  errno=EAGAIN;
  return -1;
}

int execve(char *name, char **argv, char **env){
  errno=ENOMEM;
  return -1;
}

void _exit(int status) {

}


int *popen(const char *command, const char *type) {
	return 0;
}

int pclose(int *stream) {
	return 0;
}


