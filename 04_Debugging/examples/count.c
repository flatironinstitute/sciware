#include <stdio.h>
#include <sys/time.h>
#include <time.h>
#include <unistd.h>

int main() {
	unsigned long long x = 0;
	struct timeval t;
	for (x = 0;; x++) {
		gettimeofday(&t, NULL);
		printf("%020llu %14ld.%06ld %s", x, t.tv_sec, t.tv_usec, ctime(&t.tv_sec));
		sleep(1);
	}
}
