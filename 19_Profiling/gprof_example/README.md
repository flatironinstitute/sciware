# gprof example
- [code](main.cc)
- [run script](run.sh), example output:
   ```
   g++ -g -pg -Wall -std=c++20 -fopenmp -o run_array main.cc
   g++ -g -pg -Wall -std=c++20 -fopenmp -DUSE_UNORDERED_MAP=1 -o run_map main.cc

   time ./run_array
   init=0.000010 fill=8.817046 add=2.915686 total=11.732742 res=3.56445e+08
   5.51user 7.62system 0:13.14elapsed 99%CPU (0avgtext+0avgdata 16472988maxresident)k

   time ./run_map
   init=0.000003 fill=31.427033 add=11.878583 total=43.305619 res=3.56445e+08
   47.03user 0.94system 0:47.98elapsed 99%CPU (0avgtext+0avgdata 717676maxresident)k
   ```
- example gprof output: [array](gprof_array.txt), [map](gprof_map.txt)
