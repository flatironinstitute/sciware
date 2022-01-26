#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <unordered_map>
#include <omp.h>

template <class V>
class MyTable {
#ifdef USE_UNORDERED_MAP
	/* sparse array: only store values as assigned */
	std::unordered_map<unsigned, V> map;

#else
	/* dense array: pre-allocate 4B entries */
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
#ifdef USE_UNORDERED_MAP
		if (!map.contains(i))
			return 0;
#endif
		return this->index(i);
	}
	void set(unsigned i, V x) {
		this->index(i) = x;
	}
};

#define COUNT (UINT32_MAX/256)

/* set values in some subset of table entries (every STRIDE) */
static void fill(MyTable<double> &table) {
	for (unsigned x = 0; x < COUNT; x++)
		table.set(rand(), sqrt((double)x));
}

/* add up some (pseudo-)random entries */
static double addup(MyTable<double> &table) {
	double t = 0;
	for (unsigned x = 0; x < COUNT; x ++)
		t += sqrt(table.get(rand()));
	return t;
}

static inline double timer() {
	/* see also gettimeofday, std::chrono */
	return omp_get_wtime();
}

int main() {
	double t0, t1, t2, t3;
	srand(1);

	t0 = timer();
	MyTable<double> table;
	t1 = timer();
	fill(table);
	t2 = timer();
	double r = addup(table);
	t3 = timer();
	printf("init=%f fill=%f add=%f total=%f res=%g\n", t1-t0, t2-t1, t3-t2, t3-t0, r);

	return 0;
}
