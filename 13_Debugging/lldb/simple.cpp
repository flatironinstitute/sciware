// Compile with: clang++ -g -std=c++20 -o simple simple.cpp

#include <iostream>
#include <vector>
#include <string>

struct coord {
  int x;
  int y;
};

auto square(auto x) { return x * x; }

int main() {

  auto s = std::string{"Hello there!"};

  // ---- std::vector ----

  auto ints = std::vector{0, 1, 1, 2, 3, 5};

  std::cout << ints[0] << "\n";

  for (auto i : ints)
    std::cout << square(i) << "\n";

  ints[0] = 10;

  // ---- custom types -----

  auto coords = std::vector<coord>{{0, 0}, {1, 1}};

  coords.push_back({4, 6});

  for (auto &[x, y] : coords)
    x = square(x);

  return 0;
}
