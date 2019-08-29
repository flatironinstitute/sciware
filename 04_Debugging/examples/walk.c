#include <dirent.h>
#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>

static unsigned long long count;

static mode_t file_type(int fd) {
	struct stat st;
	if (fstat(fd, &st) == 0)
		return st.st_mode & S_IFMT;
	return 0;
}

static void visit_file(int fd) {
	static char buf[1024*1024];
	read(fd, buf, sizeof(buf));
}

static DIR *visit(int dfd, char *path) {
	int fd = openat(dfd, path, O_RDONLY|O_NOFOLLOW);
	if (fd < 0) return NULL;
	switch (file_type(fd)) {
		case S_IFREG:
			visit_file(fd);
			break;
		case S_IFDIR: {
			DIR *d = fdopendir(fd);
			if (d) return d;
		}
	}
	close(fd);
	return NULL;
}

static void walk(int dfd, char *path) {
	count++;
	DIR *d = visit(dfd, path);
	if (!d) return;
	struct dirent *e;
	while ((e = readdir(d)))
		if (e->d_name[0] != '.')
			walk(dirfd(d), e->d_name);
	closedir(d);
}

int main(int argc, char **argv) {
	walk(AT_FDCWD, argc > 1 ? argv[1] : "/mnt/ceph/users");
	printf("%llu\n", count);
	return 0;
}
