#include <stdio.h>
#include <unistd.h>

int main() {
	unsigned long long x = 0;
	for (x = 0;; x++) {
		printf("%llu\n", x);
		fflush(stdout);
		sleep(1);
	}
}
