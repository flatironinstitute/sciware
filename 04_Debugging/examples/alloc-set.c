#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

static const size_t BLOCK_SIZE = 16*1024*1024;

int main() {
	unsigned long long x = 0;
	for (x = 0;; x++) {
		printf("%llu\n", x);
		char *b = malloc(BLOCK_SIZE);
		memset(b, 0, BLOCK_SIZE);
		sleep(1);
	}
}
