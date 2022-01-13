#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <unordered_map>

#define STRIDE (1<<8)

template <class V>
class MyTable {
#ifdef USE_UNORDERED_MAP
	std::unordered_map<unsigned, V> map;
#else
	V *map;
public:
	MyTable() {
		map = (V *)calloc(UINT32_MAX, sizeof(V));
	}
	~MyTable() {
		free(map);
	}
#endif

public:
	V get(unsigned i) {
		return map[i];
	}
	void set(unsigned i, V x) {
		map[i] = x;
	}
};

static void fill(MyTable<double> &table) {
	for (unsigned x = STRIDE; x; x += STRIDE)
		table.set(x, sqrt(x));
}

static double addup(MyTable<double> &table) {
	double t = 0;
	srand(1);
	for (unsigned x = STRIDE; x; x += STRIDE)
		t += table.get(rand());
	return t;
}

int main() {
	MyTable<double> table;

	fill(table);
	double r = addup(table);
	printf("%g\n", r);

	return 0;
}
