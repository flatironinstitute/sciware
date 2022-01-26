# gprof example
- [code](main.cc)
- [run script](run), example output:
   ```
   g++ -g -pg -Wall -std=c++20 -fopenmp -o run_array main.cc
   g++ -g -pg -Wall -std=c++20 -fopenmp -DUSE_UNORDERED_MAP=1 -o run_map main.cc

   time ./run_array
   init=0.000013 fill=12.779974 add=3.156935 sum=1.2692e+08
   4.89user 11.81system 0:16.71elapsed 100%CPU (0avgtext+0avgdata 33557300maxresident)k

   time ./run_map
   init=0.000004 fill=24.568832 add=10.684079 sum=1.2692e+08
   38.09user 0.62system 0:38.71elapsed 99%CPU (0avgtext+0avgdata 719400maxresident)k
   ```
- example gprof output: [array](gprof_array), [map](gprof_map)
