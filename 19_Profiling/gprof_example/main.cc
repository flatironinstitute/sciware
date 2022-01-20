#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <unordered_map>

#define STRIDE 256
#define COUNT (UINT32_MAX/STRIDE)

template <class V>
class MyTable {
#ifdef USE_UNORDERED_MAP
	/* sparse array */
	std::unordered_map<unsigned, V> map;
#else
	/* dense array (4B) */
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
	V &index(unsigned i) {
		return map[i];
	}
	V get(unsigned i) {
		return this->index(i);
	}
	void set(unsigned i, V x) {
		this->index(i) = x;
	}
};

/* set values in some subset of table entries (every STRIDE) */
static void fill(MyTable<double> &table) {
	for (unsigned x = 0; x < COUNT; x++)
		table.set(STRIDE*x, sqrt((double)x));
}

/* add up some (pseudo-)random entries */
static double addup(MyTable<double> &table) {
	double t = 0;
	srand(1);
	for (unsigned x = 0; x < COUNT; x ++)
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
