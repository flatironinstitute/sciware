#include <c2py/c2py.hpp>

struct S {
  int i;

  S(int i):i{i}{}

  int m() const { return i+2;}
};

// A function using S
int f(S const & s){ return s.i;}

// make S printable in C++
std::ostream & operator<<(std::ostream &out, S const & s) {return out << "S struct with i=" << s.i << '\n';}

