#include <stdio.h>

int main() {
	char buf[256];
	for(;;) {
		FILE *f = fopen("open.c", "r");
		fread(buf, 1, sizeof(buf), f);
		fclose(f);
	}
}
