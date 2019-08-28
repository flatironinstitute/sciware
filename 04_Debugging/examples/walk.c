#include <dirent.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>

static mode_t file_type(int fd) {
	struct stat st;
	if (fstat(fd, &st) == 0)
		return st.st_mode & S_IFMT;
	return 0;
}

static void visit_file(int fd) {
	char buf[8192];
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
	DIR *d = visit(dfd, path);
	if (!d) return;
	struct dirent *e;
	while ((e = readdir(d)))
		if (e->d_name[0] != '.')
			walk(dirfd(d), e->d_name);
	closedir(d);
}

int main() {
	walk(AT_FDCWD, "/mnt/ceph/users");
}
